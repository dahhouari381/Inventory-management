from sqlmodel import SQLModel, Field

class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    sku: str = Field(unique=True)
    cost_price: int 
    purchase_price:int

class UpdateProduct(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    name: str | None
    sku: str | None
    cost_price: int | None
    purchase_price:int | None