from sqlmodel import SQLModel, Field

class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    decription : str

class UpdateProduct(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    name: str | None = None
    decription : str | None = None