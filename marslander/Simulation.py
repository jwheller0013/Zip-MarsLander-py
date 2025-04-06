import random

from Vehicle import Vehicle
from BurnDataStream import BurnDataStream
from OnBoardComputer import OnBoardComputer
from DescentEvent import DescentEvent
from BurnInputStream import BurnInputStream


class Simulation:
    # Mars Simulation Source Code.

    version = "2.0"  # The Version of the program

    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.onboard_computer = None
        self.descent_event = None

    @staticmethod
    def random_altitude():
        max_altitude = 20000
        min_altitude = 10000
        r = random.randint(min_altitude, max_altitude)
        #had to change the return value below from 4000 to something passable like 5010
        #if velocity starts at 1000 it takes 10 intervals to slow down to 0 or under 3 per game rules
        # so total needed to stop = (initial speed + desired end speed)/2 * 10 since need average speed going
        # down then times the 10 intervals needed to stop at 1000. It equals 5010
        return (r % 15000 + 5010)

    def game_header(self):
        s = ""
        s += "\nMars Simulation - Version " + self.version + "\n"
        s += "Elon Musk has sent a really expensive Starship to land on Mars.\n"
        s += "The on-board computer has failed! You have to land the spacecraft manually.\n"
        s += "Set burn rate of retro rockets to any value between 0 (free fall) and 200\n"
        s += "(maximum burn) kilo per second. Set burn rate every 10 seconds.\n"
        s += "You must land at a speed of 2 or 1. Good Luck!\n\n"
        return s

    def get_header(self):
        s = ""
        s += "\nTime\t"
        s += "Velocity\t\t"
        s += "Fuel\t\t"
        s += "Altitude\t\t"
        s += "Burn\n"
        s += "----\t"
        s += "-----\t\t"
        s += "----\t\t"
        s += "------\t\t"
        s += "----\n"
        return s

    def print_string(self, string):
        # print long strings with new lines in them.
        lines = string.split("\n")
        for line in lines:
            print(line)

    # main game loop
    def run_simulation(self, burn_source):
        status = None
        burn_interval = 0
        self.print_string(self.game_header())
        self.print_string(self.get_header())
        # print(f"Initial still_flying: {self.vehicle.still_flying()}")
        while self.vehicle.still_flying():
            status = self.vehicle.get_status(burn_interval)
            # comp_status = self.vehicle.comp_status()
            # onboard_computer = OnBoardComputer(comp_status)
            print(f"{status}\t\t")

            # if isinstance(burn_source, BurnInputStream):
            #     burn = burn_source.get_next_burn(status)
            # elif isinstance(burn_source, OnBoardComputer):
            #     burn = onboard_computer.get_next_burn()
            #adjusted to allow OnBoardComputer to be called
            #working on this change "burn_source.get_next_burn(status)" below for burn
            self.vehicle.adjust_for_burn(burn_source.get_next_burn(status))
            self.descent_event = self.vehicle.get_status(burn_interval)
            if self.vehicle.out_of_fuel():
                break
            burn_interval += 1
            if burn_interval % 9 == 0:
                self.print_string(self.get_header())
        self.vehicle.check_final_status()
        final_status_message = self.vehicle.check_final_status()
        #checking something if final status is being called properly
        self.print_string(final_status_message)
        final_status_event = self.vehicle.get_status(burn_interval)
        return final_status_event.get_status()
        # if status is not None:
        #     return status.get_status()
        # return -1

    @staticmethod
    def main():
        # create a new Simulation object with a random starting altitude (moved it to top so can start with it)
        game = Simulation(Vehicle(Simulation.random_altitude()))
        # create a new BurnInputStream
        # burnSource = BurnInputStream()
        # how about using the OnBoardComputer
        burnSource = OnBoardComputer()

        # pass the new BurnInputStream to the run_simulation method
        result = game.run_simulation(burnSource)
        return result


if __name__ == '__main__':
    Simulation.main()