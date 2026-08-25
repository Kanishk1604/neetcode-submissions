class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize:
            return False
        hand.sort()

        freqMap = {}

        for h in hand:
            freqMap[h] = 1 + freqMap.get(h, 0)

        for n in hand:
            if freqMap[n]:
                for i in range(n, n + groupSize):
                    if i not in freqMap or not freqMap[i]:
                        return False
                    freqMap[i] -= 1
        
        return True