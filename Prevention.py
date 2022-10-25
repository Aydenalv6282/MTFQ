import csv
import numpy
from matplotlib import pyplot as plt

SPY = {}
DPY = {}
given_years = 22
with open("Assets/Qualifying Phase Dataset.csv", "r") as QPD:
    QPDR = csv.reader(QPD)
    next(QPDR)
    for l in QPDR:
        y = int(l[0])-1999
        d = int(l[3])
        s = l[2]
        if s not in DPY:
            DPY.update({s: [d]})
        elif len(DPY[s])-1 < y:
            DPY[s].append(d)
        else:
            DPY[s][y]+=d
        if "suicide" in l[1]:
            if s not in SPY:
                SPY.update({s: [d]})
            elif len(SPY[s]) - 1 < y:
                SPY[s].append(d)
            else:
                SPY[s][y] += d

DPYM = {}
SPYM = {}
x_vals = [x+given_years-1 for x in range(int(input("Enter how many years the program will be active for: ")))]

for s in DPY:
    xs = [x for x in range(len(DPY[s]))]
    DPYM.update({s: numpy.polyfit(xs, DPY[s], 1)})
    xs = [x for x in range(len(SPY[s]))]
    SPYM.update({s: numpy.polyfit(xs, SPY[s], 1)})


inp = input("Enter the state to graph: ")
lives_saved = {}
for state in SPY:
    y_vals_s = []
    y_vals_sp = []
    y_vals_d = []
    y_vals_dp = []
    eqs = SPYM[state]
    eqd = DPYM[state]
    for x in x_vals:
        s = eqs[0]*x+eqs[1]
        d = eqd[0]*x+eqd[1]
        sp = s*(.92**(x-given_years+1))
        dp = (d-s)+sp
        y_vals_s.append(s)
        y_vals_sp.append(sp)
        y_vals_d.append(d)
        y_vals_dp.append(dp)
    if state == inp:
        px = [x for x in range(given_years)]
        plt.title(state)
        plt.plot(px, SPY[state], color="green")
        plt.plot(x_vals, y_vals_s, color="red")
        plt.plot(x_vals, y_vals_sp, color="blue")
        print(y_vals_s)
        print(y_vals_sp)
    lives_saved.update({state: sum(y_vals_d)-sum(y_vals_dp)})
    print(state, "saved", lives_saved[state], "lives.")

s = max(lives_saved, key=lambda x: lives_saved[x])
print(s, "had the most lives saved, with", lives_saved[s], "lives saved.")
print(SPYM[s])
plt.show()
