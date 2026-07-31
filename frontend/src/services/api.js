import axios from "axios";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000",
});

export const uploadFile = (file) => {
    const formData = new FormData();
    formData.append("file", file);

    return api.post("/upload", formData);
};


export const askQuestion = (question) => {
    return api.post("/ask", {
        question
    });
};


export const imageChat = (image, question) => {
    const formData = new FormData();

    formData.append("file", image);
    formData.append("question", question);

    return api.post("/image-chat", formData);
};


export const getDocuments = () => {
    return api.get("/documents");
};