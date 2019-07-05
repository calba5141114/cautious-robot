
def sum_limit(arr, limit):
  dict_map = {}
  for i in range(len(arr)):
    mist_sum = limit - arr[i]
    if mist_sum in dict_map:
      return [mist_sum, arr[i]]
    dict_map[arr[i]] = arr[i]
  return None

print(sum_limit([1,2,3,4,5,6,7], 30))
