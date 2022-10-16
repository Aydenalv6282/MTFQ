import csv
from matplotlib import pyplot as plt
import numpy

epochs = 1000

dpy = []
with open("Assets/Qualifying Phase Dataset.csv", "r") as QPD:
    QPDR = csv.reader(QPD)
    next(QPDR)
    for l in QPDR:
        y = int(l[0])-1999
        d = int(l[3])
        if y <= len(dpy)-1:
            dpy[y] += d
        else:
            dpy.append(d)
x_vals = [t for t in range(len(dpy))]


def gradient_descent_sine(x_vals, y_vals, a_now, b_now, c_now, m_now, d_now):
    n = len(x_vals)
    a_gradient = 0
    b_gradient = 0
    c_gradient = 0
    m_gradient = 0
    d_gradient = 0
    a_gradient2 = 0
    b_gradient2 = 0
    c_gradient2 = 0
    m_gradient2 = 0
    d_gradient2 = 2/n+2
    # (Divide[1,n])*Sum[Power[\(40)y\(40)i\(41)-\(40)a*sin\(40)bx\(40)i\(41)+c\(41)+mx\(40)i\(41)+d\(41)\(41),2],{i,0,n}]
    for i in range(n):
        x = x_vals[i]
        y = y_vals[i]
        bx = b_now*x
        sbcx = numpy.sin(bx+c_now)
        cbcx = numpy.cos(bx+c_now)
        a_gradient += (-2/n)*(sbcx)*(y-(a_now*sbcx+d_now+m_now*x))
        a_gradient2 += (2/n)*(sbcx**2)
        b_gradient += (-2/n)*(a_now*cbcx*x)*(y-(a_now*sbcx+d_now+m_now*x))
        b_gradient2 += (2/n)*(a_now*(x**2))*(-a_now*(sbcx**2)+a_now*(cbcx**2)-d_now*sbcx-m_now*x*sbcx+y*sbcx)
        c_gradient += (-2/n)*(a_now*cbcx)*(y-(a_now*sbcx+d_now+m_now*x))
        c_gradient2 += (2/n)*(a_now)*(a_now*(cbcx**2)+y*sbcx-a_now*(sbcx**2)-d_now*sbcx-m_now*x*sbcx)
        m_gradient += (-2/n)*(x)*(y-(a_now*sbcx+d_now+m_now*x))
        m_gradient2 += (2/n)*(x**2)
        d_gradient += (-2/n)*(y-(a_now*sbcx+d_now+m_now*x))
    a = a_now - a_gradient * abs(1/a_gradient2)
    b = b_now - b_gradient * abs(1/b_gradient2)
    c = c_now - c_gradient * abs(1/c_gradient2)
    m = m_now - m_gradient * abs(1/m_gradient2)
    d = d_now - d_gradient * abs(1/d_gradient2)
    return a, b, c, m, d



print(dpy)
print(x_vals)

# Sine Variables
a, b, c, m, d = 0.1, 0.001, 0.1, 0.1, 3959964
for i in range(epochs):
    a, b, c, m, d = gradient_descent_sine(x_vals, dpy, a, b, c, m, d)
line_vals = []
sine_x_vals = []
sine_vals = []
sine_smooth_vals = []
for i in range(len(x_vals) * 100):
    x = i / 100
    sine_smooth_vals.append(a * numpy.sin(b * x + c) + m * x + d)
    sine_x_vals.append(x)

print(a, b, c, m, d)

plt.scatter(x_vals, dpy, color="green")
exp1 = numpy.polyfit(x_vals, dpy, 2)
exp2 = numpy.polyfit(x_vals, dpy, 3)
line = numpy.polyfit(x_vals, dpy, 1)
y_line = []
y_exp1 = []
y_exp2 = []
for x in x_vals:
    y_line.append(line[0]*x+line[1])
    y_exp1.append(exp1[0]*(x**2)+exp1[1]*x+exp1[2])
    y_exp2.append(exp2[0]*(x**3)+exp2[1]*(x**2)+exp2[2]*x+exp2[3])

print(line)
plt.plot(x_vals, y_exp1, color="blue")
plt.plot(x_vals, y_exp2, color="red")
plt.plot(x_vals, y_line, color="purple")
plt.plot(sine_x_vals, sine_smooth_vals, color="gold")
plt.show()

