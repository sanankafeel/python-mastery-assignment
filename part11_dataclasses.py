# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
# Part 11 - Type hints and dataclasses
# Warm-up: type hints were added to part05_functions.py.
#          Check with:  pip install mypy   then   mypy part05_functions.py

import json
from dataclasses import asdict, dataclass, field

PRODUCTS_FILE = "products.json"


# order=True makes Python compare products field by field, in order.
# price is the FIRST field, so sorting compares by price first.
@dataclass(order=True)
class Product:
    price: float
    name: str = field(compare=False)
    stock: int = field(default=0, compare=False)
    tags: list[str] = field(default_factory=list, compare=False)  # new list per object

    def __post_init__(self) -> None:
        # runs automatically right after the generated __init__
        if self.price < 0:
            raise ValueError(f"{self.name}: price cannot be negative")
        if self.stock < 0:
            raise ValueError(f"{self.name}: stock cannot be negative")


def save_products(products: list[Product], path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump([asdict(p) for p in products], f, indent=2)


def load_products(path: str) -> list[Product]:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return [Product(**d) for d in data]   # ** unpacks the dict into keyword arguments


def main() -> None:
    products = [
        Product(name="Notebook", price=150, stock=40, tags=["stationery"]),
        Product(name="Calculator", price=2200, stock=0, tags=["electronics", "exam"]),
        Product(name="Geometry box", price=650, stock=12),
        Product(name="USB drive", price=1200, stock=0, tags=["electronics"]),
        Product(name="Pen pack", price=300, stock=25, tags=["stationery"]),
    ]

    print("--- Build: out of stock ---")
    for p in products:
        if p.stock == 0:
            print(" ", p.name)

    try:
        Product(name="Broken", price=-10, stock=5)
    except ValueError as e:
        print("Validation works:", e)

    print("\n--- Challenge: save, load, sort ---")
    save_products(products, PRODUCTS_FILE)
    loaded = load_products(PRODUCTS_FILE)
    # Compare with asdict(): because of compare=False, == on Product objects
    # only checks price, which would hide a wrong name or stock.
    same = [asdict(p) for p in loaded] == [asdict(p) for p in products]
    print(f"Loaded {len(loaded)} products back. Same as saved? {same}")
    for p in sorted(loaded):
        print(f"  Rs {p.price:>7.2f}  {p.name}")


if __name__ == "__main__":
    main()
