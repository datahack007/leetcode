class Solution(object):
    def countAndSay(self, n):
        #111221
        if n == 1:
           return "1"
        prev = self.countAndSay(n-1)
        res =""
        count = 1
        for i in range(len(prev)):
            if i==len(prev)-1 or prev[i] != prev[i+1]:
                res += str(count) + prev[i]
                count = 1
            else:
                count += 1
        return res
        

if __name__ == "__main__":
    a = Solution()
    x = a.countAndSay(5)
    print(x)
    pass