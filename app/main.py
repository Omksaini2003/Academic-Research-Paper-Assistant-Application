from fastapi import FastAPI
from app.agents.search_agent import SearchAgent
from app.agents.database_agent import DatabaseAgent
from app.agents.qa_agent import QAAgent
from app.agents.future_works_agent import FutureWorksAgent

app = FastAPI()

search_agent = SearchAgent()
database_agent = DatabaseAgent()
qa_agent = QAAgent()
future_works_agent = FutureWorksAgent()

@app.get("/search/")
async def search_papers(query: str):
    return await search_agent.search(query)

@app.get("/papers/")
async def list_papers():
    return await database_agent.get_papers()

@app.post("/qa/")
async def ask_question(question: str, paper_id: str):
    return await qa_agent.answer(question, paper_id)

@app.post("/future-works/")
async def generate_future_works(topic: str):
    return await future_works_agent.suggest(topic)
