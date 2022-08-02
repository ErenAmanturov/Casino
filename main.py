from Lottery import Lottery
from Ruletka import Ruletka


game = input('Какую игру будете играть(Ruletka or Lottery): ')
while True:
    if game == 'Ruletka':
        rul = Ruletka(1000)
        while True:
            print(rul.start())
            if rul.players_moneyr == 0:
                print('Вы проиграли все деньги. Не зря ХАРАМ')
                break
    elif game == 'Lottery':
        lot = Lottery()
    else:
        print('Только Рулетка и Лотарея')
        break