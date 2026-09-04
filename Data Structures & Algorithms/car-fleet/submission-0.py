class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        d = {}
        for i in range (len(position)) :
            d[position[i]]= speed[i]

        p_sorted = sorted(position, reverse=True)

        time = []

        for i in range (len(position)) :

            t = (target - p_sorted[i] )/d[p_sorted[i]]

            if time and t<=time[-1]:
                continue
            time.append(t)
        return len(time)
