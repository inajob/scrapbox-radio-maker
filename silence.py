import json
import requests
import wave

def generate_wav(filepath='./silence.wav'):
    wf = wave.open(filepath, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(24000)
    for x in range(24000*2): # 2sec
      wf.writeframes(b'\0')
    wf.close()

if __name__ == '__main__':
    generate_wav()
