# Alice has some number of cards, and she wants to rearrange the cards into groups
# so that each group is of size groupSize,
# and consists of groupSize consecutive cards.
#
# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize,
# return true if she can rearrange the cards, or false otherwise.
#
# Example 1:
# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
#
# Example 2:
# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.
from typing import List
import heapq


class Solution:
    # brute force
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        card_count = {}
        cards = []
        for n in hand:
            if n not in card_count:
                cards.append(n)
            card_count[n] = card_count.get(n, 0) + 1

        # distribute cards, start from the smallest card
        num_of_group = 0
        max_groups = len(hand) // groupSize
        while num_of_group < max_groups and card_count:
            count = 0
            prev = cards[0]
            for n in cards:
                if n in card_count:
                    if count >= 1 and n - 1 != prev:
                        return False
                    count += 1
                    card_count[n] -= 1
                    if card_count[n] == 0:
                        card_count.pop(n)
                    prev = n
                if count == groupSize:
                    num_of_group += 1
                    break
        return num_of_group == max_groups

    # 更優解
    def isNStraightHandV2(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        cardMap = {}
        for n in hand:
            cardMap[n] = cardMap.get(n, 0) + 1
        minHeap = list(cardMap.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]  # start from the smallest card
            for i in range(first, first + groupSize):  # 找連續的牌
                if i not in cardMap:
                    return False
                cardMap[i] -= 1
                if cardMap[i] == 0:
                    if i != minHeap[0]:  # 會導致無法連續
                        return False
                    heapq.heappop(minHeap)
        return True


sol = Solution()
h = [1, 2, 3, 6, 2, 3, 4, 7, 8]
h1 = [1, 2, 3, 4, 5]
print(sol.isNStraightHandV2(h, 3))
print(sol.isNStraightHandV2(h1, 4))
print(sol.isNStraightHandV2([1, 5], 2))
