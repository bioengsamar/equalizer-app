from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
#from skimage import util
from scipy import fftpack
from matplotlib import cm
rate, audio = wavfile.read('mix3.wav')
#print(len(audio))
print(audio[:,1])
audio = np.mean(audio, axis=1)
#a=audio[:,0]
#print(a[0])

Fourier = fftpack.fft(audio)
fft_out=np.abs(Fourier)
print(fft_out)
freqs = fftpack.fftfreq(len(audio))*rate
print(freqs)
#print(len(fft_out))
bands1=[fft_out[0:273693],fft_out[273693:547386],fft_out[547386:821079],
fft_out[821079:1094772],fft_out[1094772:1368465],fft_out[1368465:1642158],
fft_out[1642158:1915851]]
#plt.plot(freqs,np.abs(fft_out))
#plt.show()
bands2=[freqs[0:273693],freqs[273693:547386],freqs[547386:821079],
freqs[821079:1094772],freqs[1094772:1368465],freqs[1368465:1642158],
freqs[1642158:1915851]]

#print(bands1[0])
colors = cm.rainbow(np.linspace(0, 1, len(bands1)))
for i,k,clr in zip(bands1,bands2,colors):
    plot, =plt.plot(k,i,color=clr)
    #plt.plot(fftpack.fftshift(i))