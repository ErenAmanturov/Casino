import random


class Casino:

    def ruletka(self, players_moneyr, choice):
        self.players_moneyr = players_moneyr
        self.choice = choice

    def enter(self, choice):
        self.choice = choice

    def start(self, bet):
        self.bet = bet
        integers = random.choice([i for i in range(0, 36)])
        colours = random.choice(['Red', 'Black'])
        if self.players_moneyr >= self.bet >= 50:
            if self.choice == integers:
                self.players_moneyr += (self.bet * 3)
                return self.players_moneyr
            elif self.choice == colours:
                self.players_moneyr += (self.bet * 2)
                return self.players_moneyr
            else:
                self.players_moneyr -= self.bet
                return self.players_moneyr
        else:
            return 'Ставка должна быть больше 50. Ограничения твои деньги'
