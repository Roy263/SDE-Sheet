'''
Given an m*n city. There is a virus spread in the city. 
each cell can have one of three values: - > 0 represents emptycell[no person] 
-> 1 represents a people unaffected by the virus 
-> 2 represents virus affected person 
-> every hour, any unaffected person 4-directionally adjacent to an affected person becomes affected. 
Return the minimum no of hours that must elapse until no person is unaffected by the virus. 
If this is impossible return -1(not possible to affect all the people). return a python code for this 
'''

class Solution():
    def calculate_hours(self,grid):
        rows,cols=len(grid),len(grid[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        affected_persons=[]
        unaffected=0
        for i in range(rows):
            for j in range(cols):
                if(grid[i][j]==2):
                    affected_persons.append((i,j))
                if(grid[i][j]==1):
                    unaffected+=1
        hours=0
        while(affected_persons):
            current_persons=affected_persons
            print(current_persons)
            if(unaffected==0):
                return hours
            affected_persons=[]
            for i,j in current_persons:
                for dx,dy in directions:
                    x,y=i+dx,j+dy
                    if(0<=x<rows) and (0<=y<cols) and grid[x][y]==1:
                        grid[x][y]=2
                        unaffected-=1
                        affected_persons.append((x,y))
            print("new affected:",affected_persons)
            hours+=1
        if(unaffected>0):
            return -1

if __name__=="__main__":
    grid=[
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ]

    obj=Solution()
    print("hours: ",obj.calculate_hours(grid))