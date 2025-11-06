"""
Dice module with all necessary functions to represent the dice in the program
"""
import random

class Dice:
    """
    Dice class that has all the information and functions necessary for a dice
    """
    sides: int
    
    DICE_TYPES = {4, 6, 8, 10, 12, 20, 100}
    
    def __init__(self, sides: int):
        """
        Checks if the new dice has a valid amount of sides and then creates the 
        object
        """
        if sides not in self.DICE_TYPES:
            raise ValueError(f"The a dice with a number of sides -> {sides} <- is not available")
        else:
            self.sides = sides
            
    def __str__(self):
        return f"d{self.sides}"
            
    def roll(self) -> int:
        """
        Rolls a random number between 1 and the amount of sides of the dice and
        returns the result
        """
        min_result = 1
        max_result = self.sides
        
        return random.randint(min_result, max_result)

class History:
    """
    History of all rolling that has been done in the lifetime of the program
    """
    pass