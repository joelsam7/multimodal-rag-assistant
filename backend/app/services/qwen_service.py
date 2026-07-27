from ollama import chat


class QwenService:

    def generate_response(self, prompt):

        response = chat(
            model="qwen2.5:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    def analyze_image(self, image_path, question):

        response = chat(
            model="qwen2.5vl:3b",
            messages=[
                {
                    "role": "user",
                    "content": question,
                    "images": [image_path]
                }
            ]
        )

        return response["message"]["content"]


qwen_service = QwenService()