import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import FileUpload from "./components/file_upload";
import ExtractedForm from "./components/extracted_form";
import CrudOperations from "./components/crud_operations";

function App() {
    const [extractedData, setExtractedData] = useState(null);

    const handleDataSubmit = (data) => {
        console.log("Validated Data:", data);
    };

    return (
        <Router>
            <div className="bg-gray-100 min-h-screen">
                <Routes>
                    <Route
                        path="/"
                        element={
                            <>
                                <FileUpload setExtractedData={setExtractedData} />
                                {extractedData && (
                                    <ExtractedForm data={extractedData} onSubmit={handleDataSubmit} />
                                )}
                            </>
                        }
                    />
                    <Route path="/crudOperations" element={<CrudOperations />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
