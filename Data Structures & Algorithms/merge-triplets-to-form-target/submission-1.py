class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t1 = False
        t2 = False
        t3 = False

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            if triplet[0] == target[0]:
                t1 = True
            if triplet[1] == target[1]:
                t2 = True
            if triplet[2] == target[2]:
                t3 = True
        

        return t1 and t2 and t3