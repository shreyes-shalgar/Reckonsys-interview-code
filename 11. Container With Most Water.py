def max_area(height):
    area=0
    
    # Iterate through all possible combinations
    for i in range(len(height)):
        for j in range(i+1,len(height)):

            # calculate the min height out of the two walls
            dist = min(height[i],height[j]) 

            # calculate the current area made by the two walls
            temp_area = dist * (j-i) 

            # check for maximum area  
            if temp_area > area: 
                area = temp_area
    return area

# Driver code
i=int(input())
heights=list(map(int, input().split()))
# print(height)
print(max_area(heights))
