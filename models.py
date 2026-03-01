from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import List


@dataclass
class Product:
    name: str
    reference: str
    quantity: int
    price: float
    category: str

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, d):
        return cls(
            name=d["name"],
            reference=d["reference"],
            quantity=int(d["quantity"]),
            price=float(d["price"]),
            category=d["category"],
        )


@dataclass
class Sale:
    reference: str
    product_name: str
    quantity: int
    unit_price: float
    date: str
    category: str = ""

    @property
    def total(self):
        return self.quantity * self.unit_price

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, d):
        return cls(
            reference=d["reference"],
            product_name=d["product_name"],
            quantity=int(d["quantity"]),
            unit_price=float(d["unit_price"]),
            date=d["date"],
            category=d.get("category", ""),
        )


@dataclass
class Supplier:
    name: str
    contact: str
    products: List[str] = field(default_factory=list)

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, d):
        prods = d.get("products", [])
        if isinstance(prods, str):
            prods = [p.strip() for p in prods.split(",") if p.strip()]
        return cls(name=d["name"], contact=d["contact"], products=prods)
