def obtainweights(n, bias, x1, x2, classification, wt):
    for _ in range(1000):
        for i in range(n):
            x1x2 = (wt[0] * x1[i] + bias) + (wt[1] * x2[i] + bias)
            if x1x2 > 0:
                y = 1
            else:
                y = 0
            error = classification[i] - y
            if error != 0:
                wt[0] += 0.1 * error * x1[i]
                wt[1] += 0.1 * error * x2[i]


n = int(input("Enter number of x1 and x2 elements: "))
x1 = []
for i in range(n):
    x1.append(float(input("Enter the elements of x1:")))

x2 = []
for i in range(n):
    x2.append(float(input("Enter elements of x2: ")))

wt = [0.0, 0.0]

classification = []
for i in range(n):
    classification.append(float(input("enter classification: ")))

obtainweights(n, 1, x1, x2, classification, wt)
print("Weights: ")
for i in range(2):
    print(wt[i])
