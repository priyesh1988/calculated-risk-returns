# calculated-risk-returns

End‑to‑end deployment with:
Postgres, Kafka, Celery-ready workers, async execution, Alpaca adapter-ready, Grafana, Helm, CI/CD, zero‑trust auth ready.

## Run (Full Stack)
cd infra
docker compose up --build

Frontend: http://localhost:3000
Backend: http://localhost:8000  
Grafana: http://localhost:3001  

## Dashboards

Low Risk Dashboard  
GET /dashboard/low

Medium Risk Dashboard  
GET /dashboard/medium

Extreme Risk Dashboard  
GET /dashboard/extreme

<img width="1120" height="540" alt="Screenshot 2026-02-20 at 12 48 46" src="https://github.com/user-attachments/assets/a42e40c1-e35d-4978-92ec-7ad9dae69cdd" />
