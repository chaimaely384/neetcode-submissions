class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        d_sorted = sorted([[p,s] for p, s in zip(position, speed)], reverse = True)
        #p_sorted = sorted(position, reverse=True)

        time = []

        for p, s in d_sorted :

            t = (target - p )/s

            if time and t<=time[-1]:
                continue
            time.append(t)

        return len(time)
