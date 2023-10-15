championship_round = input()
ticket_type = input()
ticket_count = int(input())
trophy_photo = input()

total_ticket_price = 0
total_photo_price = 40 * ticket_count

if championship_round == "Quarter final":
    if ticket_type == "Standard":
        total_ticket_price += 55.50 * ticket_count
    elif ticket_type == "Premium":
        total_ticket_price += 105.20 * ticket_count
    elif ticket_type == "VIP":
        total_ticket_price += 118.90 * ticket_count

elif championship_round == "Semi final":
    if ticket_type == "Standard":
        total_ticket_price += 75.88 * ticket_count
    elif ticket_type == "Premium":
        total_ticket_price += 125.22 * ticket_count
    elif ticket_type == "VIP":
        total_ticket_price += 300.40 * ticket_count

elif championship_round == "Final":
    if ticket_type == "Standard":
        total_ticket_price += 110.10 * ticket_count
    elif ticket_type == "Premium":
        total_ticket_price += 160.66 * ticket_count
    elif ticket_type == "VIP":
        total_ticket_price += 400 * ticket_count

if total_ticket_price > 2500 and total_ticket_price < 4000:
    total_ticket_price *= 0.9
    if trophy_photo == "Y":
        total_ticket_price += total_photo_price
if total_ticket_price > 4000:
    total_ticket_price *= 0.75

print(f"{total_ticket_price:.2f}")