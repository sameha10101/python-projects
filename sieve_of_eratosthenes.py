"""Uses the Sieve of Eratosthenes to list primes till n."""
def eratosthenes_till_n(x):
    list_of_numbers= list(range(2,1+x))
    list_of_divisors= [2]
    #start by removing the multiples of 2.
    while len(list_of_numbers) != 0:
        for n in list_of_numbers:
            if n%list_of_divisors[-1]==0:
                list_of_numbers.remove(n)
        """after all the multiples of all primes till p_i are removed,
        the first remaining element in the list of numbers is
        the prime next to p_i: i.e. p_{i+1}."""
        
        """add p_{i+1} to the list and start to remove multiples of p_{i+1}."""
        if len(list_of_numbers) != 0:
            list_of_divisors.append(list_of_numbers[0])
    return list_of_divisors

print(eratosthenes_till_n(1000))
