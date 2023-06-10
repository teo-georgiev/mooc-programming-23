# Write your solution here
def factorials(n: int): 
    
    # MODEL SOLUTION
    # result = {}
    # result[1] = 1
    # for i in range(2, n+1):
    #     result[i] = result[i - 1] * i
    # return result


    dict = {}
    i = n

    for n in range(n, 0, -1):  
        fact = 1
        for i in range(0, n, 1): 
            fact = fact * (n-i)
        dict[n] = fact
    
    return dict    

if __name__ == "__main__": 
    k = factorials(5)

    print(k[1])
    print(k[3])
    print(k[5])