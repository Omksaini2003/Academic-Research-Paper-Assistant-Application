from app.services.llama_service import LlamaService

class FutureWorksAgent:
    def __init__(self):
        self.llm = LlamaService()
        
    async def suggest(self, topic: str):
        return self.llm.generate_future_works(topic)
