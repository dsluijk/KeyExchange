import random, math, time

def isPrime(p):
    if(p==2): return True
    if(not(p&1)): return False
    return pow(2,p-1,p)==1

def getPrime():
    isFound = False;
    while not isFound:
        r = random.randint(1000000, 9999999);
        if isPrime(r):
            return r;

def calcKey(g, pk, p):
	startTime = int(round(time.time() * 1000));
	key = long(g ** pk) % p
	endTime = int(round(time.time() * 1000)) - startTime;
	print "Key calculation took ", endTime, " milliseconds.";
	return key;