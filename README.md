# 🏠 House Price Prediction API (MLOps Deployment)

An end-to-end Machine Learning web service that predicts house prices based on square meters. This project demonstrates the complete MLOps lifecycle: training a linear regression model, building a RESTful API with FastAPI, containerizing the application with Docker, and deploying it to a live Debian Linux server using Nginx Proxy Manager.

## 🚀 Live Demo
You can test the live API and explore the interactive Swagger documentation here:
👉 **[Live Swagger UI: ai.mehmetkiyik.com.tr/docs](https://ai.mehmetkiyik.com.tr/docs)**

*(Example API Request: `https://ai.mehmetkiyik.com.tr/tahmin?metrekare=150`)*

## 🛠️ Tech Stack
* **Machine Learning:** Python, Scikit-learn, Pandas
* **Web Framework:** FastAPI, Uvicorn
* **Containerization & Deployment:** Docker, Docker Compose
* **Reverse Proxy:** Nginx Proxy Manager (NPM)
* **OS:** Debian Linux

## 📂 Project Structure
- `ev_tahmini.py`: Contains the ML model training logic and FastAPI endpoints.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Instructions to build the lightweight Python 3.11 container.
- `docker-compose.yml`: Services configuration for seamless deployment in the server network.

## 🔌 API Endpoints
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/docs` | Opens the interactive Swagger UI documentation. |
| `GET` | `/tahmin?metrekare={value}` | Returns the predicted house price in JSON format based on the given square meters. |

## 💻 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git)
   cd YOUR_REPOSITORY_NAME

Run with Docker Compose:

Bash
docker compose up -d --build
Access the API:
Open your browser and navigate to http://localhost:8000/docs.

Developed by Mehmet Kıyık.


   
