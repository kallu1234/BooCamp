def ClimbStarirs(n):
    return Possible(0,n)

def Possible(curr_index,target):
    if curr_index==target:
        return 1
    if curr_index>target:
        return 0
    

    oneStep=Possible(curr_index+1,target)
    twoStep=Possible(curr_index+2,target)
    threeStep=Possible(curr_index+3,target)

    return oneStep+twoStep+threeStep

child=int(input("Enter no of stairs a :"))
ways=ClimbStarirs(child)
print(ways)


    