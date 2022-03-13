# Program to display the Fibonacci sequence up to n-th term

# nterms = int(input("How many terms? "))
nterms = 10

# first two terms
n1, n2 = 0, 1
count = 0
x,y = [],[]

# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
# generate fibonacci sequence
else:
    while count < nterms:
        try:
            print((count, n1, n2/n1))
            x.append(count)
            y.append(n2/n1)
        except:
            pass
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,5))

# line 1 points
# plotting the line 1 points
plt.plot(x, y, label = "Fibonacci graph")

# line 2 points
f = [1.618033988749895]*(count-1)
# plotting the line 2 points
plt.plot(x, f, label = "1.618033988749895")

# naming the x axis
plt.xlabel('count')
# naming the y axis
plt.ylabel('n2 / n1')
# giving a title to my graph
plt.title('Golden Ratio!')

plt.grid()
# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()
png_file = '1.6180339.png'
fig.savefig(png_file)
