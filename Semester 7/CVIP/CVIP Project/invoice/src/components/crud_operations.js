import React, { useState, useEffect } from "react";
import axios from "axios";

const CrudOperations = () => {
    const [invoices, setInvoices] = useState([]);
    const [searchQuery, setSearchQuery] = useState("");
    const [dateRange, setDateRange] = useState({ from: "", to: "" });
    const [filteredInvoices, setFilteredInvoices] = useState([]);

    // Fetch invoices from the backend
    const fetchInvoices = async () => {
        try {
            const params = new URLSearchParams();
            if (searchQuery) params.append("trader_name", searchQuery);
            if (dateRange.from) params.append("from_date", dateRange.from);
            if (dateRange.to) params.append("to_date", dateRange.to);

            const response = await axios.get(`http://127.0.0.1:5000/invoices?${params.toString()}`);
            setFilteredInvoices(response.data);
        } catch (error) {
            console.error("Failed to fetch invoices:", error);
        }
    };

    // Load all invoices on initial render
    useEffect(() => {
        fetchInvoices();
    }, []);

    // Handle search by trader name
    const handleSearch = async () => {
        await fetchInvoices();
    };

    // Handle filters by date range
    const handleFilters = async () => {
        await fetchInvoices();
    };

    // Clear all filters and search
    const clearFilters = async () => {
        setSearchQuery("");
        setDateRange({ from: "", to: "" });
        await fetchInvoices(); // Fetch all invoices
    };

    return (
        <div className="min-h-screen flex flex-col">
            {/* Navbar */}
            <nav className="bg-gray-900 text-white py-4">
                <div className="container mx-auto flex justify-between items-center">
                    <h1 className="text-2xl font-bold">CRUD Operations</h1>
                    <ul className="flex space-x-4">
                        <li>
                            <a href="/" className="hover:text-yellow-500">
                                Home
                            </a>
                        </li>
                    </ul>
                </div>
            </nav>

            {/* Main Content */}
            <main className="flex-grow bg-gray-100 py-8">
                <div className="container mx-auto">
                    <h2 className="text-3xl font-semibold mb-6 text-center">Invoice Management</h2>

                    {/* Search Section */}
                    <div className="bg-white p-6 rounded-lg shadow mb-4">
                        <h3 className="text-lg font-semibold mb-4">Search Invoices</h3>
                        <div className="flex gap-4">
                            <input
                                type="text"
                                placeholder="Search by trader name..."
                                value={searchQuery}
                                onChange={(e) => setSearchQuery(e.target.value)}
                                className="p-2 border rounded flex-grow"
                            />
                            <button
                                onClick={handleSearch}
                                className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
                            >
                                Search
                            </button>
                        </div>
                    </div>

                    {/* Filters Section */}
                    <div className="bg-white p-6 rounded-lg shadow mb-8">
                        <h3 className="text-lg font-semibold mb-4">Filter Invoices</h3>
                        <div className="flex gap-4">
                            <input
                                type="date"
                                value={dateRange.from}
                                onChange={(e) => setDateRange({ ...dateRange, from: e.target.value })}
                                className="p-2 border rounded"
                            />
                            <input
                                type="date"
                                value={dateRange.to}
                                onChange={(e) => setDateRange({ ...dateRange, to: e.target.value })}
                                className="p-2 border rounded"
                            />
                            <button
                                onClick={handleFilters}
                                className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
                            >
                                Apply Filters
                            </button>
                            <button
                                onClick={clearFilters}
                                className="bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600"
                            >
                                Clear Filters
                            </button>
                        </div>
                    </div>

                    {/* Invoices Table */}
                    <div className="bg-white p-6 rounded-lg shadow">
                        <h3 className="text-lg font-semibold mb-4">Invoices</h3>
                        <table className="table-auto w-full border-collapse border border-gray-200">
                            <thead>
                                <tr className="bg-gray-200">
                                    <th className="p-2 border border-gray-300">Invoice Number</th>
                                    <th className="p-2 border border-gray-300">Date</th>
                                    <th className="p-2 border border-gray-300">Supplier</th>
                                    <th className="p-2 border border-gray-300">Total Amount</th>
                                </tr>
                            </thead>
                            <tbody>
                                {filteredInvoices.length > 0 ? (
                                    filteredInvoices.map((invoice) => (
                                        <tr key={invoice.id} className="hover:bg-gray-100">
                                            <td className="p-2 border border-gray-300">{invoice.invoice_number}</td>
                                            <td className="p-2 border border-gray-300">{invoice.invoice_date}</td>
                                            <td className="p-2 border border-gray-300">{invoice.supplier}</td>
                                            <td className="p-2 border border-gray-300">{invoice.total_amount}</td>
                                        </tr>
                                    ))
                                ) : (
                                    <tr>
                                        <td colSpan="4" className="p-2 text-center">
                                            No invoices found.
                                        </td>
                                    </tr>
                                )}
                            </tbody>
                        </table>
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

export default CrudOperations;
