#!/usr/bin/python3.3
limit = 4000000
fibonacci = [1,2]
ans = 0

while fibonacci[len(fibonacci) - 1] + fibonacci[len(fibonacci) - 2] < limit:
    fibonacci.append(fibonacci[len(fibonacci) - 2] + fibonacci[len(fibonacci) - 1])

for n in fibonacci:
    if n%2 ==0:
        ans += n

print(ans)
