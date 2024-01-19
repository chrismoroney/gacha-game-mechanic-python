import random as rand

class gacha_simulator():
    def __init__(self):
        self.counter = 0
        self.five_star = self.generate_five_star_occ()
        self.four_star = self.generate_four_star_occ()

    def generate_five_star_occ(self):
        return rand.randrange(0,100) + 1

    def generate_four_star_occ(self):
        return rand.randrange(0,10) + 1

    def ten_pull(self):
        for _ in range(10):
            self.one_pull()

    def one_pull(self):
        self.counter += 1
        if self.counter == self.four_star:
            print('4-star item')
            self.four_star = self.counter + self.generate_four_star_occ()
        elif self.counter == self.five_star:
            print('5-star item')
            self.five_star = self.counter + self.generate_five_star_occ()
        else:
            print('3-star item')