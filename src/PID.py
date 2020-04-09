class PID(object):
    def __init__(self):
        self.p = -1
        self.i = -1
        self.d = -1
        self.v = -1
        self.v_ref = -1