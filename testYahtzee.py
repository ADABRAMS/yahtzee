# importing from unittest and Die.  The unittest module has a class called TestCase.
# There are lots of methods associated with that class that help to test your code.
# Die.py has our Die class of course.
import unittest
from Die import Die


# the beginning of our Yahtzee class.  This is our game.
# right now there is the initialization routine __init__ which is called each time
# you instantiate an instance of the class.
# There is a difference in the class definition and the instantiation of it.
# The class is like a template that you create an object from.
class Yahtzee():
    def __init__(self):
        self.chosen = ()  # This will keep the indices for the dice we don't want to roll again
        self.d1 = Die(6)  # these are our 5 dice
        self.d2 = Die(6)
        self.d3 = Die(6)
        self.d4 = Die(6)
        self.d5 = Die(6)
        # we collect them in something called cup_of_dice
        self.cup_of_dice = [self.d1, self.d2, self.d3, self.d4, self.d5]



        # figure out if numbers which is a list of 5 numbers between 1 and 6
        # if they are all the same and return 50 if that is the case
        # if not, return the sum of all the numbers

    def roll(self):  # we call this to roll the dice
        if len(self.chosen) == 0:  # If nothing is chosen to hold, roll them all
            rolled_dice = [self.d1.roll(), self.d2.roll(), self.d3.roll(), self.d4.roll(), self.d5.roll()]
            return rolled_dice
        else:  # disable the dice that we don't want to roll
            for v in self.chosen:  # v will be an index into cup_of_dice
                self.cup_of_dice[v].active = False  # when a die is not active, it just keeps its value
            rolled_dice = [self.d1.roll(), self.d2.roll(), self.d3.roll(), self.d4.roll(), self.d5.roll()]
            return rolled_dice

    def choose(self, choice):  # choice will be a tuple
        self.chosen = choice  # save it into the chosen variable.

    def score(self, values):
        self.game = Yahtzee()
        values = [1, 1, 1, 1, 1]
        self.assertTrue(self.game.score(values) == 50)
        values = [1, 2, 3, 4, 5]
        self.assertTrue(self.game.score(values) != 15)

    def assertTrue(self, param):
        pass


# this is our test case
# it inherits the methods from unittest.TestCase
# methods like assertTrue (you need self.assertTrue since it's part of the unittest.TestCase class)
class MyTestCase(unittest.TestCase):
    def test_yahtzee(self):
        self.game = Yahtzee()  # just make sure we can create the game

    def test_roll(self):
        self.game = Yahtzee()
        values = self.game.roll()
        self.assertEqual(5, len(values))  # make sure we get 5 values from the roll

    def test_die(self):
        d = Die(6)
        v = d.roll()
        self.assertGreater(v, 0)  # make sure the values are between 0 and 7
        self.assertLess(v, 7)

    def test_choose(self):
        self.game = Yahtzee()
        values = self.game.roll()
        print(values)
        self.game.choose((0, 1))
        new_values = self.game.roll()
        print(new_values)
        self.assertEqual(values[0], new_values[0])  # make sure the first two values didn't change
        self.assertEqual(values[1], new_values[1])

    def score(self):
        self.game = Yahtzee()
        values = [1, 1, 1, 1, 1]
        self.assertTrue(self.game.score(values) == 50)
        values = [1, 2, 3, 4, 5]
        self.assertTrue(self.game.score(values) != 15)


if __name__ == '__main__':
    unittest.main()
