	def sequentialSearch(arr, item):
	    pos = 0
      found = False
	
	    while pos < len(arr) and not found:
	        if arr[pos] == item:
	            found = True
	        else:
	            pos = pos+1
	
        return found
