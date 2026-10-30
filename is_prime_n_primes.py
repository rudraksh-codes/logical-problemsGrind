#modular
def is_prime(n):
    if n < 2 : 
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def primes_b_w(a,b):
    nums = []
    for i in range(max(2,a),b+1):
        if is_prime(i):
            nums.append(i)
    return nums


#combined
def primes(a, b):
    nums = []
    for n in range(a,b+1):
        if n<2:
            continue
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                break
        else : 
            nums.append(n)
    return(nums)

prime_nums = primes(-5,20)
print(prime_nums)