import copy
import random
# Consider using the modules imported above.

class Hat:
    
    def __init__(self, **kwargs): #kwargs to get dictionary of inputs
        # print(kwargs)
        self.contents = []
        # appends key value number of times 
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
            print(self.contents)
    
    def draw(self, number):
        if(number > len(self.contents)):
            return self.contents
        
        removed_list = []
        for i in range(number):
            removed = self.contents.pop(int(random.random() * len(self.contents)))
            removed_list.append(removed)
        return removed_list



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for i in range(num_experiments):
        # deepcopy parameters for each experiment
        t_hat = copy.deepcopy(hat)
        t_expected = copy.deepcopy(expected_balls)

        # tallies each drawn from expected
        t_drawn = t_hat.draw(num_balls_drawn) # list
        for ball in t_drawn:
            if(ball in t_expected):
                t_expected[ball] -= 1
        
        # verifying draw is what we want
        if (all(x <= 0 for x in t_expected.values())):
            success += 1

    return success/num_experiments
        