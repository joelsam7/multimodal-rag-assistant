class ChunkService:

    @staticmethod
    def chunk_pages(pages, chunk_size=500):

        chunks = []

        for page in pages:

            text = page["text"].strip()

            for i in range(0, len(text), chunk_size):

                chunks.append({
                    "text": text[i:i + chunk_size],
                    "page": page["page"]
                })

        return chunks


chunk_service = ChunkService()  