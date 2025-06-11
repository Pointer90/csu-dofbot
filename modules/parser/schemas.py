from pydantic import BaseModel


class BaseDTO(BaseModel):
    target: None | str = None
    cmd: str
    args: list = []
