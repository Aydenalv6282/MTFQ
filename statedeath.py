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
        if l[2] == "Wyoming":
            y = int(l[0])-1999
            d = int(l[3])
            if y <= len(dpy)-1:
                dpy[y] += d
            else:
                dpy.append(d)
x_vals = [t for t in range(len(dpy))]
for d in dpy:
    print(d)

def sinusoid(x, a, b, c, m, d):
    return a*numpy.sin(b*x+c)+m*x+d


popt, pcov = scipy.optimize.curve_fit(sinusoid, x_vals[:-1], dpy[:-1], p0=[16800, 0.3, -1.1, 1130, 276000], maxfev=100000)
#
a, b, c, m, d = popt
print(a, b, c, m, d)
print("Deaths =",int(a),"* sin(", round(b, 3),"* x +", round(c, 3),")", int(m),"* x +", int(d))
# Sine Variables
line_vals = []
sine_x_vals = []
sine_vals = []
sine_smooth_vals = []
sine_smooth_vals1 = []
sine_eq_vals = []

#151839.397Sin (0.312t - 11.197) + 8260.535t + 3793222
for i in range((len(x_vals)*2) * 100):
    x = i / 100
    sine_smooth_vals.append(a*math.sin(b*x+c)+m*x+d)
    sine_x_vals.append(x)


vals = numpy.polyfit(x_vals, dpy, 1)

f, ax = plt.subplots(1)
ax.scatter(x_vals, dpy, color="green", label="Raw Data")
ax.plot(sine_x_vals, sine_smooth_vals, color="blue")
ax.legend(["Data", "Model Without Outlier", "Model With Outlier"], loc="lower left")
ax.set_ylim(ymin=0)
ax.set_xlim(xmax=40)

plt.xlabel("Years since 1999")
plt.ylabel("Deaths in the Florida")
plt.title("Deaths Per Year")

plt.show()
