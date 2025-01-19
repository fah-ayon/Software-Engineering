class Celebrity:
    def __init__(self):
        self._fans = []
        self._state = None
    def attach(self, fan):
        self._fans.append(fan)
    def detach(self, fan):
        self._fans.remove(fan)
    def _notify(self):
        for fan in self._fans:
            fan.update(self)
    def set_state(self, state):
        self._state = state
        self._notify()
    def get_state(self):
        return self._state

class Fan:
    def __init__(self):
        self._celebrities = []
    def update(self, celebrity):
        state = celebrity.get_state()
    def add_celebrity(self, celebrity):         
        self._celebrities.append(celebrity)
        celebrity.attach(self)
    def remove_celebrity(self, celebrity):
        self._celebrities.remove(celebrity)
        celebrity.detach(self)
celebrity = Celebrity()
fan = Fan()
#fan starts following…
fan.add_celebrity(celebrity)
#celeb changes status and #notification is received by fan.
celebrity.set_state('New state')
#fan can stop following…
fan.remove_celebrity(celebrity)
