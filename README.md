# Image Processing 100 Questions

My solution to [ryoppippi/Gasyori100knock](https://github.com/ryoppippi/Gasyori100knock)

<img width="45%" alt="スクリーンショット 2023-01-18 11 16 54" src="https://user-images.githubusercontent.com/60843722/213067431-a7ec2f98-3122-484d-a445-081c02f64640.png"> <img width="45%" alt="スクリーンショット 2023-01-18 11 32 27" src="https://user-images.githubusercontent.com/60843722/213067771-343c74a3-64a7-4609-ae92-301af7f4f96d.png">



# Docker (Frontend + Backend)
[![Docker](https://skillicons.dev/icons?i=docker)](https://skillicons.dev)
```bash
docker-compose up
```
Then, visit the following url: http://localhost:3000

# Non-Docker
## Frontend
[![Frontend](https://skillicons.dev/icons?i=react,ts,next,)](https://skillicons.dev)
```bash
cd frontend
yarn install
yarn dev
```

## Backend
[![Backend](https://skillicons.dev/icons?i=python,fastapi)](https://skillicons.dev)
```bash
cd backend
python -m venv venv

# (Recommended) Switch Python version to 3.9.xx
pyenv install 3.9.13
pyenv local 3.9.13

# Mac
. venv/bin/activate

# Windows (Powershell)
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

> **コードレビューをしてくださる方へ**
>
> 単体でPythonプログラムの実行をしたい場合は、`/backend/`ディレクトリで上記の**Backend**の設定のうち、Fast APIサーバーを起動する`uvicorn ~`以外を行っていただきたいです。
>
> `/backend/routers/q1_10/q7.py`のようにファイル分けされているので、該当ディレクトリに移動して`python q7.py`のようにコマンドで実行できます。