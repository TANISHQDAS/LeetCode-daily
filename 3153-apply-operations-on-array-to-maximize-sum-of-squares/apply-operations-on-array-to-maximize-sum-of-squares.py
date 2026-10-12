
class Solution:
  def maxSum(self, nums: list[int], k: int) -> int:
    mod = 10**9 + 7
    a = [0] * len(nums)
    b = [0] * 30
    for x in nums:
      for i in range(30):
        if x >> i & 1:
          a[b[i]] |= 1 << i
          b[i] += 1
    s = 0
    for i in range(k):
      s = (s + a[i]**2) % mod
    return s
