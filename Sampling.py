import pip
try:
    import numpy as np
    import matplotlib.pyplot as plt
except ImportError:
    # pip.main(['install', 'numpy'])
    # pip.main(['install', 'matplotlib'])
    # import numpy as np
    # import matplotlib.pyplot as plt
    print("Install numpy and matplotlib !!!")


class createWave:
    def __init__(self, t_start, t_end, dt):
        self.t = np.arange(t_start, t_end + dt, dt)

    def sineWave(self, f, ph):
        return [np.sin(self.t * 2 * f * np.pi + ph), self.t]

    def time(self):
        return self.t

t_start = 0
t_end = 1
f = int(input("Enter Signal Frequency: "))
wave = createWave(t_start, t_end, 0.001)
x, t = wave.sineWave(f, 0)

Fs = int(input("Enter Sampling Frequency: ")) #Sampling Frequency
Ts = 1 / Fs
sampling = createWave(t_start, t_end, Ts)

###########################################################################
#Sampled Signal
x_samp, t_samp = sampling.sineWave(f, 0)
plt.plot(t, x, 'b-')
markerline, stemlines, baseline = plt.stem(t_samp, x_samp, 'r-', 'ro')
markerline.set_markerfacecolor('none')
plt.xlabel('Time')
plt.ylabel('Amplitude')
###########################################################################

###########################################################################
#Quantized Signal
q = float(input("Enter Quantization Level (1>) : "))
x_quant = np.round(x_samp / q) * q
markerline2, stemlines2, baseline2 = plt.stem(t_samp, x_quant, linefmt='r--', markerfmt='gs', basefmt='r-')
markerline2.set_markerfacecolor('none')
plt.yticks(np.arange(np.min(x_quant), np.max(x_quant) + q, q))
plt.grid(True)
plt.show()
###########################################################################
i = input()
exit()