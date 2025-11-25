from pydantic import BaseModel

class Transaction(BaseModel):
    amount: int
    description: str

class TransactionResponse(BaseModel):
    id: int
    amount: int
    description: str

    class Config:
        from_attributes = True