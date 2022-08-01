class Lottery:

    def __init__(self):
        self.players_money = 1000
        while True:
            print(f'Деньги игрока:{self.players_money}')
            print(f'Сумма билета: 20')
            print('Билеты от 00000 до 00030')
            a = input('Введите номер билета:')
            if len(a) == 5:
                if a == '0003':
                    self.players_money += 50
                    print(f'20 учтены из ваших денег.\nВы получили 70.\nДенег стало: {self.players_money - 20}')
                elif a == '00004':
                    self.players_money += 80
                    print(f'20 учтены из ваших денег.\nВы получили 100.\nДенег стало: {self.players_money - 20}')
                elif a == '0008':
                    self.players_money += 40
                    print(f'20 учтены из ваших денег.\nВы получили 60.\nДенег стало: {self.players_money - 20}')
                elif a == '00012':
                    self.players_money += 10
                    print(f'20 учтены из ваших денег.\nВы получили 30.\nДенег стало: {self.players_money - 20}')
                elif a == '00016':
                    self.players_money += 30
                    print(f'20 учтены из ваших денег.\nВы получили 50.\nДенег стало: {self.players_money - 20}')
                elif a == '00020':
                    self.players_money += 70
                    print(f'20 учтены из ваших денег.\nВы получили 90.\nДенег стало: {self.players_money - 20}')
                elif a == '00024':
                    self.players_money += 30
                    print(f'20 учтены из ваших денег.\nВы получили 50.\nДенег стало: {self.players_money - 20}')
                elif a == '00025':
                    self.players_money += 20
                    print(f'20 учтены из ваших денег.\nВы получили 20.\nДенег стало: {self.players_money - 20}')
                elif a == '00028':
                    self.players_money += 20
                    print(f'20 учтены из ваших денег.\nВы получили 20.\nНе везет. В следующий раз!\nДенег стало: '
                          f'{self.players_money - 20}')
                elif a == '00029':
                    self.players_money += 1000000
                    print(f'Вы получили 1000000.\nИгра окончена вы выиграли')
                    break
                elif self.players_money < 20:
                    print('Лузер, ты проиграл')
                    break
                else:
                    self.players_money -= 20
                    print(f'20 учтены из ваших денег.\nВы получили 0\nДенег стало: {self.players_money}')
            else:
                print('Неправильный номер билета')
