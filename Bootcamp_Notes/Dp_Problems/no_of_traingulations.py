class Solution:
    #same as catelon no
    def findtri(self,n):
        #return the nth ways of traingulation
        return self.nthTri(n,{})
    def nthTri(self,n,memo):
        n=n-2
        if n<=1:
            return 1
       
        #create a key 
        key=n
        if key in memo:
            return memo[key]
        ways=0
        for i in range(0,n):
              ways+= self.nthTri(i,memo) * self.nthTri(n-i-1,memo)
        
        memo[key]=ways
        return memo[key]
        
s=Solution()
n=int(input())
print(s.findTri(n))

#how we can find
#ex-> n->2 so if we have 2 points then we are unable to make traingle  so , bydefault we have to return 1
#ex->n->3 so here also we have 3 points and we are able to make 1 triangle 
#ex n->4 so here are 2 possible ways to make triangle so return 2
#ex n->5 so here are 5 possible ways to make traingle so return 5


#So i used the technique of nth  Catalan no  here 
#n->1 return 1
#n->0 return 1 catalan of 1 and 0 is 1 
# to find catelan of n->2 we have one formuala c0c1 +c1c0
#n->3 formula will be c0c2+c1c1+c2c0  
#n->4 formula will be c0c3+c1c2+c2c1+c3c0
