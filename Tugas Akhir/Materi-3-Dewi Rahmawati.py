import numpy as np
import matplotlib.pyplot as plt

g = 9.8
v0 = 0
h0 = 20

t_sampai_tanah = np.sqrt(2 * h0 / g)
print("Waktu Mencapai Tanah =", t_sampai_tanah, "s")
v_akhir = g * t_sampai_tanah
print("Kecepatan Akhir Benda =", v_akhir, "m/s")
h_akhir = h0 - 0.5 * g * t_sampai_tanah**2
print("Ketinggian Akhir Benda =", h_akhir, "m") 

t = np.linspace(0, t_sampai_tanah, 1000)
v = g * t 
h = h0 - 0.5 * g * t**2  

fig, ax = plt.subplots()
ax.plot(t, v)
ax.set(xlabel='Waktu (s)', ylabel='Kecepatan (m/s)', title='Grafik Kecepatan  terhadap Waktu selama Benda Jatuh')
ax.grid()

fig, ax = plt.subplots()
ax.plot(t, h)
ax.set(xlabel='Waktu (s)', ylabel='Ketinggian (m)', title='Grafik Posisi Benda terhadap Waktu selama Benda Jatuh')
ax.grid()

plt.show()
