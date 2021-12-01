#How many measurements are larger than the previous measurement?
with open ("input.txt") as f:
    lines = f.read().splitlines()

for i in lines:
    difference = lines[(i)] - lines[(i-1)]
    print(difference)
