# Student ML API

A small FastAPI service used to demonstrate an MLOps workflow.

## Endpoints

- `GET /health` — service status, application name, and version.
- `POST /predict` — body: `{"value": number}` → `{"input": number, "prediction": number}`.

## Local development

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

## Tests

```bash
pytest
```

## Docker

```bash
docker build -t student-ml-api .
docker run -p 5000:5000 student-ml-api
```
