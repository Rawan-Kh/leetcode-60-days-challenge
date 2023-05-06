class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t)):
            return False
        else:
            dt,ds={},{}
            for i in range(len(s)):
                dt[t[i]] = 1 + dt.get(t[i],0)
                ds[s[i]] = 1 + ds.get(s[i], 0)
                # print(ds)
            return dt == ds


        
