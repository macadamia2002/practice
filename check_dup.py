def check_dup(nums):
  seen = set()
  for num in nums:
    if num in seen:
      return True
    seen.add(num)
  return False


# Test
t1 = [1,2,3,4,5,6]
assert check_dup(t1) == False, "should be False, no dups"

t2 = []
assert check_dup(t2) == False, "should be False, no dups"

t3 = [1,2,45,88,1]
assert check_dup(t3) == False, "should be True"
      
  
