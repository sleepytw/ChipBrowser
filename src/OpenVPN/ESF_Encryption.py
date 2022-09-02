'''
The private key d is derived from the following formula:
d = (k*Φ(n) + 1) / e for some integer k

At step 5 instead of doing what Eddie did, I'd suggest for you to use this formula instead which is basically the same thing.
The little trick here is that k has to be such an integer, that k*Φ(n) + 1%e=0
(% stands for the mathematical mod)

So let us try and find k for the above example where Φ(n)=6 and e=5
if k=1,  1*6+1%e = 2
if k=2,  2*6+1%e = 3
if k=3,  3*6+1%e = 4
if k=4,  4*6+1%e = 0
if k=5,  5*6+1%e = 1
if k=6,  6*6+1%e = 2
if k=7,  7*6+1%e = 3
if k=8,  8*6+1%e = 4
if k=9,  9*6+1%e = 0
So k=9 is our answer. Notice that we did not stop at k=4, because that would give us d=5
and the idea here is that d and e cannot be the same.
Hence, for k=9
d = (k*Φ(n) + 1) / e = 11.
'''

def Φ(n) -> ...: return
