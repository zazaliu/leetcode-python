class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return True if word.capitalize() == word or word.lower() == word or word.upper() == word else False
