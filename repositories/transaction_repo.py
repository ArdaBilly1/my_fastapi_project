from sqlalchemy.future import select
from models.transactions import Transaction

class TransactionRepository:

    @staticmethod
    async def create(db, payload):
        trx = Transaction(**payload.dict())
        db.add(trx)
        await db.commit()
        await db.refresh(trx)
        return trx

    @staticmethod
    async def get_all(db):
        result = await db.execute(select(Transaction))
        return result.scalars().all()

    @staticmethod
    async def get_by_id(db, trx_id: int):
        result = await db.execute(
            select(Transaction).where(Transaction.id == trx_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def delete(db, trx_id: int):
        trx = await TransactionRepository.get_by_id(db, trx_id)
        if trx:
            await db.delete(trx)
            await db.commit()
        return trx
