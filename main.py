import random as rand

def ten_pull():
    [one_pull() for _ in range(10)]

def one_pull():
    global counter
    counter += 1
    print(counter)

if __name__ == '__main__':
    counter = 0

    inp = input("enter command: ")
    while(inp != 'q'):
        if inp == '1':
            one_pull()
        if inp == '10':
            ten_pull()
        inp = input("enter command: ")