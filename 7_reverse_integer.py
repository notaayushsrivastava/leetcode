class Solution:
    def reverse(self, x: int) -> int:
        target = int(str(x)[::-1]) if not x<0 else int('-'+str(abs(x))[::-1])
        
        return 0 if target<-1 * 2**31 or target>2**31-1 else target