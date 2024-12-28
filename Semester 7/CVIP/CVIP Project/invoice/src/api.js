import axios from "axios";

const BASE_URL = "http://127.0.0.1:5000"; // Backend URL

export const uploadFile = async (file) => {
    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await axios.post(`${BASE_URL}/upload`, formData, {
            headers: { "Content-Type": "multipart/form-data" },
        });
        return response.data;
    } catch (error) {
        console.error("Error uploading file:", error);
        throw error;
    }
};
