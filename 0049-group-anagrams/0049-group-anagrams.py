from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def get_cha_vector(string):
            vector = [0]*27
            for s in string:
                idx = ord(s)-ord('a')
                vector[idx] +=1
            return tuple(vector)
        count_dict = defaultdict(list)
        
        for s in strs:
            key = get_cha_vector(s)
            count_dict[key].append(s)
        
        return list(count_dict.values())