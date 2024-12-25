import time
import keyboard


def main():
    time.sleep(2)

    with open('input.txt', 'r') as file:
        lines = file.readlines()


    for line in lines:
        for char in line:
            print(f"Char: {char}")
            if char.isalnum():
                time.sleep(0.1)
                if char.isupper():
                    keyboard.send(f"shift + {char.lower()}")
                else:
                    keyboard.send(char)
            elif char == '\n':
                time.sleep(0.5)
                keyboard.send('enter')
                time.sleep(0.5)
            else:
                print(f"Char {char} not supported")


if __name__ == '__main__':
    main()
