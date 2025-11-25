from schemas.transactions import Transaction, TransactionResponse
from schemas.response import success
from repositories.transaction_repo import TransactionRepository

transactions = {}
next_id=1

class TransactionService:

    @staticmethod
    async def create(db, payload: Transaction):
        trx = await TransactionRepository.create(db, payload)
        return success("OK",TransactionResponse.model_validate(trx))

    @staticmethod
    async def get_all(db):
        trx = await TransactionRepository.get_all(db)
        result = []
        for tx in trx:
            parse = TransactionResponse.model_validate(tx)
            result.append(parse)

        return success("OK", result)

    @staticmethod
    async def get_by_id(db, trx_id: int):
        return await TransactionRepository.get_by_id(db, trx_id)

    @staticmethod
    async def delete(db, trx_id: int):
        return await TransactionRepository.delete(db, trx_id)