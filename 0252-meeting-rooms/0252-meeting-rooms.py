class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals)<2:
            return True
        
        intervals.sort()

        for ii in range(1, len(intervals)):
            if intervals[ii-1][1]>intervals[ii][0]:
                return False
        return True

        
        