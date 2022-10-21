import csv
from matplotlib import pyplot as plt
import numpy
import math
import scipy

epochs = 1000

dpy = []
with open("Assets/Qualifying Phase Dataset.csv", "r") as QPD:
    QPDR = csv.reader(QPD)
    next(QPDR)
    for l in QPDR:
        if "suicide" in l[1]:
            y = int(l[0])-1999
            d = int(l[3])
            if y <= len(dpy)-1:
                dpy[y] += d
            else:
                dpy.append(d)
x_vals = [t for t in range(len(dpy))]

print(numpy.std(dpy))
def sinusoid(x, a, b, c, m, d):
    return a*numpy.sin(b*x+c)+m*x+d

popt, pcov = scipy.optimize.curve_fit(sinusoid, x_vals, dpy, p0=[0, 0, 0, 0, 0])

print(dpy)
print(x_vals)

# Sine Variables
a, b, c, m, d = popt
line_vals = []
sine_x_vals = []
sine_vals = []
sine_smooth_vals = []
sine_smooth_vals1 = []
sine_eq_vals = []


for i in range(len(x_vals) * 100):
    x = i / 100
    sine_smooth_vals.append(a * math.sin(b * x + c) + m * x + d)
    sine_x_vals.append(x)


vals = numpy.polyfit(x_vals, dpy, 1)

plt.scatter(x_vals, dpy, color="green", label="Raw Data")

plt.plot(sine_x_vals, sine_smooth_vals, color="red")


plt.legend(["Data", "Model"])

plt.xlabel("Years since 1999")
plt.ylabel("Deaths in the USA")
plt.title("Deaths Per Year From Heart Disease (1999-2020)")





plt.show()

