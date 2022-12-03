import numpy as np 
import pyaudio as pa 
import struct 
import matplotlib.pyplot as plt 
import os
import wave

#CHUNK = 1024 * 2
CHUNK = 1024
FORMAT = pa.paInt16
CHANNELS = 1
RATE = 44100 # in Hz
file_path = '../data/audio/aeka_audio/'
files = os.listdir(file_path)
file = 'AEKA0_tcp-27_11_2022-16-08-20.wav'
p = pa.PyAudio()
#for file in files:
wf = wave.open(file_path + file, 'rb')
stream = p.open(
    format =p.get_format_from_width(wf.getsampwidth()),
    channels = wf.getnchannels(),
    rate = wf.getframerate(),
    output = True)
        #format = FORMAT,
        #channels = CHANNELS,
        #rate = RATE,
        #input=True,
        #output=True,
        #frames_per_buffer=CHUNK
    #)



fig,ax = plt.subplots()
x = np.arange(0,2*CHUNK,2)
line, = ax.plot(x, np.random.rand(CHUNK),'r')
ax.set_ylim(-60000,60000)
ax.ser_xlim = (0,CHUNK)
fig.show()

while 1:
    data = stream.read(CHUNK)
    dataInt = struct.unpack(str(CHUNK) + 'h', data)
    line.set_ydata(dataInt)
    fig.canvas.draw()
    fig.canvas.flush_events()
