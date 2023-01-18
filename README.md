# Image Processing 100 Questions

My solution to [ryoppippi/Gasyori100knock](https://github.com/ryoppippi/Gasyori100knock)

<img width="45%" alt="スクリーンショット 2023-01-18 11 16 54" src="https://user-images.githubusercontent.com/60843722/213067431-a7ec2f98-3122-484d-a445-081c02f64640.png"> <img width="45%" alt="スクリーンショット 2023-01-18 11 32 27" src="https://user-images.githubusercontent.com/60843722/213067771-343c74a3-64a7-4609-ae92-301af7f4f96d.png">



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
