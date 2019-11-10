# -*- coding: utf-8 -*-
"""App4-S5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1morNhlAW_Cucm8mrP6r66HxjEJYgok8a
"""

import numpy as np
import matplotlib.pyplot as plt

### Plots' title and axes are missing for now

N = 10000
u_uniform = np.random.uniform(0,1,N);
theta = 2*np.pi*u_uniform

plt.figure(0)
plt.xlabel("Échantillon")
plt.ylabel("Valeur de thêta")
plt.title("Valeurs aléatoires de thêta")
plt.plot(theta)

plt.figure(1)
plt.xlabel("Thêta (rad)")
plt.ylabel("Nombre d'échantillons")
plt.title("Histogramme des valeurs aléatoires de thêta")
plt.hist(theta, normed=1)

variance = np.array((0.25, 1, 4, 9, 16))

d = np.linspace(0,10,10000)

# Loi théorique de Rayleigh
plt.figure(2)
for v in variance:
  f_d = (d / v) * np.exp(- d**2 /(2 * v))
  plt.plot(d, f_d, label='Variance :' + str(v))  
plt.legend(loc='best')
plt.title("PDFs de la loi de Rayleigh")
plt.xlabel("x")
plt.ylabel("p(x)")

# CDF de rayleigh
plt.figure(3)
for v in variance:
  CDF = -np.exp(-d**2/(2 * v))+1
  plt.plot(d, CDF, label='Var :' + str(v))
plt.legend(loc="best")

# Histogrammes r commun
plt.figure(4)
P = np.random.uniform(0,1,N)
r_randomized = np.sqrt(-np.log(1-P)*(2*variance[2]))
plt.hist(r_randomized,label='Var :' + str(variance[2]))
plt.legend(loc="best")
plt.xlabel("r")
plt.ylabel("Fréquence de r")
plt.title("Réalisations des nombres aléatoires pour plusieurs variances")

plt.figure(5)
P = np.random.uniform(0,1,N)
r_randomized = np.sqrt(-np.log(1-P)*(2*variance[3]))
plt.hist(r_randomized,label='Var :' + str(variance[3]))
plt.legend(loc="best")
plt.xlabel("r")
plt.ylabel("Fréquence de r")
plt.title("Réalisations des nombres aléatoires pour plusieurs variances")

# Histogrammes de rayleigh aléatoire théorique
plt.figure(6)
r_theorique = np.random.rayleigh(np.sqrt(variance[2]), N)
plt.hist(r_theorique,label='Var :' + str(variance[2]))
plt.legend(loc="best")
plt.xlabel("r")
plt.ylabel("Fréquence de r")
plt.title("Réalisations théoriques des nombres aléatoires pour plusieurs variances")

plt.figure(7)
r_theorique = np.random.rayleigh(np.sqrt(variance[3]), N)
plt.hist(r_theorique,label='Var :' + str(variance[3]))
plt.legend(loc="best")
plt.xlabel("r")
plt.ylabel("Fréquence de r")
plt.title("Réalisations théoriques des nombres aléatoires pour plusieurs variances")

# Histogramme r séparé
n = 7
for v in variance:
  P = np.random.uniform(0,1,N)
  n-=np.cos(np.pi)
  plt.figure(n)
  d_randomized = np.sqrt(-np.log(1-P)*(2*v))
  plt.hist(d_randomized,bins=60,label='Var :' + str(v))
  plt.legend(loc="best")

# Nuages de points des différentes variance
plt.figure(13)
for v in reversed(variance):
  P = np.random.uniform(0,1,N)
  d_randomized = np.sqrt(-np.log(1-P)*(2*v))
  u_uniform = np.random.uniform(0,1,N);
  phi = 2*np.pi*u_uniform
  
  dx=d_randomized*np.cos(phi)
  dy=d_randomized*np.sin(phi)
  plt.scatter(dx,dy,label='Var :' + str(v))
plt.legend(loc="best")

# Couple r et theta
plt.figure(14)
for v in reversed(variance):
  P = np.random.uniform(0,1,N)
  d_randomized = np.sqrt(-np.log(1-P)*(2*v))
  u_uniform = np.random.uniform(0,1,N);
  phi = 2*np.pi*u_uniform
  plt.scatter(d_randomized,phi,label='Var :' + str(v))
plt.legend(loc="best")
plt.title("Couple thêta et r")
plt.xlabel("r")
plt.ylabel("Thêta")


# Vecteur final
v = 16
d = 100
angle_d = 30
angle = angle_d*np.pi/180

P = np.random.uniform(0,1,N)
r_randomized = np.sqrt(-np.log(1-P)*(2*v))
u_uniform = np.random.uniform(0,1,N);
theta = 2*np.pi*u_uniform
D = np.sqrt((d**2+2*d*r_randomized*np.cos(theta)+r_randomized))
Phi = angle+np.arctan((r_randomized*np.sin(theta))/(d+r_randomized*np.cos(theta)))
Dx = D*np.cos(Phi)
Dy = D*np.sin(Phi)

plt.figure(15)
plt.scatter(Dx,Dy, label="Nuage d'erreur additive")
plt.plot([0,d*np.cos(angle)], [0,d*np.sin(angle)],'r-',label="Vecteur du radar")
plt.title("Cas de figure [{0} {1}]".format(d,angle_d))
plt.xlim(0,120)
plt.xlabel("Dx (m)")
plt.ylim(0,80)
plt.ylabel("Dy (m)")
plt.legend(loc="best")

plt.figure(16)
plt.scatter(range(0,N),Dx)
plt.title("Valeurs de Dx, cas [{0} {1}]".format(d,angle_d))
plt.xlabel("Indice")
plt.ylabel("Valeurs de Dx (m)")

plt.figure(17)
bin_heights, bin_borders = np.histogram(Dx, bins=10)
plt.hist(Dx, bins=10,label="histogramme")
plt.plot(bin_borders[:-1]+(bin_borders[1]-bin_borders[0])/2,bin_heights,label="Courbe de fréquence relative")
plt.title("Histogramme Dx, cas [{0} {1}]".format(d,angle_d))
plt.xlabel("Classes")
plt.ylabel("Fréquence")
#plt.legend(loc="best")
Dx_mean = np.mean(Dx)
Dx_variance = np.var(Dx)
Dx_stddev = np.std(Dx)
print(Dx_mean, Dx_variance, Dx_stddev)

plt.figure(18)
plt.scatter(range(0,N),Dy)
plt.title("Valeurs de Dy, cas [{0} {1}]".format(d,angle_d))
plt.xlabel("Indice")
plt.ylabel("Valeurs de Dy (m)")

plt.figure(19)
##Dx -> Dy
bin_heights, bin_borders = np.histogram(Dy, bins=10)
##Dx -> Dy
plt.hist(Dy, bins=10,label="histogramme")
plt.plot(bin_borders[:-1]+(bin_borders[1]-bin_borders[0])/2,bin_heights,label="Courbe de fréquence relative")
plt.title("Histogramme Dy, cas [{0} {1}]".format(d,angle_d))
plt.xlabel("Classes")
plt.ylabel("Fréquence")
#plt.legend(loc="best")
Dy_mean = np.mean(Dy)
Dy_variance = np.var(Dy)
Dy_stddev = np.std(Dy)
print(Dy_mean, Dy_variance, Dy_stddev)