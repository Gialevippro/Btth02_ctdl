def max_sliding_window(nums, k):
    result = []
    
   
    iterations = len(nums) - k + 1
    
    for i in range(iterations):
        
        end_index = i + k
        
        
        sublist = nums[i:end_index]
        
       
        max_num = max(sublist)
        
        
        result.append(max_num)
    
    return result


num_list = [1, 3, -1, -3, 5, 3, 6, 7]
size_k = 3
print(max_sliding_window(num_list, size_k))
