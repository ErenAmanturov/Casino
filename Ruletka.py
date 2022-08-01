import random


class Ruletka:

    def __init__(self):
        self.players_moneyr = 1000
        self.choice = input('Ваш выбор(Red, Black) или (0 до 36): ')

    def start(self):
        self.bet = int(input(f'Ваш баланс: {self.players_moneyr}.\nВаша ставка: '))
        integers = random.choice([i for i in range(0, 35)])
        colours = random.choice(['Red', 'Black'])
        if self.players_moneyr >= int(self.bet) >= 50:
            if str(self.choice) == colours:
                self.players_moneyr += (int(self.bet) * 2)
                return f'Вы Выиграли\n' \
                       f'Ваш баланс: {self.players_moneyr}'
            elif self.choice == integers:
                self.players_moneyr += (int(self.bet) * 3)
                return f'Вы Выиграли\n' \
                       f'Ваш баланс: {self.players_moneyr}'
            else:
                self.players_moneyr -= int(self.bet)
                return f'Вы проиграли\n' \
                       f'Ваш баланс: {self.players_moneyr}'
        else:
            return 'Ставка должна быть больше 50. Ограничения твои деньги'
