# 🚀 FastAPI CRUD Example Project

A simple FastAPI project demonstrating basic CRUD operations (Create, Read, Update, Delete) at the root endpoint `/`. Ideal for learning or testing small APIs quickly.

---

## 📦 Prerequisites

- Python 3.10+  
- pip (Python package manager)  
- Basic knowledge of Python  

Check Python version:

```bash
python --version
🔧 Installation
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
Activate it:

Windows:

bash
Copy code
venv\Scripts\activate
Linux/macOS:


bash
Copy code
source venv/bin/activate
Install FastAPI and Uvicorn:


bash
Copy code
pip install fastapi uvicorn
📝 Project Structure


fastapi_project/
├── main.py       ← FastAPI app

├── README.md

└── venv/         ← Optional virtual environment

⚡ Endpoints



Method	Endpoint	Description	Example Response

GET	/	Read a simple message	{"message": "Hello World"}

POST	/	Create a sample item	{"item_id": 1, "name": "Sample Item"}

PUT	/	Update a sample item	{"item_id": 1, "name": "Updated Item"}

DELETE	/	Delete a sample item	{"message": "Item with id 1 has been deleted"}


🚀 Run the Application
uvicorn main:app --reload
main → Python file name (main.py)

app → FastAPI instance

--reload → auto-reloads server on changes

Open in browser:

http://127.0.0.1:8000
Interactive docs:


http://127.0.0.1:8000/docs
📖 Test Endpoints
Browser → GET requests only

Postman / Insomnia / curl → All HTTP methods

⭐ Features
Simple FastAPI project

Demonstrates basic CRUD

Easy to extend for dynamic data or databases

⚠️ Notes
Currently uses fixed example items

Add a database (SQLite, PostgreSQL, MongoDB) for dynamic data

🧠 Tips
Use Pydantic models for request validation

Add path/query parameters for dynamic endpoints

Organize endpoints with routers for bigger projects

Add .gitignore to avoid committing venv/

🔗 Resources
FastAPI Docs → https://fastapi.tiangolo.com/

Uvicorn Docs → https://www.uvicorn.org/

UV Docs (Astral) → https://docs.astral.sh/uv/

Pydantic Docs → https://docs.pydantic.dev/
Happy FastAPI Coding! 🚀
