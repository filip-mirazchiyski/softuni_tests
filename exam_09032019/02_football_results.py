first_match_result = input()
second_match_result = input()
third_match_result = input()

matches_won = 0
matches_lost = 0
matches_draw = 0

if int(first_match_result[0]) > int(first_match_result[2]):
    matches_won += 1
elif int(first_match_result[0]) < int(first_match_result[2]):
    matches_lost += 1
else:
    matches_draw += 1

if int(second_match_result[0]) > int(second_match_result[2]):
    matches_won += 1
elif int(second_match_result[0]) < int(second_match_result[2]):
    matches_lost += 1
else:
    matches_draw += 1

if int(third_match_result[0]) > int(third_match_result[2]):
    matches_won += 1
elif int(third_match_result[0]) < int(third_match_result[2]):
    matches_lost += 1
else:
    matches_draw += 1

print(f"Team won {matches_won} games.")
print(f"Team lost {matches_lost} games.")
print(f"Drawn games: {matches_draw}")
