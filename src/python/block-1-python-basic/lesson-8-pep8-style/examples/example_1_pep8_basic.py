"""
Lesson 8: Example 1 — Основи PEP 8.

Демонстрація базових правил форматування коду.
"""

# === ПРАВИЛЬНЕ ФОРМАТУВАННЯ (PEP 8 Compliant) ===


def calculate_total(items, tax_rate=0.2):
    """
    Розрахувати загальну вартість з податком.

    Args:
        items: Список цін товарів
        tax_rate: Ставка податку (за замовчуванням 20%)

    Returns:
        Загальна вартість з податком
    """
    subtotal = sum(items)
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total


class ShoppingCart:
    """Кошик для покупок."""

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, item, price):
        """Додати товар в кошик."""
        self.items.append({"name": item, "price": price})

    def get_total(self):
        """Розрахувати загальну вартість."""
        prices = [item["price"] for item in self.items]
        return calculate_total(prices)


# === НЕПРАВИЛЬНЕ ФОРМАТУВАННЯ (Порушення PEP 8) ===


# ❌ Неправильна назва функції (PascalCase замість snake_case)
def CalculateTotal(items,tax_rate=0.2):
    subtotal=sum(items)  # ❌ Без пробілів навколо оператора
    tax=subtotal*tax_rate  # ❌ Без пробілів
    total=subtotal+tax;return total  # ❌ Дві інструкції в одному рядку


# ❌ Неправильна назва класу (snake_case замість PascalCase)
class shopping_cart:
    def __init__(self,customer_name):  # ❌ Без пробілу після коми
        self.customer_name=customer_name  # ❌ Без пробілів


# === ДЕМОНСТРАЦІЯ ===


if __name__ == "__main__":
    print("=" * 60)
    print("ПРИКЛАД ПРАВИЛЬНОГО ФОРМАТУВАННЯ")
    print("=" * 60)

    # Створення кошика
    cart = ShoppingCart("Alice")

    # Додавання товарів
    cart.add_item("Ноутбук", 15000)
    cart.add_item("Миша", 500)
    cart.add_item("Клавіатура", 1200)

    # Розрахунок
    total = cart.get_total()
    print(f"\nКлієнт: {cart.customer_name}")
    print(f"Товарів у кошику: {len(cart.items)}")
    print(f"Загальна вартість (з податком): {total:.2f} грн")

    print("\n" + "=" * 60)
    print("ПОРІВНЯННЯ СТИЛІВ")
    print("=" * 60)
    print("✅ Правильно: calculate_total(items, tax_rate=0.2)")
    print("❌ Неправильно: CalculateTotal(items,tax_rate=0.2)")
    print("\n✅ Правильно: x = y + 1")
    print("❌ Неправильно: x=y+1")

