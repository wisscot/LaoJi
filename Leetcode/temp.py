
def myrange(start):
    while True:
        yield start
        start += 1

for num in myrange(1):
    print(num)

