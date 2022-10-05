# input:[0,3,4,31],[4,6,30]
# ouput: [0,3,4,4,6,30,31]
def merge_sorted_arrays(list1,list2):
    list1.extend(list2)
    return sorted(list1)

print(merge_sorted_arrays([0,3,4,31],[4,6,30]))
