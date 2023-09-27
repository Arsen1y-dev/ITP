# Задание 1.3* Генератор сказок


hero_name = input("Как зовут героя? ")
villain_name = input("Кто его противник? ")
kingdom_name = input("Название места действия? ")
conflict_reason = input("Причина конфликта? ")
hero_weapon = input("Оружие героя? ")
villain_ability = input("Способность злодея? ")
years = input("Сколько лет герою? ")


print(f"Жил-был в королевстве {kingdom_name} герой {hero_name}. Было ему {years} лет.")
print(f"Однажды на королевство напал злой {villain_name}.")
print(f"А произошло это из-за: {conflict_reason}.")
print(f"Герой {hero_name} вооружен {hero_weapon}, а злодей {villain_name} обладает ужасной способностью: {villain_ability}.")
print(f"День бились, другой бились, наконец {hero_name} одолел врага.")
print(f"Вернулся домой, а {hero_name} забыл {hero_weapon} в лесу.")
print(f"Тут и сказочке конец, а кто слушал — молодец!")
 