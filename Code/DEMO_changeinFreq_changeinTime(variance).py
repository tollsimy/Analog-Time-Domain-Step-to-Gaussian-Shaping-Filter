import numpy as np
import matplotlib.pyplot as plot
from scipy import signal

#setting plots
fig1, ax1 = plot.subplots()
fig2, ax2 = plot.subplots()
ax1.set_title("Frequency response")
ax1.set_xlabel("Angular frequency [rad/s]")
ax1.set_ylabel("Gain [dB]")
ax2.set_title("Impulse response")
ax2.set_xlabel("Time [S]")
ax1.set_xlim(0.1,1000)
ax1.set_ylim(-80,1)

#gaussian with variance 2.57
expr="x*(0.5*np.e**((-x**(2))/(2*(2.57**(2)))))"
x=np.logspace(-1,3,1000)
y=20*np.log10(eval(expr))
ax1.semilogx(x,y,color="silver")

#gaussian with larger variance (25.7)
expr="x*(0.05*np.e**((-x**(2))/(2*(25.7**(2)))))"
x=np.logspace(-1,3,1000)
y=20*np.log10(eval(expr))
ax1.semilogx(x,y,color="black")

#bessel filters
b, a = signal.bessel(8,3.3,"low", analog=True,norm="mag")
w, h = signal.freqs(b,a)
t1, v1 = signal.impulse((b,a))
ax2.plot(t1,10*v1,color="blue")
ax1.semilogx(w,20*np.log10(abs(h)),color="blue")
b, a = signal.bessel(8,33,"low", analog=True,norm="mag")
w, h = signal.freqs(b,a)
t2, v2 = signal.impulse((b,a))
ax2.plot(t2,v2,color="red")
ax1.semilogx(w,20*np.log10(abs(h)),color="red")

plot.show()

