class Solution:
    def romanToInt(self, s: str) -> int:
        romans={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        lst=list(s)
        prev=0
        tot=0
        for i in lst:
            tot+=romans[i]
            if romans[i]>prev:
                tot-=2*prev
            prev=romans[i]
        return tot
                
                        
                    
                    
            