class Solution:
  def resultArray(self, nums: list[int], k: int) -> list[int]:
    a = [0] * k
    d = [0] * k

    for x in nums:
      n = [0] * k
      m = x % k
      n[m] = 1
      for i in range(k):
        nm = (i * m) % k
        n[nm] += d[i]
      for i in range(k):
        a[i] += n[i]
      d = n

    return a