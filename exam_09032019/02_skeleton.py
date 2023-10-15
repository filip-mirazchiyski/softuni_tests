control_minutes = int(input())
control_seconds = int(input())
slope_length = int(input())
seconds_for_100m = int(input())

total_control_seconds = control_minutes * 60 + control_seconds
total_times_slow_down = slope_length / 120
total_seconds_slow_down = total_times_slow_down * 2.5

marin_time = (slope_length / 100) * seconds_for_100m - total_seconds_slow_down

if marin_time <= total_control_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {marin_time:.3f}.")
else:
    extra_seconds = marin_time - total_control_seconds
    print(f"No, Marin failed! He was {extra_seconds:.3f} second slower.")
