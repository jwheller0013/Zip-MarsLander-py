class DescentEvent:
    def __init__(self, t, sp, f, h, st):
        self.seconds = t * 10
        self.velocity = sp
        self.fuel = f
        self.altitude = h
        self.status = st

    def get_velocity(self):
        return self.velocity

    def get_altitude(self):
        return self.altitude

    def get_status(self):
        return self.status

    def __str__(self):
        return f"{self.seconds}\t\t{self.velocity}\t\t{self.fuel}\t\t{self.altitude}"
