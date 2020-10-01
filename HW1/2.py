time_seconds = int(input('Введите количество секунд: '))
time = [0, 0, 0]


def convert_time(time_seconds):
    while time_seconds > 60:
        while time_seconds > 3600:
            time[0] += 1
            time_seconds -= 3600
        time[1] += 1
        time_seconds -= 60
    time[2] = time_seconds


convert_time(time_seconds)
print(time)

print(f'Это {time[0]}ч:{time[1]}м:{time[2]}с')
