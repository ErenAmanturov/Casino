from Lottery import Lottery
from Ruletka import Ruletka


game = input('Какую игру будете играть(Ruletka or Lottery): ')
if game == 'Ruletka':
    while True:
        rul = Ruletka()
        print(rul.start())
        if rul.players_moneyr == 0:
            print('Вы проиграли все деньги. Не зря ХАРАМ')
            break
else:
    lot = Lottery()