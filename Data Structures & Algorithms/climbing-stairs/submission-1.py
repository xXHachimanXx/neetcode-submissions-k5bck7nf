class Solution:
    def climbStairs(self, n: int) -> int:
        '''

        4


        1 1 2

                (1, 2)
           (1, 2)    (1', 2)
       (1)  

        '''

        if n == 0:
            return 0
        
        memo = {}

        def count_distinct_ways(steps):
            
            if steps == n:
                return 1

            if steps > n:
                return 0
            
            if steps in memo and memo[steps]:
                return memo[steps]
            
            memo[steps] = count_distinct_ways(steps + 1) + count_distinct_ways(steps + 2)
            return memo[steps]


        
        return count_distinct_ways(0)

        