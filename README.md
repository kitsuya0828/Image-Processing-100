# Image Processing 100 Questions



## Docker (Frontend + Backend)
```bash
docker-compose up
```
Then, visit the following url: http://localhost:3000

## Frontend
```bash
cd frontend
yarn install
yarn dev
```

## Backend
```bash
cd backend
python -m venv venv
. venv/bin/activate

pip install requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
