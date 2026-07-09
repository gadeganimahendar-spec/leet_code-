class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total=0
        for i  in digits:
           total=(total*10)+i
        total+=1
        t=[]
        for i in str(total):
            t.append(int(i))
        return t
        