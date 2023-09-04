arr1 = []
class Solution:
        
    def reverseString(self, s: list[str]) -> None:
      global arr1
      if(len(s)>0):
          arr1.append(s[-1])
          s.pop(-1)
          self.reverseString(s)
      else:
          s[:] = arr1
          arr1 = []
