# -*- coding: utf-8 -*-


class EventManager(object):
    def __init__(self, game_manager, name=""):
        self.game_manager = game_manager
        self.name = name
        self.time_slice_count = 0
        self.state = 'Pause'
        self.event_list = []

    def add_event(self, event):
        event.start_time = self.time_slice_count
        self.event_list.append(event)

    def run_time(self, ticks=50):
        self.state = 'Run'
        ticks_temp = 0
        while ticks_temp < ticks:
            if self.state == 'Run':
                self.time_slice_count += 1
                for event in list(self.event_list):
                    if event.end_time == self.time_slice_count:
                        pass
                        # TODO: PERFORM EVENT, ASK FOR NEXT ONE, REMOVE THE OLD ONE
            else:
                pass
            ticks_temp += 1
