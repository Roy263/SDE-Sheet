class Solution:
    def generatePascals(self,numRows):
        pascals=[]
        for i in range(numRows):
            n=11**i
            pascals.append([int(d) for d in str(n)])
        return pascals
if __name__ == "__main__":
    print(Solution().generatePascals(5))