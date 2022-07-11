from typing import List, Tuple


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """ Calculates the resulting asteroids after collision.

        Args:
          asteroids: An array of integers representing asteroids in a row.

        Returns:
          An array of integers representing the resulting asteroids.
        """
        base = 1

        while base is not None:
            base, match = self.getMatch(asteroids=asteroids, start=base if base >= 1 else 1)

            if base is not None:
                if abs(asteroids[base]) == abs(asteroids[match]):
                    del asteroids[base: match + 1]
                else:
                    del asteroids[match if abs(asteroids[base]) > abs(asteroids[match]) else base]

        return asteroids

    def getDirection(self, asteroid: int) -> bool:
        """ Calculates the direction of the asteroid.

        Args:
          asteroid: Integer representation of the asteroid direction and magnitude.

        Returns:
          Boolean representation of the asteroid direction (True meaning right, False meaning left).
        """
        return True if asteroid > 0 else False
    
    def getMatch(self, start: int, asteroids: List[int]) -> Tuple[int, int]:
        """ Detects a collision of asteroids on the given array.

        Args:
          start: Index of the starting point to check in the asteroids array.
          asteroids: An array of integers representing asteroids in a row.

        Returns:
          The indexes of the collision asteroids, tuple with two index values.
        """
        for i in range(start, len(asteroids)):
            if self.getDirection(asteroids[i - 1]) and not self.getDirection(asteroids[i]):
                return i - 1, i
        return None, None