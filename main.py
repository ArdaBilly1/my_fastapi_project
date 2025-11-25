from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from schemas.response import Response, success, fail
from services.transaction_svc import TransactionService
from schemas.transactions import Transaction
from db.database import engine, get_db
from models.transactions import Base

async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def health_check():
    return Response(
        message="OK"
    )

@app.post("/transactions", response_model=Response)
async def create_transaction(payload: Transaction, db = Depends(get_db)):
    return await TransactionService.create(db, payload)

@app.get("/transactions", response_model=Response)
async def get_all_transaction(db = Depends(get_db)):
    return await TransactionService.get_all(db)

@app.get("/transactions/{trx_id}")
async def get_transaction_by_id(trx_id: str,db = Depends(get_db)):
    return await TransactionService.get_by_id(db, trx_id)

@app.delete("/transactions/{trx_id}")
async def delete(trx_id:str, db = Depends(get_db)):
    return await TransactionService.delete(db, trx_id)

