import requests

class LocalLLMBackend:
    def __init__(self, base_url="http://localhost:11434", model="deepseek-r1:1.5b"):
        self.base_url = base_url
        self.model = model

    def answer(self, prompt):
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json()["response"]

