class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        l_sorted = sorted([[p,s] for p, s in zip(position, speed)], reverse = True)
        
        # l_sorted is a list of couples position and its corresponding speed , sorted in a reverse order of position

        time = []

        # time is a stack where we push the time of arriving to target higher than the top of the stack, i.e the time of the car forming a new fleet

        for p, s in l_sorted :

            t = (target - p )/s

            if time and t<=time[-1]:
                continue
            time.append(t)

        return len(time)
