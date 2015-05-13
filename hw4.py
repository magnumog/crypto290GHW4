import random
print('hi')

def fermat(n):
    witness = []
    liar = []
    for i in range(0,len(n)):
        a = random.randint(2,n-2)
        x = (a**(n-1))%n
        if(x!=(1%n)):
            witness.add(n)
        else:
            liar.add(n)
    return witness, liar

numbers = [41041, 62745, 63973, 75361, 101101, 126217, 172081, 188461, 278545, 340561, 449065, 552721, 656601, 658801, 670033, 748657, 838201, 852841, 997633, 1033669, 1082809, 1569457, 1773289, 2100901, 2113921, 2433601, 2455921]

print(fermat(numbers))
       
