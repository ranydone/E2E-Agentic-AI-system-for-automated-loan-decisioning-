from fastapi import FastAPI
from agent.loan_agent import LoanAgent

app = FastAPI(title="Agentic Loan Origination System")
agent = LoanAgent()

@app.post("/loan/decision")
def loan_decision(application: dict):
    return agent.decide(application)
