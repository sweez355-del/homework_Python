from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "A56", "+79261234567"),
    Smartphone("Apple", "iPhone 17 Pro Max", "+79161234567"),
    Smartphone("OnePlus", "9RT", "+79031234567"),
    Smartphone("Oppo", "Reno 15", "+79011234567"),
    Smartphone("Xiaomi", "17 Ultra", "+79051234567")]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
