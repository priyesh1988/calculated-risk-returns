# calculated-risk-returns

End‑to‑end deployment with:
Postgres, Kafka, Celery-ready workers, async execution, Alpaca adapter-ready, Grafana, Helm, CI/CD, zero‑trust auth ready.

## Run (Full Stack)

add infra/.env

insert
ALPACA_KEY="<ALPACA_KEY>"
ALPACA_SECRET="<ALPACA_SECRET>"

cd infra \
docker compose up --build


Frontend: http://localhost:3000   
Backend: http://localhost:8000  
Grafana: http://localhost:3001  

## Endpoints

Low Risk Dashboard  
GET /dashboard/low

Medium Risk Dashboard  
GET /dashboard/medium

Extreme Risk Dashboard  
GET /dashboard/extreme 

## Dashboard

<img width="1648" height="502" alt="Screenshot 2026-02-20 at 12 48 04" src="https://github.com/user-attachments/assets/2f7ffdab-f13b-4639-8940-4699961e5476" />

\
🔎 What Each Field Means

1️⃣ "tier": "low" \
You’re using the Low Risk policy. \
That means: Max 5% capital per position 

2️⃣ "max_position_pct": 0.05" \
This means: Each position can use at most 5% of total portfolio capital. \
If your portfolio = $1,000 \
Max per position = $50 \
That’s your exposure cap. 

3️⃣ "VaR": 0.017950 \
This is Value at Risk (95%). \
Interpreted as: There is a 5% chance of losing ~1.7% or more in one day. \
If portfolio = $1,000 \
Possible 1-day loss at 95% confidence ≈ $17


4️⃣ "ES_95": 0.02155 → 2.15% \
Expected Shortfall (Conditional VaR) \
Interpretation: \
If markets fall into that worst 5% scenario, the average loss is ~2.15%. \
If portfolio = $1000 \
Tail-event average loss ≈ $21 \
If markets fall badly, this is the average loss you can expect on those worst days.
