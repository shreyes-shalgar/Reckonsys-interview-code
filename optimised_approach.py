def max_area(height):
    area=0
    sh = sorted(height, reverse=True)

    for i in range(len(sh)-1):
        for j in range(i+1,len(sh)):

            min_wall = min(sh[i],sh[j])
            dist = abs(height.index(sh[i]) - height.index(sh[j]))

            temp_area = min_wall * dist
            print(min_wall, dist, temp_area)
            if temp_area > area: 
                area = temp_area
    return area
    



# Driver code
i=int(input())
heights=list(map(int, input().split()))
# print(height)
print(max_area(heights))





