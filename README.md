# calculated-risk-returns

End‑to‑end deployment with:
Postgres, Kafka, Celery-ready workers, async execution, Alpaca adapter-ready, Grafana, Helm, CI/CD, zero‑trust auth ready.

## Run (Full Stack)
cd infra
docker compose up --build

Backend: http://localhost:8000  
Grafana: http://localhost:3001  

## Dashboards

Low Risk Dashboard  
GET /dashboard/low

Medium Risk Dashboard  
GET /dashboard/medium

Extreme Risk Dashboard  
GET /dashboard/extreme
