# -*- coding: utf-8 -*-


class TimeManager(object):
    def __init__(self, game_manager, name="", start_time=0):
        self.game_manager = game_manager
        self.name = name
        self.start_time = start_time
        self.time_slice_count = 0
        self.state = 'Pause'
        self.action_list = []

    def add_action(self, action):
        action.start_time = self.time_slice_count
        self.action_list.append(action)

    def run_time(self, ticks=0):
        self.state = 'Run'
        ticks_temp = 0
        while ticks_temp < ticks:
            if self.state == 'Run':
                self.time_slice_count += 1
                for action in list(self.action_list):
                    if action.start_time + action.during_count == self.start_time + self.time_slice_count:
                        action.complete()
                        self.action_list.remove(action)
            else:
                pass
            ticks_temp += 1

    def save(self):
        return {"name": self.name, "start_time": self.start_time, "time_slice_count": self.time_slice_count,
                "state": self.state, "action": [action.save() for action in self.action_list]}

    def load_base_element(self, value):
        self.name = value['name']
        self.start_time = value['start_time']
        self.time_slice_count = value['time_slice_count']

    def load_reference(self, value):
        pass
