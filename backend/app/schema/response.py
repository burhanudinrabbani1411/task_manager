from typing import Any

from pydantic import BaseModel


class SuccessResponse(BaseModel):
    success: bool
    message: str
    data: Any
