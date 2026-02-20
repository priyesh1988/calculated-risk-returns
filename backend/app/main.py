from fastapi import FastAPI
import pandas as pd, numpy as np
from scipy.stats import norm

app = FastAPI(title="calculated-risk-returns")

POLICIES = {"low":0.05,"medium":0.10,"extreme":0.20}

def var_es(r):
    m, s = r.mean(), r.std()
    z = norm.ppf(0.05)
    return float(-(m+z*s)), float(-(m - s*norm.pdf(z)/0.95))

@app.get("/health")
def health():
    return {"status":"ok"}

@app.get("/dashboard/{tier}")
def dashboard(tier:str):
    returns = pd.Series(np.random.normal(0.001,0.02,252))
    var, es = var_es(returns)
    return {
        "tier": tier,
        "max_position_pct": POLICIES[tier],
        "VaR": var,
        "ES": es
    }
