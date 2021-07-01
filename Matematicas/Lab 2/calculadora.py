 
# number to its corresponding decimal
# number
  
# Function to convert any base number
# to its corresponding decimal number
def any_base_to_decimal(number, base):
      
    # calling the builtin function 
    # int(number, base) by passing 
    # two arguments in it number in
    # string form and base and store
    # the output value in temp
    temp = int(number, base)
      
    # printing the corresponding decimal
    # number
    print(temp)
  
# Driver's Code
if __name__ == '__main__' :
    hexadecimal_number = '1A'
    base = 16
    any_base_to_decimal(hexadecimal_number, base)