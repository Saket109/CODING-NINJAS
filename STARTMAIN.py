# Bitwise operators :

# to find the ith bit of a number first right shift the 1 to i-1 times and take and with the 
# number of this if it gives zero then the bit is 0 and if it gives any result then bit is 1

# and also (1<<(i-1)) is called mask

#   also if the question is set the ith bit then just take or of mask and the number

# If the question is to reset the ith bit then make a mask and take and with the number
# So what will be the mask is the 1111110111 take zero at that place whose bit you want to reset
# now this mask will come by complimenting the 000000001000 !(1<<(i-1)) 

#   QUESTION : FIND THE POSITON OF THE RIGHT MOST SET BIT 
#       ANS : take n&(-n) --> this will give you result like this 0000100 --> 4

#   
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
