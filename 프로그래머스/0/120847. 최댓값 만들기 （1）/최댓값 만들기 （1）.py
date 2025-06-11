def solution(numbers):
    
    max1 = max2 = -1
    
    for x in numbers:
        if x > max1:          
            max2 = max1      
            max1 = x          
        elif x > max2:       
            max2 = x          
    
    return max1 * max2