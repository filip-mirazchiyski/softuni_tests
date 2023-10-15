player_1 = input()
player_2 = input()

player_1_points = 0
player_2_points = 0

command = input()

while command != "End of game":
    command_2 = input()
    if int(command) > int(command_2):
        player_1_points += int(command) - int(command_2)
    elif int(command) < int(command_2):
        player_2_points += int(command_2) - int(command)
    elif command == command_2:
        print("Number wars!")
        card_again = int(input())
        card_again_2 = int(input())
        if card_again > card_again_2:
            print(f"{player_1} is winner with {player_1_points} points")
            break
        else:
            print(f"{player_2} is winner with {player_2_points} points")
            break
    command = input()

if command == "End of game":
    print(f"{player_1} has {player_1_points} points")
    print(f"{player_2} has {player_2_points} points")