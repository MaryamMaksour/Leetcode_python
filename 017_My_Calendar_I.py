''' 

Linke:  https://leetcode.com/problems/my-calendar-i/

Runtime 
56 ms, Beats 66.16%

Memory 
18.89 MB, Beats  28.29%

'''

class MyCalendar:



    def __init__(self):
        self.calender = [] 
        

    def book(self, startTime: int, endTime: int) -> bool:

        calender = self.calender

        ls = [startTime, endTime]

        def find_start( ):
            
            l =  -1
            r = len(calender)
            ans = -1

            while l + 1 < r:
                mid = l + int((r - l)/2)

                if ls[1] <= calender[mid][0]:
                    r = mid
                    ans = mid
                else:
                    l = mid 

            # add to the end

            if(ans == -1 and ls[0] >= calender[-1][1]):
                ans = len(calender)


            return ans

         

        # claender is empty
        if(len(calender) == 0):
            calender.insert(0, ls)
            return True

        idx =  find_start()

     

        # can not added
        if( idx == -1 ):
            return False


        # add to the begain 
        elif (idx == 0):
            if  ls[1] <= calender[idx][0]:
                calender.insert(idx, ls)
                return True
            else: 
                return False

        # added to the end
        elif (idx == len(self.calender)):

            if calender[idx - 1][1] <= ls[0]:
                calender.insert(idx, ls)
                return True

            else: 
                return False

        
        # added to the middel 
        elif (calender[idx-1][1] <= ls[0] and ls[1] <= calender[idx][0]):
            calender.insert(idx, ls)
            return True
    
    
        return False


     
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
