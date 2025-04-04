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

    @staticmethod
    def random_altitude():
        max_altitude = 20000
        min_altitude = 10000
        r = random.randint(min_altitude, max_altitude)
        return (r % 15000 + 4000)

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
        while self.vehicle.still_flying():
            status = self.vehicle.get_status(burn_interval)
            print(f"{status}\t\t")
            self.vehicle.adjust_for_burn(burn_source.get_next_burn(status))
            if self.vehicle.out_of_fuel():
                break
            burn_interval += 1
            if burn_interval % 9 == 0:
                self.print_string(self.get_header())
        self.print_string(self.vehicle.check_final_status())
        if status is not None:
            return status.get_status()
        return -1

    @staticmethod
    def main():
        # create a new BurnInputStream
        burnSource = BurnInputStream()
        # create a new Simulation object with a random starting altitude
        game = Simulation(Vehicle(Simulation.random_altitude()))
        # pass the new BurnInputStream to the run_simulation method
        result = game.run_simulation(burnSource)
        return result


if __name__ == '__main__':
    Simulation.main()