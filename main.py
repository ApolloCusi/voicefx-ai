Python 
import librosa
import noisereduce as nr
import soundfile as sf
import numpy as np

try:
    # cargar audio
    y, sr = librosa.load("input.wav", sr=None)

    # normalizar
    y = y / np.max(np.abs(y))

    # 👇 TOMAR SOLO UNA PARTE COMO "RUIDO"
    noise_sample = y[0:int(sr*0.5)]  # primeros 0.5 segundos

    # reducir ruido con perfil
    reduced_noise = nr.reduce_noise(
        y=y,
        sr=sr,
        y_noise=noise_sample,
        prop_decrease=0.8
    )

    # compresión suave
    compressed = np.tanh(reduced_noise * 1.5)

    # normalizar salida
    output = compressed / np.max(np.abs(compressed))

    # guardar
    sf.write("output.wav", output, sr)

    print("Audio mejorado listo 🚀")

except Exception as e:
    print("ERROR:", e)