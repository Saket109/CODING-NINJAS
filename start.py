# ABOUT HASHMAPS : hashmaps are like dictionary   where we will use the key,value pairs

    # For storing keys,values we will use bucket array
    # keys -> hashfunction -> integer(index)
    # Hashfunction has two things  : 
                            # 1.) Hashcode
                            # 2.) Compression function

            # Compression function will compress the hashcode value within the bucket array size

        # So the compression function is (hashcode) % bucketsize
        
# Hashcode : for key integers we will can take hashcode as same integer
    # for key strings we can take ascii value of every char value with respect to p
    # like 10^2(ascii of c)+10^1(ascii of b)+10^0(ascii of a) for "abc"

    # But there is one problem called collision handling during compression function :
        # if we have 105 and 205 and bucket size is 20 then for both ()%size is same
    
    # IN PYTHON WE ALSO HAVE A INBUILT FUNCTION CALLED HASH() FOR GENERATING HASHCODE

    # Collision Handling  : we have 2 solutions :
            # 1.) closed hashing : using linked list or we can say by adding multiple integers to same index
            # 2.) open addressing : hi(a) = hf(a)+f(i) 
                # > linear probing : f(i) = i  -> f(0)=0
                # > quadratic probing : f(i) = i^2 -> f(0)=0 Also better solution
                # > doubling hashing : f(i) = i*hf'(i) -> f(0)=0

# But the best method for hashcode is closed hashing

# Now we will learn to access and insert in the hashmaps  :  
    # class map : buckets,bucket size,count
    # class mapnode : key,value,next

# we will do following things : 
     # insert(key,value)
     # delete(key)
     # search(key) -> return value

