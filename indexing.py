# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

number = "1234-5678-9101-11213"
# print(number[0])  > 1
# print(number[:4])  > 1234
# print(number[5:9])   > 5678 
# print(number[5:])    > 5678-9101-11213
# print(number[-1])    > 3  the last digit
# print(number[::3])     > 146-011
last_digits = number[-5:]
print(last_digits) 

backward_number = number[::-1]
print(backward_number) 