from gacha_simulator import gacha_simulator

if __name__ == '__main__':
    game = gacha_simulator()
    inp = input("enter command: ")
    while(inp != 'q'):
        if inp == '1':
            game.one_pull()
        elif inp == '10':
            game.ten_pull()
        else:
            print("Please input valid command.\n")
        inp = input("enter command: ")