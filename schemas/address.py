from pydantic import BaseModel


class cepSchema(BaseModel):
    cep: str = "22430090"