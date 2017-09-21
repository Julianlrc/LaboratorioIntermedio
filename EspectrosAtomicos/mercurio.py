import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

x = np.array([8.7, 8.8,10.9, 15.9])
y = np.array([ 579.07, 576.96, 546.07, 435.83])
rcParams['text.usetex'] = True

def reg(x):
	return -19.94*x + 755.336

def yerr(y, x):
	err = []
	for i in range(len(y)):
		e = abs(float((reg(x)[i]-y[i])))
		err.append(e)
	return err

print yerr(y, x)	

plt.errorbar(x, y, yerr=yerr(y, x), fmt='o', label=r"datos")
plt.plot(x, reg(x), label=r"Regresi\'on: $\lambda$ = -19.94x+755.336")
plt.title(r"Calibraci\'on de escala del espectr\'ometro (Espectro de Hg)")
plt.xlabel("Escala (unidades arbitrarias)")
plt.ylabel(r"$\lambda_{teo}$ (nm)")
plt.legend()
plt.savefig("calibracion.png")
plt.show()
