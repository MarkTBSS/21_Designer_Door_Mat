input = "7 21"
n, m = map(int, input.split())
print(n)
print(m)

# Top part
for i in range(1, n, 2): 
    print(i)
    print((i * '.|.').center(m, '-'))

# Mid part
print('WELCOME'.center(m, '-'))

# Bottom part 
for i in range(n-2, 0, -2): 
    print(i)
    print((i * '.|.').center(m, '-'))