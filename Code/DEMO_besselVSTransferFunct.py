import numpy as np
import matplotlib.pyplot as plot
from scipy import signal

fig1, ax1 = plot.subplots()
b, a = signal.bessel(1,1.9,"high", analog=True,norm="mag")
w, h = signal.freqs(b,a)
ax1.plot(w,(abs(h)),color="blue")
b, a = signal.bessel(3,3.3,"low", analog=True,norm="mag")
w, h = signal.freqs(b,a)
ax1.plot(w,(abs(h)),color="red")
expr="x*(0.5*np.e**((-x**(2))/(2*(2.57**(2)))))"
x=np.logspace(-2,3,100)
y=((eval(expr)))
ax1.plot(x,y,color="black")
ax1.set_xlim(-2,10)
ax1.set_ylim(-1,1.5)

plot.show()