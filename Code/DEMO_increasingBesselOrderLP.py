import functools
import numpy as np
import matplotlib.pyplot as plot
from scipy import signal

def plotlive(func):
    plot.ion()
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        result = func(*args, **kwargs)
        plot.draw()
        plot.pause(1)
        return result
    return new_func

@plotlive
def plot_something_live(ax, x, y):
    ax.plot(x, y)

#setting plots
plot.ion()
fig1, (ax1,ax2) = plot.subplots(1,2)
mng = plot.get_current_fig_manager()
mng.resize(1200,600)
ax1.set_title("Frequency response")
ax1.set_xlabel("Angular frequency [rad/s]")
ax1.set_ylabel("Gain [dB]")
ax2.set_title("Impulse response")
ax2.set_xlabel("Time [S]")
ax1.set_xlim(0.1,100)
ax1.set_ylim(-120,1)

#gaussian with variance 1.15
expr="x*(0.5*np.e**((-x**(2))/(2*(2.57**(2)))))"
x=np.logspace(-1,3,1000)
y=20*np.log10(eval(expr))
ax1.semilogx(x,y,color="black")

for i in range(10):
    b, a = signal.bessel(i+1,3.3,"low", analog=True,norm="mag")
    w, h = signal.freqs(b,a)
    plot_something_live(ax1, w, 20*np.log10(abs(h)))
    t2, v2 = signal.impulse((b,a))
    plot_something_live(ax2, t2, v2)