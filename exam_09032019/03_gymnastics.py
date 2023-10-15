country = input()
tool = input()

difficulty_mark = 0
execution_mark = 0
total_mark = difficulty_mark + execution_mark
max_mark = 20

if country == "Russia":
    if tool == "ribbon":
        difficulty_mark = 9.100
        execution_mark = 9.400
    elif tool == "hoop":
        difficulty_mark = 9.300
        execution_mark = 9.800
    elif tool == "rope":
        difficulty_mark = 9.600
        execution_mark = 9.000

elif country == "Bulgaria":
    if tool == "ribbon":
        difficulty_mark = 9.600
        execution_mark = 9.400
    elif tool == "hoop":
        difficulty_mark = 9.550
        execution_mark = 9.750
    elif tool == "rope":
        difficulty_mark = 9.500
        execution_mark = 9.400

elif country == "Italy":
    if tool == "ribbon":
        difficulty_mark = 9.200
        execution_mark = 9.500
    elif tool == "hoop":
        difficulty_mark = 9.450
        execution_mark = 9.350
    elif tool == "rope":
        difficulty_mark = 9.700
        execution_mark = 9.150


total_mark = difficulty_mark + execution_mark
percentage_max_mark = 20 / 100
percentage_not_enough = (20 - total_mark) / percentage_max_mark
print(f"The team of {country} get {total_mark:.3f} on {tool}.")
print(f"{percentage_not_enough:.2f}%")