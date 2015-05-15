import random
import math

def fermat(n,a):
    x = fastermod(a,(n-1),n)
    if(x!=(1%n)):
        return True
    return False

def millerRabin(n,a):
    k,m =  decompose(n)
    x = fastermod(a,m,n)
    if(x==1%n):
        return False
    for j in range(0,k-1):
        if(x==-1%n):
            return False
        else:
            x = fastermod(x,2,n)
    return True

def decompose(n):
    exponentOfTwo = 0
    while n % 2 == 0:
        n = n/2
        exponentOfTwo += 1
    return exponentOfTwo, n

def fastermod(factor,power,modulus):
    result = 1;
    while(power > 0):
        if (power % 2 == 1):    
            result = (result*factor) % modulus
            power = power-1

        power = power/2;
        factor = (factor*factor)%modulus
    return result


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

def runFermat():
    witnesses = []
    liars = []
    #for i in range(0,len(numbers)):
    for i in range(0,len(numbers)):
        tempWitness=0
        tempLiar=0
        for a in range(2,int(numbers[i])):
            bol = fermat(numbers[i],a)
            if(bol and tempWitness==0):
                tempWitness=a
            elif(not(bol) and tempLiar==0):
                tempLiar=a
            if(tempLiar!=0 and tempWitness!=0):
                break
        witnesses.append(int(tempWitness))
        liars.append(int(tempLiar))
    #print("Witnesses",witnesses,len(witnesses))
    #print("liars",liars,len(liars))
    print "Fermat"
    printNice(witnesses,liars)


def runMillerRabin():

    witnesses = []
    liars = []
    for i in range(0,len(numbers)):
        tempLiar=0
        tempWitness=0
        for a in range(1,int(numbers[i])):
            bol = millerRabin(numbers[i],a)
            if(bol and tempWitness==0):
                tempWitness=a
            elif(not(bol) and tempLiar==0):
                tempLiar=a
            if(tempLiar!=0 and tempWitness!=0):
                break
        witnesses.append(int(tempWitness))
        liars.append(int(tempLiar))
    #print("witnesses",witnesses,len(witnesses))
    #print("liars",liars,len(liars))
    print "Miller-Rabin"
    printNice(witnesses,liars)

def printNice(witnesses,liars):
    for i in range(0,len(numbers)):
        print "NUMBER: ",numbers[i] 
        print "Witnes: ", witnesses[i]
        print "Liar: ",liars[i]

def main():
    runFermat()
    runMillerRabin()