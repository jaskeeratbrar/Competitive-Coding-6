## T(C): O(n!)
## S(C): O(n)

class Solution:
    def countArrangement(self, n: int) -> int:

        #helper functio
        def count(position, available):
            if position == 1:
                return 1
            
            #global counter
            valid_count = 0

            
            for i in range(1, n + 1):

                if available[i] and (i % position == 0 or position % i == 0):

                    ## mark tracking list position as false, indicating beauty check pass
                    available[i] = False

                    ##updatinng counter
                    valid_count += count(position - 1, available)
                    
                    available[i] = True
            
            return valid_count
        
        #  availability list where all numbers from 1 to n are available
        available = [True]  * (n + 1)


        return count(n, available)
