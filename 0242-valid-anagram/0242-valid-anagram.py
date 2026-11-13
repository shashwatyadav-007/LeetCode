class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freq={}
        if len(s)!=len(t):
            return False
        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        for ch in t:
            if ((ch not in freq) or (freq[ch]==0)):
                return False
            freq[ch]-=1
        return True