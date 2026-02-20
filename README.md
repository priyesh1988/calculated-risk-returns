# calculated-risk-returns

End‑to‑end deployment with:
Postgres, Kafka, Celery-ready workers, async execution, Alpaca adapter-ready, Grafana, Helm, CI/CD, zero‑trust auth ready.

## Run (Full Stack)
cd infra
docker compose up --build

Frontend: http://localhost:3000

Backend: http://localhost:8000  
Frontend: http://localhost:3000 Grafana: http://localhost:3001  
Backend: http://localhost:8000  
Grafana: http://localhost:3001  

## Dashboards

Low Risk Dashboard  
GET /dashboard/low

Medium Risk Dashboard  
GET /dashboard/medium

Extreme Risk Dashboard  
GET /dashboard/extreme

<img width="1648" height="502" alt="Screenshot 2026-02-20 at 12 48 04" src="https://github.com/user-attachments/assets/2f7ffdab-f13b-4639-8940-4699961e5476" />
