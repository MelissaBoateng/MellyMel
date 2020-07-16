from dot import*
''' Testing using N=10 with random variables, The sample class of the random library allows the function get randomized sample of size N'''

N = 10
ListA= sample(range(1,1000),N)
ListB= sample(range(1,1000),N)
Dotproduct(N,ListA,ListB)

N = 10
ListA= sample(range(1,1000),N)
ListB= sample(range(1,1000),N)
Dotproduct(N,ListA,ListB)
