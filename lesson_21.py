from dataclasses import dataclass

@dataclass
class Customer:
    name: str
    balance: int


jack = Customer('jack', 500)
print(jack)
