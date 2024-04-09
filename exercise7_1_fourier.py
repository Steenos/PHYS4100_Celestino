import numpy as np
import matplotlib.pyplot as plt

'''Write Python programs to calculate the coefficients in the discrete Fourier transforms 
of the following periodic functions sampled at N = 1000 evenly spaced points, 
and make plots of their amplitudes:

a) A single cycle of a square-wave with amplitude 1
b) The sawtooth wave yn = n
c) The modulated sine wave yn = sin(πn/N) sin(20πn/N)
'''

# Number of sample points
N = 1000

# sample points for a square-wave function
n = np.arange(N)
square_wave = np.ones(N)
square_wave[N//2:] = -1

#The DFT of the square-wave function
dft_square_wave = np.fft.fft(square_wave)

# Plot the amplitude of the DFT coefficients
plt.figure(figsize=(10, 6))
plt.plot(np.arange(N), np.abs(dft_square_wave), 'r')
plt.title('Amplitude of the DFT Coefficients for a Square-Wave Function')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

#sawtooth wave function
sawtooth_wave = n

dft_sawtooth_wave = np.fft.fft(sawtooth_wave)

# Plot the amplitude vs frequency
plt.figure(figsize=(10, 6))
plt.plot(np.arange(N), np.abs(dft_sawtooth_wave), 'b')
plt.title('Amplitude of the DFT Coefficients for a Sawtooth Wave Function')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

# Modulated sine wave function
y_modulated = np.sin(np.pi * n / N) * np.sin(20 * np.pi * n / N)

# Perform the Fourier Transform
dft_modulated = np.fft.fft(y_modulated)

# Plot the amplitude spectrum
plt.figure(figsize=(10, 4))
plt.plot(np.arange(N), np.abs(dft_modulated), 'g')
plt.title('Amplitude Spectrum of Modulated Sine Wave')
plt.ylabel('Amplitude')
plt.xlabel('Frequency (Hz)')
plt.grid()
plt.show()


