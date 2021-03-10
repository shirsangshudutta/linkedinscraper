# Python3 code to demonstrate 
# Extracting specifix keys from dictionary 
# Using dictionary comprehension + items() 

# initializing dictionary 
test_dict = {'nikhil' : 1, "akash" : 2, 'akshat' : 3, 'manjeet' : 4} 

# printing original list 
print("The original dictionary : " + str(test_dict)) 

# Using dictionary comprehension + items() 
# Extracting specifix keys from dictionary 
res = {key: test_dict[key] for key in test_dict.keys() 
							& {'akshat', 'nikhil'}} 

# print result 
print("The filtered dictionary is : " + str(res)) 
