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
    
    try:
        user_input = int(input(": "))
    
        initial -= 7

        if user_input == initial:
            continue
        else:
            wrong = "\nWrong answer. -inserts earthworms into your ears-"
            for i in wrong:
                time.sleep(0.1)
                print(i, end="")
            break

        if user_input < 10 and initial < 10:
            congrats = "\nCongratulations on completing this torture, now you can go home.. \nYou: Wow really?! Thanks a lo- -stabs you with his kagune-...."
            for i in congrats:
                time.sleep(0.1)
                print(i, end="")
            break

    except:
        fool = "\nYou are a fool, you can't read -takes out your eyeballs-"
        for i in fool:
            time.sleep(0.1)
            print(i, end="")
        break
