def sum_num(nums):
  total = 0
  for num in nums:
    total += num
  return total
  
# Test
t1 = [1,2,3,4,5]
assert sum_num(t1) == 15, "should sum to 15"

t2 = []
assert sum_num(t2) == 0, "should sum to 0"

t3 = [1]
assert sum_num(t3) == 1, "should sum to 1"
