import requests

import aiohttp
import xml.etree.ElementTree as ET

class SearchAgent:
    def __init__(self):
        self.api_url = "http://export.arxiv.org/api/query"

    async def search(self, query: str, max_results: int = 10):
        """
        Search for academic papers using the arXiv API.
        
        Parameters:
            query (str): The search query (e.g., "machine learning").
            max_results (int): Maximum number of papers to retrieve.
        
        Returns:
            dict: A dictionary containing the search query and a list of relevant papers.
        """
        params = {
            "search_query": query,
            "start": 0,
            "max_results": max_results
        } 

        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url, params=params) as response:
                print(response)
                if response.status == 200:
                    data = await response.text()
                    papers = self._parse_arxiv_response(data)
                    return {"query": query, "papers": papers}
                else:
                    print(response.text)
                    return {"error": f"Failed to fetch papers, status code: {response.status}"}

    def _parse_arxiv_response(self, xml_data: str):
        """
        Parse the XML response from the arXiv API.
        
        Parameters:
            xml_data (str): XML response from the arXiv API.
        
        Returns:
            list[dict]: List of papers with relevant details.
        """
        root = ET.fromstring(xml_data)
        papers = []
        for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
            paper = {
                "title": entry.find("{http://www.w3.org/2005/Atom}title").text.strip(),
                "authors": [author.find("{http://www.w3.org/2005/Atom}name").text for author in entry.findall("{http://www.w3.org/2005/Atom}author")],
                "summary": entry.find("{http://www.w3.org/2005/Atom}summary").text.strip(),
                "published": entry.find("{http://www.w3.org/2005/Atom}published").text,
                "link": entry.find("{http://www.w3.org/2005/Atom}id").text
            }
            papers.append(paper)
        return papers


# class SearchAgent:
#     def __init__(self):
#         self.api_url = "https://api.semanticscholar.org/v1/paper"
        
#     async def search(self, query: str):
#         # Simulate a search process
#         return {"query": query, "papers": ["paper1", "paper2"]}
