import string

import data
from toolset import *
def problem31():
    """How many different ways can 2 pounds be made using any number of coins?"""
    def get_weights(units, remaining):
        """Return weights that sum 'remaining'. Pass units in descending order.  
        get_weigths([4,2,1], 5) -> (0,0,5), (0,1,3), (0,2,1), (1,0,1)"""   
        if len(units) == 1 and remaining % units[0] == 0:
            # Make it generic, do not assume that last unit is 1
            yield (remaining/units[0],)
        elif units:
            for weight in xrange(0, remaining + 1, units[0]):
                for other_weights in get_weights(units[1:], remaining - weight):
                   yield (weight/units[0],) + other_weights
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    return ilen(get_weights(sorted(coins, reverse=True), 200))

print problem31()
