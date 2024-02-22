class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        has_outgoing = set()
        for i in range(len(paths)):
            has_outgoing.add(paths[i][0])
        
        for i in range(len(paths)):
            candidate = paths[i][1]
            if candidate not in has_outgoing:
                return candidate
        
        return ""
