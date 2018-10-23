# -*- coding: utf-8 -*-


class BaseActor(object):
    def __init__(self, game_manager, name=None, job=None, money=None, current_location=None):
        self.name = name
        self.job = job
        self._money = money
        self._energy = 100
        self._full = 100

        self._current_location = current_location

        self.game_manager = game_manager

    def save(self):
        return {
            "name": self.name,
            "job": self.job,
            "money": self.money,
            "energy": self.energy,
            "full": self.full,
            "current_location": None if self._current_location is None else self._current_location.name}

    def load(self, value):
        self.name = value["name"]
        self.job = value["job"]
        self._money = value["money"]
        self._energy = value["energy"]
        self._full = value["full"]
        self._current_location = self.game_manager.map_manager.find(value["current_location"])

    @property
    def money(self):
        return self._money

    def add_money(self, change_money):
        if change_money is not int:
            raise ValueError('change_money should be a int object')
        if (self._money + change_money) < 0:
            raise ValueError('your money is less than what you want')
        else:
            self._money += change_money

    @property
    def energy(self):
        return self._energy

    def add_energy(self, change_energy):
        if change_energy is not int:
            raise ValueError('change_energy should be a int object')
        if (self._energy + change_energy) < 0:
            raise ValueError('your change_energy is less than what you want')
        else:
            self._energy = min(self._energy + change_energy, 100)

    @property
    def full(self):
        return self._full

    def add_full(self, change_full):
        if change_full is not int:
            raise ValueError('change_full should be a int object')
        if (self._full + change_full) < 0:
            raise ValueError('your change_full is less than what you want')
        else:
            self._full = min(self._full + change_full, 100)

    @property
    def current_location(self):
        return self._current_location

    def move_location(self, next_location):
        if self._current_location is None:
            self._current_location = next_location
        else:
            if next_location not in self._current_location.routes:
                raise ValueError('you cannot move to this location')
            self._current_location = next_location
