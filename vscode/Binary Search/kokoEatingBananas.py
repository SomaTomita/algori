"""
Koko Eating Bananas
You are given an integer array piles where piles[i] is the number of bananas in the ith pile.
You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k.
Each hour, you may choose a pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.

Example 1:
Input: piles = [1,4,3,2], h = 9
Output: 2
Explanation: With an eating rate of 2, you can eat the bananas in 6 hours.
 With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.

Example 2:
Input: piles = [25,10,23,4], h = 4
Output: 25

Constraints:
1 <= piles.length <= 1,000
piles.length <= h <= 1,000,000
1 <= piles[i] <= 1,000,000,000
"""

from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        pass


# ------------------------------------------------------------
# ------------------------------------------------------------


# 総当たり解法（Brute Force）
class BruteForceSolution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k=1から始めて、条件を満たす最小のkを探す
        for k in range(1, max(piles) + 1):
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / k)

            if totalTime <= h:
                return k  # 最初に見つかったkが最小値

        return max(piles)  # 理論上ここには到達しない


print(BruteForceSolution().minEatingSpeed([1, 4, 3, 2], 9))

"""
総当たり解法の流れ: piles = [1, 4, 3, 2], h = 9

目標: h時間以内に全てのバナナを食べられる最小のk

========================================

k=1 を試す:
pile[0]=1: ceil(1/1) = 1時間
pile[1]=4: ceil(4/1) = 4時間  
pile[2]=3: ceil(3/1) = 3時間
pile[3]=2: ceil(2/1) = 2時間
totalTime = 1 + 4 + 3 + 2 = 10時間

判定: 10 <= 9 → False
k=1では時間オーバー、次を試す

========================================

k=2 を試す:
pile[0]=1: ceil(1/2) = ceil(0.5) = 1時間
pile[1]=4: ceil(4/2) = ceil(2.0) = 2時間
pile[2]=3: ceil(3/2) = ceil(1.5) = 2時間
pile[3]=2: ceil(2/2) = ceil(1.0) = 1時間
totalTime = 1 + 2 + 2 + 1 = 6時間

判定: 6 <= 9 → True ✓
k=2が最初に条件を満たす

結果: return 2
========================================
"""


print(BruteForceSolution().minEatingSpeed([25, 10, 23, 4], 4))

"""
総当たり解法の流れ: piles = [25, 10, 23, 4], h = 4

========================================

k=1 を試す:
pile[0]=25: ceil(25/1) = 25時間
pile[1]=10: ceil(10/1) = 10時間
pile[2]=23: ceil(23/1) = 23時間
pile[3]=4: ceil(4/1) = 4時間
totalTime = 25 + 10 + 23 + 4 = 62時間

判定: 62 <= 4 → False

========================================

k=2 を試す:
totalTime = ceil(25/2) + ceil(10/2) + ceil(23/2) + ceil(4/2)
          = 13 + 5 + 12 + 2 = 32時間

判定: 32 <= 4 → False

========================================

k=3 を試す:
totalTime = ceil(25/3) + ceil(10/3) + ceil(23/3) + ceil(4/3)
          = 9 + 4 + 8 + 2 = 23時間

判定: 23 <= 4 → False

========================================

... (中略: k=4~24まで全てFalse) ...

========================================

k=24 を試す:
totalTime = ceil(25/24) + ceil(10/24) + ceil(23/24) + ceil(4/24)
         = 2 + 1 + 1 + 1 = 5時間

判定: 5 <= 4 → False

========================================

k=25 を試す:
totalTime = ceil(25/25) + ceil(10/25) + ceil(23/25) + ceil(4/25)
         = 1 + 1 + 1 + 1 = 4時間

判定: 4 <= 4 → True ✓

結果: return 25
"""
