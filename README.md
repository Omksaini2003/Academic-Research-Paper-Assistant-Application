# Academic Research Paper Assistant Application

This repository contains the source code for the **Academic Research Paper Assistant Application**, which is designed to help researchers efficiently interact with academic papers. The application utilizes cutting-edge machine learning models, natural language processing techniques, and a graph-based database to extract valuable insights from academic papers, summarize findings, and provide suggestions for future research.

## Features

The application provides a set of advanced features to assist researchers in navigating academic literature:

1. **Answer Basic Questions About a Single Paper**  
   The system can answer specific questions regarding the content of a single academic paper. The model can retrieve and highlight relevant sections to provide accurate responses.

2. **Cross-Paper Question Answering**  
   The application can answer questions across multiple research papers on a given topic. It identifies relevant sections from each paper, providing detailed citations of where the information came from (which papers and which part of those papers).

3. **Summarize Findings from Multiple Papers**  
   You can input a set of research papers from a specific time period, and the application will generate a comprehensive summary of the collective findings, giving a concise overview of the state of research during that period.

4. **Key Information Extraction and Presentation**  
   The application can automatically extract and present key information from multiple academic papers in a coherent and easy-to-digest format, helping researchers quickly understand the essential points of each paper.

5. **Generate Ideas for Future Work**  
   Based on the content of research papers, the system can suggest possible areas for future research that are suitable for inclusion in a review paper. It helps researchers explore novel directions for further exploration.

6. **Create Well-Structured Review Paper**  
   The application can generate a structured review paper by summarizing key research contributions and offering insights into future research opportunities.

7. **Generate an Improvement Plan Based on Key Research Works**  
   The system helps create an improvement plan that outlines key research works and suggests areas for improvement. It identifies gaps in the current research and proposes directions for new contributions.

8. **Cohesive Improvement Plan from Multiple Papers**  
   The application can combine insights from multiple papers and generate a cohesive improvement plan, including suggestions for new research directions, advancements, and methodologies to address unresolved challenges.

## Technology Stack

This project leverages several modern technologies to provide its functionalities:

- **Python**: The primary programming language for the application.
- **Neo4j Database**: A graph-based database to store and query relationships between papers, citations, and key concepts.
- **Llama-7B LLM**: A large language model used for natural language understanding, processing, and generation of research insights and answers.
- **FastAPI**: A high-performance framework for building APIs that interface with the Llama-7B model and Neo4j database.
- **Streamlit**: A framework for creating interactive web applications for data science and machine learning, used to build the user interface for this application.

## Installation

Follow the steps below to get the project running locally:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Academic-Research-Paper-Assistant-Application.git
cd Academic-Research-Paper-Assistant-Application
```

## Setup Instructions

### 2. Set Up the Environment

Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows
```

### 3. Install Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt
```
Make sure you have Neo4j running locally or access to a remote Neo4j instance.

### 4. Configure the Neo4j Database
Edit the config.py file to include your Neo4j database connection settings (URL, username, password).

### 5. Run the Application
Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```
This will start the backend API on http://localhost:8051


Then, start the Streamlit app:

```bash
streamlit run frontend/app.py
```

This will open a local instance of the web application in your browser.

![User Interface Image](https://i.postimg.cc/vZ40csh5/front.png)

### Usage
Once the application is running, you can use the web interface to:

1. write topic research papers or query to add them into database.
2. Ask questions about specific papers or across multiple papers.
3. Summarize the collective findings from multiple papers.
4. Generate ideas for future research and create a structured review paper.
5. Explore suggestions for improving the current research landscape.



### Descriptions of Key Files/Directories:
- **`app/`**: Contains the backend logic of the application, including FastAPI routes, agents, services, and data models.
  - **`agents/`**: Various agents for specific tasks like search, QA, and future work generation.
  - **`services/`**: Services that interact with external systems such as the Neo4j database and Llama-7B model.
  - **`models/`**: Data models that define the structure for papers and responses.
- **`frontend/`**: Contains the user interface built with Streamlit.
- **`config/`**: Configuration files (such as YAML) used to set up paths and service parameters.
- **`requirements.txt`**: A list of Python libraries required to run the application.
- **`README.md`**: The documentation file you’re reading.
- **`.env`**: Environment variables file used for sensitive configuration (e.g., database credentials).

This structure helps keep the application organized by separating concerns between agents, services, and models, as well as the frontend and configuration files.


