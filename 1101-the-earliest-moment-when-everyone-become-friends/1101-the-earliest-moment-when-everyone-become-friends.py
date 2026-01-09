class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        friends = [ii for ii in range(n)]
        count = n
        def find(x, friends=friends):
            if x == friends[x]:
                return friends[x]
            friends[x] = find(friends[x])
            return friends[x]
        
        def union(x,y, count, friends=friends):
            root_x, root_y = find(x), find(y)
            
            if root_x!=root_y:
                friends[root_y] = root_x
                count-=1
            return count
        logs = sorted(logs)
        for t, x,y in logs:
            count = union(x,y, count)
            if count == 1:
                return t
        return -1