import axios from "axios";


const api = axios.create({

    baseURL: "http://127.0.0.1:8000",

});



// Upload PDF/DOCX/Image
export const uploadFile = (file) => {

    const formData = new FormData();

    formData.append(
        "file",
        file
    );


    return api.post(
        "/upload",
        formData
    );

};



// Ask RAG question
export const askQuestion = (question) => {

    return api.post(

        "/ask",

        {
            question: question
        }

    );

};



// Image chat
export const imageChat = (image, question) => {

    const formData = new FormData();


    formData.append(
        "file",
        image
    );


    formData.append(
        "question",
        question
    );


    return api.post(

        "/image-chat",

        formData

    );

};



// Get uploaded documents
export const getDocuments = () => {

    return api.get(
        "/documents"
    );

};

export const deleteDocument = (filename) => {

    return api.delete(
        `/documents/${filename}`
    );

};