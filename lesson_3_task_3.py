from address import Address
from mailing import Mailing


to_address = Address(
    "123456", "Москва", "Александра Солженицына", "23Ас1", "56")
from_address = Address(
    "654321", "Жуковский", "Гудкова", "20", "46")


mailing = Mailing(to_address, from_address, 1000, "01234567QAZ")
print(
    f"Отправление {mailing.track} из {mailing.from_address} "
    f"в {mailing.to_address}. Стоимость {mailing.cost} рублей.")
