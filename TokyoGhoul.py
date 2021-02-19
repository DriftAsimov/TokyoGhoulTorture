import time

welcome = "╔═════════════════════╗ \n\n TORTURE FROM JSON \n\n╚═════════════════════╝"
for i in welcome:
    time.sleep(0.1)
    print(i, end="")

initial = 1000

while True:
    ask = f"\n \nWhat's {initial} - 7"
    for i in ask:
        time.sleep(0.1)
        print(i, end="")
    user_input = int(input(": "))
    initial -= 7
    if user_input == initial:
        continue
    else:
        wrong = "Wrong answer. -inserts earthworms into your ears-"
        for i in wrong:
            time.sleep(0.1)
            print(i, end="")
        break
