import random as rand

def generate_five_star_occ():
    return rand.randrange(0,100) + 1

def generate_four_star_occ():
    return rand.randrange(0,10) + 1

def ten_pull():
    [one_pull() for _ in range(10)]

def one_pull():
    global counter, five_star, four_star
    counter += 1
    if counter == four_star:
        print('4-star item')
        four_star = counter + generate_four_star_occ()
    elif counter == five_star:
        print('5-star item')
        five_star = counter + generate_five_star_occ()
    else:
        print('3-star item')

five_star = generate_five_star_occ()
four_star = generate_four_star_occ()

if __name__ == '__main__':
    counter = 0
    five_star = generate_five_star_occ()
    four_star = generate_four_star_occ()
    print(five_star)
    print(four_star)
    inp = input("enter command: ")
    while(inp != 'q'):
        if inp == '1':
            one_pull()
        if inp == '10':
            ten_pull()
        inp = input("enter command: ")