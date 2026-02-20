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

<img width="1648" height="502" alt="Screenshot 2026-02-20 at 12 48 04" src="https://github.com/user-attachments/assets/2f7ffdab-f13b-4639-8940-4699961e5476" />

🔎 What Each Field Means

1️⃣ "tier": "low"
You’re using the Low Risk policy.
That means:
Max 5% capital per position
Tight risk limits
Lower volatility exposure

2️⃣ "max_position_pct": 0.05
This means:
Each position can use at most 5% of total portfolio capital
If your portfolio = $100,000
Max per position = $5,000
That’s your exposure cap.

3️⃣ "VaR": 0.027989
This is Value at Risk (95%)
Interpreted as:
There is a 5% chance of losing ~2.8% or more in one day (based on the simulated returns).
If portfolio = $100,000
Possible 1-day loss at 95% confidence ≈ $2,800
