import chromadb


class ChromaService:

    def __init__(self):
        self.client = chromadb.PersistentClient(path="chroma_db")

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

        self.image_collection = self.client.get_or_create_collection(
            name="images"
        )

    def add_document(self, filename, chunks, embeddings):

        ids = [f"{filename}_{i}" for i in range(len(chunks))]

        documents = [
            chunk["text"]
            for chunk in chunks
        ]

        metadatas = [
            {
                "source": filename,
                "page": chunk["page"]
            }
            for chunk in chunks
        ]

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def search_documents(self, query_embedding, n_results=3):

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )

        return results
    
    def list_documents(self):

        data = self.collection.get()

        filenames = sorted(
            set(
                metadata["source"]
                for metadata in data["metadatas"]
            )
        )

        return filenames
    
    def get_all_chunks(self):

        data = self.collection.get(
            include=["documents", "metadatas"]
        )

        return data

    def add_image(self, filename, image_path, embedding, description):

        self.image_collection.add(
            ids=[f"image_{filename}"],
            documents=[description],
            embeddings=[embedding],
            metadatas=[
                {
                    "source": filename,
                    "type": "image",
                    "path": image_path
                }
            ]
        )



    
chroma_service = ChromaService()