
class Vehicle:
    gravity = 100

    # Various end-of-game messages and status result codes.
    dead = "\nCRASH!!\n\tThere were no survivors.\n\n";
    DEAD = -3;
    crashed = "\nThe Starship crashed. Good luck getting back home. Elon is pissed.\n\n";
    CRASHED = -2;
    emptyfuel = "\nThere is no fuel left. You're floating around like Major Tom.\n\n";
    EMPTYFUEL = -1;
    success = "\nYou made it! Good job!\n\n";
    SUCCESS = 0;
    FLYING = 1;

    def __init__(self, initial_altitude):
        # initialize the altitude AND previous altitude to initialAltitude

        self.altitude= 8000
        self.prev_altitude= 8000

        self.velocity= 1000
        self.fuel = 12000
        self.burn = 0
        self.flying = Vehicle.FLYING
        pass

    def check_final_status(self):
        s = ""
        if self.altitude <= 0:
            if self.velocity > 10:
                s = self.dead
                self.flying = self.DEAD
            elif 3 < self.velocity <= 10:
                s = self.crashed
                self.flying = self.CRASHED
            elif self.velocity <= 3:
                s = self.success
                self.flying = self.SUCCESS
        else:
            if self.altitude > 0:
                s = self.emptyfuel
                self.flying = self.EMPTYFUEL
        return s


    def compute_deltaV(self):
        # return velocity + gravity - burn amount
        pass

    def adjust_for_burn(self, burnAmount):
        # set burn to burnamount requested
        # save previousAltitude with current Altitude
        # set new velocity to result of computeDeltaV function.
        # subtract speed from Altitude
        # subtract burn amount fuel used from tank
        pass

    def still_flying(self):
        # return true if altitude is positive
        pass

    def out_of_fuel(self):
        # return true if fuel is less than or equal to zero
        pass

    def get_status(self, tick):
        # create a return a new DescentEvent object
        # filled in with the state of the vehicle.
        pass


