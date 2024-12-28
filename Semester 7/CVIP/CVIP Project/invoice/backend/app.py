from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import pytesseract
import torch
import os
from supabase import create_client

# Flask setup
app = Flask(__name__)
CORS(app)

# Upload folder setup
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Supabase credentials
SUPABASE_URL = "https://xchoumvoqnkgpywmiiqg.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhjaG91bXZvcW5rZ3B5d21paXFnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzUxNjg5ODUsImV4cCI6MjA1MDc0NDk4NX0.-kbMao3J8LIal337g_FW2954chEm3kVXXAGaNf3AriY"

# Initialize Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Route: Upload and process invoice file
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # YOLOv5 and OCR Integration
    try:
        detected_data = process_invoice(file_path)
        # Save detected data to Supabase
        save_to_supabase(detected_data)
        return jsonify(detected_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Function: Process Invoice with YOLOv5 and OCR
def process_invoice(file_path):
    # Load YOLOv5 model (ensure model is available in the correct path)
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='models/yolov5s.pt')
    results = model(file_path)

    # Extracting bounding box predictions
    predictions = results.pandas().xyxy[0]  # Convert predictions to pandas DataFrame
    extracted_data = {}

    for _, row in predictions.iterrows():
        label = row['name']  # Label assigned by YOLOv5 model
        xmin, ymin, xmax, ymax = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])

        # Crop image section based on bounding box
        image = Image.open(file_path)
        cropped_image = image.crop((xmin, ymin, xmax, ymax))

        # Apply OCR to the cropped section
        text = pytesseract.image_to_string(cropped_image).strip()
        extracted_data[label] = text

    # Returning structured data
    return {
        "Invoice Number": extracted_data.get("Invoice Number", "Unknown"),
        "Date": extracted_data.get("Date", "Unknown"),
        "Supplier": extracted_data.get("Supplier", "Unknown"),
        "Total Amount": extracted_data.get("Total Amount", "Unknown")
    }

# Function: Save data to Supabase
def save_to_supabase(data):
    try:
        response = supabase.table("invoices").insert([{
            "invoice_number": data.get("Invoice Number"),
            "invoice_date": data.get("Date"),
            "supplier": data.get("Supplier"),
            "total_amount": float(data.get("Total Amount", 0))
        }]).execute()
        if response.get("error"):
            raise Exception(response["error"])
    except Exception as e:
        print("Error saving to Supabase:", e)
        raise

@app.route('/invoices', methods=['GET'])
def get_filtered_invoices():
    try:
        # Retrieve query parameters
        trader_name = request.args.get('trader_name', '').lower()
        from_date = request.args.get('from_date')
        to_date = request.args.get('to_date')

        # Log the query parameters for debugging
        print(f"Received query parameters: trader_name={trader_name}, from_date={from_date}, to_date={to_date}")

        # Base query for invoices
        response = supabase.table("invoices").select(
            """
            id,
            invoice_number,
            invoice_date,
            term_of_sale,
            supplier_id,
            buyer_id,
            total_quantity,
            total_amount_excluding,
            sales_tax_total,
            net_tax_inclusive,
            uploaded_at
            """
        ).execute()

        # Check if the response contains data
        if response.data is None:
            return jsonify({"message": "No invoices found"}), 200

        invoices = response.data

        # Fetch supplier and buyer details
        supplier_response = supabase.table("suppliers").select("id, name").execute()
        buyer_response = supabase.table("buyers").select("id, name").execute()

        if supplier_response.data is None or buyer_response.data is None:
            return jsonify({"error": "Failed to fetch supplier or buyer data"}), 500

        suppliers = {s["id"]: s["name"].lower() for s in supplier_response.data}
        buyers = {b["id"]: b["name"].lower() for b in buyer_response.data}

        # Filter by trader name if provided
        if trader_name:
            invoices = [
                invoice for invoice in invoices
                if (
                    suppliers.get(invoice["supplier_id"], "").find(trader_name) != -1 or
                    buyers.get(invoice["buyer_id"], "").find(trader_name) != -1
                )
            ]

        # Filter by date range if provided
        if from_date:
            invoices = [invoice for invoice in invoices if invoice["invoice_date"] >= from_date]
        if to_date:
            invoices = [invoice for invoice in invoices if invoice["invoice_date"] <= to_date]

        # Attach supplier and buyer names to invoices
        for invoice in invoices:
            invoice["supplier_name"] = suppliers.get(invoice["supplier_id"], "Unknown")
            invoice["buyer_name"] = buyers.get(invoice["buyer_id"], "Unknown")

        # Log the filtered results for debugging
        print(f"Filtered invoices: {invoices}")

        return jsonify(invoices), 200

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
