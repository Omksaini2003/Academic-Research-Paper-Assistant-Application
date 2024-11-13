from app.services.llama_service import LlamaService

class QAAgent:
    def __init__(self):
        self.llm = LlamaService()
        
    async def answer(self, question: str, paper_id: str):
        # Simulating context retrieval from the database for the paper
        context = f"Content of the paper with ID: {paper_id}."
        return self.llm.generate_answer(question, context)
