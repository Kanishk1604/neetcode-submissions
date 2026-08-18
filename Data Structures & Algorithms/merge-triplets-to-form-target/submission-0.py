class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #sort triplets in desc
        #if all a b c are <= target a b c
        # it can be a possible triplet
        #[5, 8, 9],[5, 2, 1],[3,4,1] [4,2,8] [2,7,9] t =[5, 4, 8]
        #greedy - ick min of trips start with target[0]
        # then compare adj trips
        #if any max b or c > taret[1] [2] -> dont append 
        #if "res[-1]" == "target"

        res = [0, 0, 0]

        for trp in triplets:
            if (trp[0] <= target[0] and trp[1] <= target[1] and trp[2] <= target[2]):
                res[0] = max(res[0],trp[0])
                res[1] = max(res[1],trp[1])
                res[2] = max(res[2],trp[2])

        return res == target
            
            