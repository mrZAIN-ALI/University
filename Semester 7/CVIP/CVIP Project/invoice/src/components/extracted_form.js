import React from "react";

const ExtractedForm = ({ data, onSubmit }) => {
    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit(data);
    };

    return (
        <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow-md">
            <h2 className="text-2xl font-semibold mb-4">Extracted Invoice Data</h2>
            <div>
                <label className="block mb-2">Invoice Number:</label>
                <input type="text" value={data?.invoiceNumber || ""} readOnly className="p-2 border rounded w-full" />
            </div>
            <div>
                <label className="block mb-2">Date:</label>
                <input type="text" value={data?.date || ""} readOnly className="p-2 border rounded w-full" />
            </div>
            {/* Add more fields for supplier, items, etc. */}
            <button type="submit" className="px-4 py-2 bg-green-500 text-white rounded">Submit</button>
        </form>
    );
};

export default ExtractedForm;
