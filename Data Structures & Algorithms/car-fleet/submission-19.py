import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Goal: number of different car fleets

        runtime O(nlogn)

        Obs: 
        - order of cars will never change
        - you will arrive in a fleet with another car if the car fleet that you are in 
        "crashes" into another car fleet before target is reached

        suppose we know the full speed graph of the car fleet in front of us:
        - then we know whether we will crash into them or not

        We can model this as a stack where the stack is the cars in the current car fleet:

        Is there a case where you wouldn't into the n + 1th car but into the nth car which crashes into the n + 1th? 

        Could we just check for the i-th car, how many cars in front of it can it reach?
        - this is not enough, because the car in front of you might go slower
        -> can we then just take the min()? I.e. if you can reach 4 in front of you but the one in front can only reach 1, then you can only reach 2? 

        How do we efficiently determine how many in front of you are reachable? 
        - brute force: n * (n/2) -> n^2
        - 

        Can we just have a stack of cars: 
        - start with last car and put on stack
        - ask for next car: can I reach the bottom car on the stack?
            - yes -> put on stack
            - no -> empty the stack and increment fleet counter
        
        mx - nx = a - b / m - n


        """
        fleet_counter = 0
        curr_fleet = []

        def _is_reachable(position, speed, head):
            tx, tv = head
        
            # case where the cars are already moving at the same speed
            if tv >= speed: return False

            t = (tx - position) / (speed - tv)
            x_intersect = math.ceil(tv * t + tx)
        
            if x_intersect <= target:
                return True
            return False

        for position, speed in reversed(sorted(zip(position, speed))):
            if len(curr_fleet) == 0:
                curr_fleet.append((position, speed))
                continue
            if _is_reachable(position, speed, curr_fleet[0]):
                curr_fleet.append((position, speed))
            else: 
                fleet_counter += 1
                curr_fleet = [(position, speed)]

        if len(curr_fleet) > 0: 
            fleet_counter += 1

        return fleet_counter