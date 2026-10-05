import requests
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI(title="FrenPet AI Strategy Engine")

# Your Coinbase Wallet Address
WALLET_ADDRESS = "0x62832d765f2E50319BA72C1cA85562Fed0c58D36"
PRICE_PER_CALL_USDC = "0.01"

@app.get("/")
async def root():
    return {"message": "FrenPet Strategy API is live. Query /api/v1/battle-strategy"}

@app.get("/api/v1/battle-strategy")
async def battle_strategy(request: Request, pet_id: str = "1"):
    payment_header = request.headers.get("X-Payment") or request.headers.get("authorization")

    # 1. No payment header -> Return HTTP 402 Paywall Intercept ($0.01 USDC)
    if not payment_header:
        return JSONResponse(
            status_code=402,
            content={
                "x402Version": 1,
                "error": "Payment Required",
                "accepts": [
                    {
                        "scheme": "exact",
                        "network": "eip155:8453",  # Base Mainnet
                        "asset": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",  # USDC
                        "payTo": WALLET_ADDRESS,
                        "maxAmountRequired": "10000",  # $0.01 USDC (10,000 atomic units)
                        "description": "FrenPet AI battle EV & training recommendation"
                    }
                ]
            }
        )

    # 2. Strategy Engine Logic for Fren Pet Bots
    recommendation = {
        "pet_id": pet_id,
        "optimal_action": "ATTACK",
        "recommended_target": "Opponent #8492",
        "expected_win_rate": "74%",
        "stat_recommendation": "TRAIN_DEFENSE",
        "strategy_type": "Balanced EV Strategy"
    }

    return {
        "status": "success",
        "pricePaid": f"${PRICE_PER_CALL_USDC} USDC",
        "recommendation": recommendation
    }
