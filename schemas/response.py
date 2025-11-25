from pydantic import BaseModel
from typing import Any

class Response(BaseModel):
    status: str
    message: str
    data: Any = None

def success(message: str, payload=None):
    return Response(
            status="success",
            message=message,
            data=payload
        )

def fail(message: str):
    return Response(
            status="failed",
            message=message
        )

    