import random


class Koleso:
    sectors = []
    def __init__(self, players_moneyk, sector):
        self.players_moneyk = players_moneyk
        self.sector = sector

    def start(self):
        sector