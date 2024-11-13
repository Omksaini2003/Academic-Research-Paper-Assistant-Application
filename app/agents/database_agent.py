from app.services.neo4j_service import Neo4jService

class DatabaseAgent:
    def __init__(self):
        self.db_service = Neo4jService()
        
    async def get_papers(self):
        return self.db_service.get_all_papers()
