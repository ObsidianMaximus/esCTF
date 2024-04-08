#!/usr/bin/env python3

from Crypto.Util.number import bytes_to_long, getPrime
import sympy

flag=b'--REDACTED--'

def get_noice_primes():
	p = getPrime(1024)
	q_base = int(bin(p)[3:],2)
	q = sympy.nextprime(q_base)
	return p,q 

p,q = get_noice_primes()
n=p*q
phi = (p-1)*(q-1)
e = 65537

m = bytes_to_long(flag)
ct = pow(m,e,n)

print("n =",n)
print("e =",e)
print("ct =",ct)


