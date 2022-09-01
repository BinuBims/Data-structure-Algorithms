x = ['w','x','y','r']
y = ['a','b','r']

# brute force:
# have two loops and check if elements in x exsist in elements in y
# time complex = o(a*b)

# def check_ele(x,y):
#   for i in x:
#     for j in y:
#       print(i,j)
#       if i == j:
#         return True
#   return False

# print(check_ele(x,y))

###########################################################################################################################################################

# more efficient code:
# for loop to create a dict
# then another for loop to check if the dict contains elements from second array
# time complexity = o(a+b)

def check_ele(x,y):
  element_dict = {}
  for i in x:
    if i not in element_dict:
      element_dict[i] = 0
    element_dict[i] += 1

  for j in y:
    if j in element_dict:
      return True
  return False

print(check_ele(x,y))