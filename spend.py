import csv
from matplotlib import pyplot as plt
import numpy
import math
import scipy

epochs = 1000

spy = []  # Suicides
hpy = []  # Heart disease deaths per year
dpy = []  # Total deaths yearly
years = []
with open("Assets/Qualifying Phase Dataset.csv", "r") as QPD:
    QPDR = csv.reader(QPD)
    next(QPDR)
    for l in QPDR:
        y = int(l[0]) - 1999
        d = int(l[3])
        if "suicide" in l[1]:
            if y <= len(spy)-1:
                spy[y] += d
            else:
                spy.append(d)
        elif "(I00-I09,I11,I13,I20-I51)" in l[1]:
            if y <= len(hpy)-1:
                hpy[y] += d
            else:
                hpy.append(d)
        if y <= len(dpy) - 1:
            dpy[y] += d
        else:
            dpy.append(d)
            years.append(y)

x_vals = [x/100 for x in range((22+5)*100)]
TOTAL = []
TOTAL_REMODELED = []



for t in x_vals:
    TD = 151839.397*numpy.sin(0.312*t-11.197)+8260.535*t+3793222
    p = t-22
    if p <= 0:
        p = 0
    S = 1670.079 * t + 50997.26086957
    HDD = 129178.216*numpy.sin(0.219*t-10.376)-13901.081*t+1490086
    SR = S*(.92)**p
    HDR = HDD*(.95)**p
    TOTAL.append(TD)
    TOTAL_REMODELED.append(TD-S-HDD+SR+HDR)


f, ax = plt.subplots(1)
ax.scatter(years, dpy, color="green", label="Raw Data")
ax.plot(x_vals, TOTAL, color="red")
ax.plot(x_vals[22*100:], TOTAL_REMODELED[22*100:], color="blue")

ax.set_ylim(ymin=0)
plt.legend(["Raw Data", "Death Model", "With Programs"], loc="lower left")
plt.xlabel("Years since 1999")
plt.ylabel("Deaths in the USA")
plt.title("Implementing Heart Disease & Suicide Prevention Programs (1999-2025)")

print(TOTAL[-1]-TOTAL_REMODELED[-1])

plt.show()

