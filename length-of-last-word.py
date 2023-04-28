class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list = s.split()
        last_len = len(list[-1])
        return(last_len)
        
#-------------
# memo notes
#does .split function put string in array (YES)
my_string = "hello world"
my_list = my_string.split()  # split the string using the default delimiter (space)
print(my_list)  # prints ['hello', 'world']
