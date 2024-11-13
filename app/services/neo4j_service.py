from neo4j import GraphDatabase

class Neo4jService:
    def __init__(self):
        self.driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
        
    def get_all_papers(self):
        with self.driver.session() as session:
            result = session.run("MATCH (p:Paper) RETURN p")
            return [record["p"] for record in result]
