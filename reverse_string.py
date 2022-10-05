
# input: my name is Binu.
# ouput: .uniB si eman ym

def reverse_string(input):
    final_str = ""
    for i in input[::-1]:
       final_str += i
    return final_str


print(reverse_string("my name is Binu."))