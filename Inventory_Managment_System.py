# inventory_system.py
# Prosty system zarządzania magazynem i raportowaniem sprzedaży

# Słownik przechowujący wszystkie produkty w magazynie.
# Kluczem jest nazwa produktu, a wartością jest słownik z ceną i ilością w magazynie.
inventory = {}


def add_item(item, price, stock):
    """
    Dodaje nowy produkt do magazynu.
    :param item: nazwa produktu (string)
    :param price: cena produktu (liczba)
    :param stock: ilość sztuk w magazynie (liczba całkowita)
    """
    if item in inventory:
        print(f"Error: Item '{item}' already exists.")  # produkt już istnieje
        return
    try:
        # Konwersja na odpowiednie typy danych
        inventory[item] = {"price": float(price), "stock": int(stock)}
        print(f"Item '{item}' added successfully.")  # komunikat sukcesu
    except ValueError:
        # Obsługa błędu, jeśli podane dane nie są liczbami
        print("Error: Price and stock must be numeric.")


def update_stock(item, quantity):
    """
    Aktualizuje ilość danego produktu w magazynie.
    :param item: nazwa produktu
    :param quantity: zmiana ilości (może być dodatnia lub ujemna)
    """
    if item not in inventory:
        print(f"Error: Item '{item}' not found.")  # produkt nie istnieje
        return
    try:
        new_stock = inventory[item]["stock"] + int(quantity)
        if new_stock < 0:
            # Nie można mieć ujemnego stanu magazynowego
            print(f"Error: Insufficient stock for '{item}'.")
        else:
            inventory[item]["stock"] = new_stock
            print(f"Stock for '{item}' updated successfully.")  # sukces
    except ValueError:
        print("Error: Quantity must be an integer.")  # błąd konwersji liczby


def check_availability(item):
    """
    Sprawdza dostępność produktu w magazynie.
    :param item: nazwa produktu
    :return: ilość sztuk w magazynie lub komunikat o braku
    """
    if item not in inventory:
        return "Item not found"  # brak produktu
    return inventory[item]["stock"]


def sales_report(sales):
    """
    Generuje raport sprzedaży i aktualizuje stany magazynowe.
    :param sales: słownik {produkt: ilość sprzedana}
    :return: string z całkowitym przychodem
    """
    total_revenue = 0
    for item, quantity in sales.items():
        if item not in inventory:
            print(f"Error: Item '{item}' not found.")  # brak produktu w magazynie
            continue
        if inventory[item]["stock"] < quantity:
            print(f"Error: Insufficient stock for '{item}'.")  # brak wystarczającej ilości
            continue
        # Aktualizacja stanu magazynowego
        inventory[item]["stock"] -= quantity
        # Dodanie przychodu
        total_revenue += quantity * inventory[item]["price"]
    return f"Total revenue: ${total_revenue:.2f}"


# Przykładowe użycie modułu:
if __name__ == "__main__":
    add_item("Apple", 0.5, 50)
    add_item("Banana", 0.2, 60)
    sales = {"Apple": 30, "Banana": 20, "Orange": 10}  # Orange powinien zgłosić błąd
    print(sales_report(sales))  # Oczekiwany wynik: 19.0
    print(inventory)
