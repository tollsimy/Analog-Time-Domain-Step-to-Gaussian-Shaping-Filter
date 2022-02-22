import numpy as np
import matplotlib.pyplot as plot

fig1, ax1 = plot.subplots()
w=np.logspace(-1,3,100)

gauss3_6_LP="(110.2)/(((-1j)*(w**3))+(-10.98*(w**2))+(56.4j*w)+110.2)"
y=20*np.log10(abs(eval(gauss3_6_LP)))
ax1.semilogx(w,y,color="red")

gauss1_6_HP="(1j*w)/((1j*w)+2)"
y=20*np.log10(abs(eval(gauss1_6_HP)))
ax1.semilogx(w,y,color="blue")

expr="w*(0.5*np.e**((-w**(2))/(2*(2.57**(2)))))"
y=(20*np.log10((eval(expr))))
ax1.plot(w,y,color="black")
ax1.set_xlim(0.01,100)
ax1.set_ylim(-50,1)

plot.show()
