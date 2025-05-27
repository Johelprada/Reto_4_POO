class MenuItem:
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str):
        self._name = name

    def get_price(self) -> float:
        return self._price

    def set_price(self, price: float):
        self._price = price

    def calculate_total_price(self, has_main_course: bool = False) -> float:
        return self._price


# BEBIDAS
class Cafe(MenuItem):
    def __init__(self):
        super().__init__("Café", 2.0)

    def calculate_total_price(self, has_main_course: bool = False) -> float:
        return self.get_price() * 0.9 if has_main_course else self.get_price()


class Agua(MenuItem):
    def __init__(self):
        super().__init__("Agua", 1.0)

    def calculate_total_price(self, has_main_course: bool = False) -> float:
        return self.get_price() * 0.9 if has_main_course else self.get_price()


class CocaCola(MenuItem):
    def __init__(self):
        super().__init__("Coca Cola", 1.5)

    def calculate_total_price(self, has_main_course: bool = False) -> float:
        return self.get_price() * 0.9 if has_main_course else self.get_price()


# POSTRES Y PLATOS
class Postre(MenuItem):
    def __init__(self):
        super().__init__("Pastel de Chocolate", 4.5)


class Nachos(MenuItem):
    def __init__(self):
        super().__init__("Nachos", 3.5)


class Ensalada(MenuItem):
    def __init__(self):
        super().__init__("Ensalada César", 4.0)


class Hamburguesa(MenuItem):
    def __init__(self):
        super().__init__("Hamburguesa", 7.5)


class Pizza(MenuItem):
    def __init__(self):
        super().__init__("Pizza", 9.0)


class TacosVegetarianos(MenuItem):
    def __init__(self):
        super().__init__("Tacos Vegetarianos", 6.5)


class Lasaña(MenuItem):
    def __init__(self):
        super().__init__("Lasaña", 8.0)


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def contains_main_course(self) -> bool:
        main_courses = (
            "Hamburguesa", "Pizza", "Tacos Vegetarianos", "Lasaña", "Ensalada César"
        )
        return any(item.get_name() in main_courses for item in self.items)

    def count_beverages(self) -> int:
        bebidas = ("Café", "Agua", "Coca Cola")
        return sum(1 for item in self.items if item.get_name() in bebidas)

    def calculate_total(self) -> float:
        has_main = self.contains_main_course()
        return sum(item.calculate_total_price(has_main) for item in self.items)

    def apply_discount(self) -> float:
        subtotal = self.calculate_total()
        item_count = len(self.items)
        beverage_count = self.count_beverages()

        # Descuento base por cantidad de ítems
        if item_count > 10:
            total = subtotal * 0.8  # 20%
        elif item_count >= 5:
            total = subtotal * 0.9  # 10%
        else:
            total = subtotal

        # Descuento acumulable por bebidas
        if beverage_count > 3:
            total *= 0.95  # 5% adicional

        return total

    def show_order_summary(self):
        print("Resumen del pedido:")
        for item in self.items:
            print(f"- {item.get_name()} (${item.get_price():.2f})")
        print(f"Subtotal (con descuentos individuales): ${self.calculate_total():.2f}")
        print(f"Total con descuentos aplicados: ${self.apply_discount():.2f}")


class Payment:
    def __init__(self, order: Order, method: str):
        self.order = order
        self.method = method  # e.g., "efectivo", "tarjeta", "paypal"

    def process_payment(self):
        total = self.order.apply_discount()
        print(f"\n pago de ${total:.2f} mediante {self.method.capitalize()}")


def main():
    orden = Order()

    # Puedes modificar aquí para probar los descuentos
    orden.add_item(Cafe())
    orden.add_item(CocaCola())
    orden.add_item(Agua())
    orden.add_item(Cafe())
    orden.add_item(Postre())
    orden.add_item(Hamburguesa())
    orden.add_item(Pizza())
    orden.add_item(TacosVegetarianos())
    orden.add_item(Ensalada())
    orden.add_item(Lasaña())
    orden.add_item(Nachos())

    orden.show_order_summary()

    pago = Payment(orden, "tarjeta")
    pago.process_payment()


if __name__ == "__main__":
    main()
