import random
import math

def fermat(n):
    #print('n',n)
    witness = 0
    liar = 0
    #a = random.randint(2,n-2)
    for a in range(2,int(math.sqrt(n))):
        x = (a**(n-1))%n
        #print('x',x)
        if(x!=(1%n)):
            if(witness==0 or x<witness):
                witness = x
        else:
            if(liar==0 or x<liar):
                liar = x
    return witness, liar

def millerRabin(n):
    witness = 0
    liar = 0
    k,m=decompose(n)
    a = random.randint(1,n-1)
    x = (a**m)%n
    if((x==1 and (witness==0 or witness>x)):
        witness=x
        if(witness==0):
            for j in range(0,k-1):
                if(x==-1%n and (witness==0 or witness>x)):
                    witness=x**2%n
    elif(witness==0 and x<liar):
        liar = x
    return witness, liar

def decompose(n):
    return 0


numbers = []
numbers.append(41041)
numbers.append(62745)
numbers.append(63973)
numbers.append(75361)
numbers.append(101101)
numbers.append(126217)
numbers.append(172081)
numbers.append(188461)
numbers.append(278545)
numbers.append(340561)
numbers.append(449065)
numbers.append(552721)
numbers.append(656601)
numbers.append(658801)
numbers.append(670033)
numbers.append(748657)
numbers.append(838201)
numbers.append(852841)
numbers.append(997633)
numbers.append(1033669)
numbers.append(1082809)
numbers.append(1569457)
numbers.append(1773289)
numbers.append(2100901)
numbers.append(2113921)
numbers.append(2433601)
numbers.append(2455921)

def main():
    #witness, liar = fermat(143)
    for i in range(0, len(numbers)):
        witness, liar = fermat(numbers[i])
        print("witness", int(witness))
        print("liar", int(liar))

def foo():
    print(math.sqrt(numbers[0]))
