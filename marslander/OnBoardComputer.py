from DescentEvent import DescentEvent

class OnBoardComputer:
    def __init__(self, descent_event):
        self.descent_event = descent_event

    def get_next_burn(self, status):
        alt = self.descent_event.get_altitude()
        velocity = self.descent_event.get_velocity()

        burn = 0

        if 1000 < alt < 4500:
            if velocity == 0:
                burn = 0
            else:
                burn = 200

        elif alt < 1000 and 100 <= velocity < 103:
            burn = 100

        elif alt < 100 and velocity > 2:
            burn = 98

        elif alt < 100 and 0 < velocity < 3:
            burn = 100

        print(burn)  # hack!
        return burn


#at most can slow speed by 100
#so 1000 takes 10 inputs to reach 0 during that time travel 4500 in game
#end velocity has to be between 1-2 m/s at the end
# a series of if/else statements seems to be how to approach issue
# if altitude is high just let it fall
# some point burn 200 to slow down till hits 0 speed
# some point burn 0 or 200 to this way bounce between 0 and 100 speed
    # if 1000 < alt < 4500:
        # if velocity = 0 set burn 0
        # else set burn 200
# low point and low speed burn 100
    # if alt < 1000 and 100 =< velocity < 103 set burn to 100
# some set really low point give a burn to drop speed to 1 or 2 (adding 98 will give 2 speed increase)
    # if alt < 100 and velocity > 2 set burn to 98
# at said really low point and speed is 1 or 2 just 100 repeatedly till end
    # if alt < 100 and 0 < velocity < 3 set burn to 100