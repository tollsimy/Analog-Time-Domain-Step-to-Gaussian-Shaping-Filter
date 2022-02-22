import numpy as np
import matplotlib.pyplot as plot
from scipy import signal

fig1, ax1 = plot.subplots()
b, a = signal.bessel(1,1.9,"high", analog=True,norm="mag")
w, h = signal.freqs(b,a)
ax1.semilogx(w,20*np.log10(abs(h)),color="blue")
b, a = signal.bessel(3,3.3,"low", analog=True,norm="mag")
w, h = signal.freqs(b,a)
ax1.semilogx(w,20*np.log10(abs(h)),color="red")
expr="x*(0.5*np.e**((-x**(2))/(2*(2.57**(2)))))"
x=np.logspace(-2,3,100)
y=(20*np.log10(eval(expr)))
ax1.semilogx(x,y,color="black")
ax1.set_xlim(0.01,100)
ax1.set_ylim(-50,1)

plot.show()
