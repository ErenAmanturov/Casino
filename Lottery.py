class Lottery:

    players_money = 100
    while True:
        print(f'Деньги игрока:{players_money}')
        print(f'Сумма билета: 20')
        print('Билеты от 00000 до 00030')
        a = input('Введите номер билета:')
        if a == '0003':
            players_money += 50
            print(f'20 учтены из ваших денег.\nВы получили 70.\nДенег стало: {players_money - 20}')
        elif a == '00004':
            players_money += 80
            print(f'20 учтены из ваших денег.\nВы получили 100.\nДенег стало: {players_money - 20}')
        elif a == '0008':
            players_money += 40
            print(f'20 учтены из ваших денег.\nВы получили 60.\nДенег стало: {players_money - 20}')
        elif a == '00012':
            players_money += 10
            print(f'20 учтены из ваших денег.\nВы получили 30.\nДенег стало: {players_money - 20}')
        elif a == '00016':
            players_money += 30
            print(f'20 учтены из ваших денег.\nВы получили 50.\nДенег стало: {players_money - 20}')
        elif a == '00020':
            players_money += 70
            print(f'20 учтены из ваших денег.\nВы получили 90.\nДенег стало: {players_money - 20}')
        elif a == '00024':
            players_money += 30
            print(f'20 учтены из ваших денег.\nВы получили 50.\nДенег стало: {players_money - 20}')
        elif a == '00025':
            players_money += 20
            print(f'20 учтены из ваших денег.\nВы получили 20.\nДенег стало: {players_money - 20}')
        elif a == '00028':
            players_money += 20
            print(f'20 учтены из ваших денег.\nВы получили 20.\nНе везет. В следующий раз!\nДенег стало: '
                  f'{players_money - 20}')
        elif a == '00029':
            players_money += 1000000
            print(f'20 учтены из ваших денег.\nВы получили 1000000.\nИгра окончена вы выиграли')
            break
        elif players_money < 20:
            print('Лузер, ты проиграл')
            break
        else:
            players_money -= 20
            print(f'20 учтены из ваших денег.\nВы получили 0\nДенег стало: {players_money}')
