import random as rand

class gacha_simulator():
    def __init__(self):
        self.counter_four_star = 0
        self.counter_five_star = 0

    def ten_pull(self):
        for _ in range(10):
            self.one_pull()

    def one_pull(self):
        pull = rand.randint(0, 99)
        '''
        four_star: 10% chance + 10% per pull after 10 pulls
        five_star: 1% chance + 5% per pull after 100 pulls
        '''
        four_star_pull = 10 + 10 * max(0, self.counter_four_star - 10)
        five_star_pull = 1 + 5 * max(0, self.counter_five_star - 100)

        if pull < five_star_pull:
            print('5-star item')
            self.counter_five_star = 0
            self.counter_four_star = 0
        else:
            if pull < four_star_pull:
                print('4-star item')
                self.counter_four_star = 0
            else:
                print('3-star item')
            self.counter_five_star += 1
            self.counter_four_star += 1