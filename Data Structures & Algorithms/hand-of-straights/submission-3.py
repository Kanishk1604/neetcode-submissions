class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize:
            return False

        hand.sort()
        counter = Counter(hand)

        for i in range(len(hand)):
            if counter[hand[i]]:
                for card in range(hand[i], hand[i] + groupSize):
                    if not counter[card]:
                        return False
                    counter[card] -= 1
        
        return True
