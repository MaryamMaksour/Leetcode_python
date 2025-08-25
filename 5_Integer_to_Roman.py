'''
Linke:
 

Runtime
134 ms, 5.06% Beats  

Memory
12.29  MB, 99.04% Beats   

'''

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        frq =   [ 1,   4,    5,  9,   10,  40,   50,   90,  100, 400,   500, 900,  1000]
        frq_c = ['I', 'IV' ,'V','IX', 'X', 'XL', 'L', 'XC', 'C', 'CD' , 'D', 'CM', 'M']

        c = 0
        ans = str()

    
        while num > 0:

            for i in range(12,-1, -1):
                if(num >= frq[i]):
                    print(num)
                    print(frq[i])
                    num -= frq[i]
                    ans += frq_c[i]
                    break

        return ans

