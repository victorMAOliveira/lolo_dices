"""
Holds the class 'Dice' that represents a dice in the program
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
        
        Args:
            sides (int): Number of sides for the new dice
        
        Raises:
            ValueError: If sides for the new dice is not int the currently 
            available dice types
        """
        if sides not in self.DICE_TYPES:
            raise ValueError(f"The a dice with a number of sides -> {sides} <- is not available")
        else:
            self.sides = sides
            
    def __str__(self):
        """
        String representation of the dice object
        """
        return f"d{self.sides}"
            
    def roll(self) -> int:
        """
        Rolls a random number between 1 and the amount of sides of the dice
        
        Returns:
            The result of the rolling
        """
        min_result = 1
        max_result = self.sides
        
        return random.randint(min_result, max_result)