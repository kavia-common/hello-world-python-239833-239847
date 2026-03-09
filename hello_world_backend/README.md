# hello_world_backend

Minimal FastAPI backend exposing a single Hello World endpoint.

## Endpoints

- `GET /hello` → `Hello, World!` (plain text)

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 3001
```

Then visit:

- http://localhost:3001/hello
