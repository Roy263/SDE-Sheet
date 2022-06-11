class Solution(object):
    def generatePascals(self, numRows):
        pascals=[]
        for i in range(numRows):
            pascals.append([])
            pascals[i].append(1)
            for j in range(1,i):
                pascals[i].append(pascals[i-1][j-1]+pascals[i-1][j])
            if(i>0):
                pascals[i].append(1)
        return pascals

if __name__ == "__main__":
    print(Solution().generatePascals(5))