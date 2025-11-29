def maximizeSum(arr, k):
   
    arr.sort()

    
    for i in range(len(arr)):
        
        if k == 0:
            break
        
        
        if arr[i] < 0:
            arr[i] = -arr[i]
            k -= 1
        else:
          
            break

   
    current_sum = sum(arr)
    
  
    if k % 2 == 1:
       
        min_val = min(arr)
        
     
        current_sum -= 2 * min_val

    return current_sum