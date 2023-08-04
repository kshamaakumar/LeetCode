def maxArea(self, height: List[int]) -> int:
    i = 0
    j = len(height) - 1
    area = 0
    curr_area = 1

    while i < j:
        minHeight = min(height[i],height[j])
        curr_area = minHeight * (j - i)
        area = max(area,curr_area)

        if height[i] < height[j]:
            i += 1
        
        else:
            j -= 1
        
    return area