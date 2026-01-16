# Docker Containerization - Next.js & FastAPI

This repository contains Dockerized applications for both Next.js (frontend) and FastAPI (backend), demonstrating containerization best practices and multi-container deployment.

## 📁 Repository Structure

```
Docker_Containerization/
├── nextjs-docker/          # Next.js frontend application
│   ├── Dockerfile
│   ├── package.json
│   └── ...
├── fastapi-docker/         # FastAPI backend application
│   ├── Dockerfile
│   ├── requirements.txt
│   └── ...
└── README.md
```

## 🚀 Projects Overview

### 1. Next.js Docker Application
A modern React-based frontend framework containerized with Docker for optimal performance and deployment.

**Tech Stack:**
- Next.js
- React
- Node.js
- Docker

### 2. FastAPI Docker Application
A high-performance Python web framework for building APIs, fully containerized and ready for production.

**Tech Stack:**
- FastAPI
- Python
- Uvicorn
- Docker

## 🐳 Docker Setup

### Prerequisites
- Docker Desktop installed on your machine
- Docker Compose (optional, for multi-container orchestration)

### Building Docker Images

#### Next.js Application
```bash
cd nextjs-docker
docker build -t nextjs-app .
```

#### FastAPI Application
```bash
cd fastapi-docker
docker build -t fastapi-app .
```

### Running Containers

#### Next.js Container
```bash
docker run -d -p 3000:3000 --name nextjs-container nextjs-app
```

#### FastAPI Container
```bash
docker run -d -p 8000:8000 --name fastapi-container fastapi-app
```

### Access Applications
- **Next.js Frontend:** http://localhost:3000
- **FastAPI Backend:** http://localhost:8000
- **FastAPI Docs:** http://localhost:8000/docs

## 📸 Screenshots

### Docker Desktop - Images
Both Next.js and FastAPI Docker images successfully built and available in Docker Desktop.

![Docker Images](./images/docker-images.png)

### Docker Desktop - Running Containers
Both containers running simultaneously, demonstrating successful containerization.

![Docker Containers](./images/docker-containers.png)

## 🛠️ Development Workflow

### Next.js Development
1. Navigate to `nextjs-docker` directory
2. Install dependencies: `npm install`
3. Run locally: `npm run dev`
4. Build Docker image: `docker build -t nextjs-app .`
5. Run container: `docker run -p 3000:3000 nextjs-app`

### FastAPI Development
1. Navigate to `fastapi-docker` directory
2. Create virtual environment: `python -m venv venv`
3. Activate environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run locally: `uvicorn main:app --reload`
6. Build Docker image: `docker build -t fastapi-app .`
7. Run container: `docker run -p 8000:8000 fastapi-app`

## 🔧 Docker Commands Reference

### Image Management
```bash
# List all images
docker images

# Remove an image
docker rmi <image-name>

# Build image with tag
docker build -t <image-name>:<tag> .
```

### Container Management
```bash
# List running containers
docker ps

# List all containers
docker ps -a

# Stop a container
docker stop <container-name>

# Remove a container
docker rm <container-name>

# View container logs
docker logs <container-name>
```

## 📦 Docker Compose (Optional)

For running both containers together, create a `docker-compose.yml`:

```yaml
version: '3.8'

services:
  nextjs:
    build: ./nextjs-docker
    ports:
      - "3000:3000"
    container_name: nextjs-container
    
  fastapi:
    build: ./fastapi-docker
    ports:
      - "8000:8000"
    container_name: fastapi-container
```

Run with:
```bash
docker-compose up -d
```

## 🎯 Features

- ✅ Fully containerized applications
- ✅ Production-ready Docker images
- ✅ Optimized image sizes
- ✅ Environment variable support
- ✅ Easy deployment and scaling
- ✅ Isolated development environments

## 📝 Notes

- Make sure ports 3000 and 8000 are available on your machine
- Docker Desktop must be running before executing Docker commands
- Images are optimized for production use
- Both applications can run independently or together

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Built with ❤️ using Docker, Next.js, and FastAPI

---

**Happy Containerizing! 🐳**
