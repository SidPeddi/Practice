class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        char_counts = Counter(magazine)
        balloon_counts = Counter(ransomNote)

        return (min(char_counts[char] // balloon_counts[char] for char in balloon_counts)) != 0   