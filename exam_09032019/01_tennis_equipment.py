from math import ceil

tennis_rocket_price = float(input())
tennis_rocket_count = int(input())
sneakers_count = int(input())

sneakers_price = tennis_rocket_price / 6

total_tennis_rocket_price = tennis_rocket_count * tennis_rocket_price
total_sneakers_price = sneakers_count * sneakers_price
total_additional_price = (total_tennis_rocket_price + total_sneakers_price) * 0.2

total_price = total_tennis_rocket_price + total_sneakers_price + total_additional_price
djokovic_price = int(total_price / 8)
sponsors_price = total_price / 8 * 7

print(f"Price to be paid by Djokovic {djokovic_price}")
print(f"Price to be paid by sponsors {ceil(sponsors_price)}")
