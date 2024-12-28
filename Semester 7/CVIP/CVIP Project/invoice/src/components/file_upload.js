import React, { useState } from "react";
import { Link } from "react-router-dom";
import { uploadFile } from "../api";

const FileUpload = () => {
    const [file, setFile] = useState(null);
    const [preview, setPreview] = useState(null);
    const [response, setResponse] = useState(null);

    // Handle file selection
    const handleFileChange = (e) => {
        const selectedFile = e.target.files[0];
        setFile(selectedFile);
        setPreview(URL.createObjectURL(selectedFile));
    };

    // Handle file upload
    const handleSubmit = async () => {
        if (!file) {
            alert("Please select a file.");
            return;
        }
        try {
            const data = await uploadFile(file);
            setResponse(data);
        } catch (error) {
            console.error("Failed to upload file:", error);
            alert("Failed to upload file. Please try again.");
        }
    };

    return (
        <div className="min-h-screen flex flex-col">
            {/* Navbar */}
            <nav className="bg-gray-900 text-white py-4">
                <div className="container mx-auto flex justify-between items-center">
                    <h1 className="text-2xl font-bold">Invoice Management</h1>
                    <ul className="flex space-x-4">
                        <li>
                            <Link to="/" className="hover:text-yellow-500">
                                Home
                            </Link>
                        </li>
                        <li>
                            <Link to="/crudOperations" className="hover:text-yellow-500">
                                CRUD Operations
                            </Link>
                        </li>
                    </ul>
                </div>
            </nav>

            {/* Main Content */}
            <main className="flex-grow bg-gray-100 py-8">
                <div className="container mx-auto text-center">
                    <h2 className="text-3xl font-semibold mb-6">Upload Your Invoice</h2>
                    <div className="bg-white shadow-md rounded-lg p-6 mx-auto max-w-md">
                        {/* File Input */}
                        <input
                            type="file"
                            onChange={handleFileChange}
                            className="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-500 file:text-white hover:file:bg-blue-600"
                        />
                        {preview && (
                            <div className="mt-4">
                                <h3 className="font-semibold mb-2">Preview:</h3>
                                <img
                                    src={preview}
                                    alt="Preview"
                                    className="w-full h-auto rounded-md shadow-md"
                                />
                            </div>
                        )}
                        {/* Upload Button */}
                        <button
                            onClick={handleSubmit}
                            className="mt-6 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
                        >
                            Upload
                        </button>
                        {/* Response Display */}
                        {response && (
                            <div className="mt-6 bg-gray-200 p-4 rounded shadow">
                                <h3 className="font-semibold mb-2">Extracted Data:</h3>
                                <pre className="text-left">{JSON.stringify(response, null, 2)}</pre>
                            </div>
                        )}
                    </div>
                </div>
            </main>

            {/* Footer */}
            <footer className="bg-gray-900 text-white py-4">
                <div className="container mx-auto text-center">
                    <p>© 2024 Invoice Management System. All rights reserved.</p>
                </div>
            </footer>
        </div>
    );
};

export default FileUpload;
