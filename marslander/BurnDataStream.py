class BurnDataStream:
    def __init__(self, burns=None):
        # these are the series of burns made each 10 secs by the lander.
        # change them to see if you can get the lander to make a soft landing.
        # burns are between 0 and 200. This burn array usually crashes.
        if burns is None:
            self.burn_array = [100, 100, 200, 200, 100, 100, 0, 0, 200, 100, 100, 0, 0, 0, 0]
        else:
            self.burn_array = burns
        self.burn_idx = -1

    def get_next_burn(self, status):
        if self.burn_idx < len(self.burn_array) - 1:
            self.burn_idx += 1
            print(self.burn_array[self.burn_idx])  # hack!
            return self.burn_array[self.burn_idx]
        return 0
