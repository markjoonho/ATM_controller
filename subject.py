from observer import *


class Subject:
    def __init__(self):
        self.observer_list = []

    def attach(self, ob):
        self.observer_list.append(ob)

    def detach(self, ob):
        for observer in self.observer_list:
            if ob == observer:
                self.observer_list.remove(ob)
                break

    def notifyObserver(self, card_num=0):
        for o in self.observer_list:
            o.notify(card_num)
