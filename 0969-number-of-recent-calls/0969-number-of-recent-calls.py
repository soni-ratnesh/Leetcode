class RecentCounter:

    def __init__(self):
        self.queue = []
        self.point = 0

    def ping(self, t: int) -> int:
        self.queue.append(t)

        while (t-self.queue[self.point]) >3000:
            self.point+=1
            continue

        res = len(self.queue) - self.point 

        return res



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)