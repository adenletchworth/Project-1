# keep splitting list
# call function on sublists too solve recursively 
# merge fully splitted sublists

def mergeSort(list):
    if len(list) > 1: # make sure list is not empty
        left = list[:len(list)//2] # creates subarray starting from middle going left
        right = list[len(list)//2:] # creates subarray starting from middle going right
    
        mergeSort(left) # recursively calls left subarray
        mergeSort(right) # recursively calls right subarray

        l, r, m = 0, 0, 0 # defining left,right and merged pointers
        
        while r < len(right) and l < len(left): #check if we have reached the end of our substrings
            if left[l] < right[r]: #check if left element is less than right element
                list[m] = left[l] # if so set merged element to the left element
                l+=1 # increment left pointer
            else:
                list[m] = right[r] #if our left element is greater or equal to our right element we need to set our merged pointer there
                r+=1 #increment right pointer
            m+=1 #increment merged pointer
        
        while l < len(left): #if anything isnt merged on left merge it
            list[m] = left[l]
            l+=1
            m+=1
        
        while r < len(right): #if anything isnt merged on right merge it
            list[m] = right[r]
            r+=1
            m+=1
    return list

test = [10,1,4,7,6,5,8,9,3,2]
mergeSort(test)
print(test)