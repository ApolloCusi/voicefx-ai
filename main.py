import librosa
import noisereduce as nr
import soundfile as sf

# cargar audio
y, sr = librosa.load("input.wav", sr=None)

# reducir ruido
reduced_noise = nr.reduce_noise(y=y, sr=sr)

# guardar resultado
sf.write("output.wav", reduced_noise, sr)

print("Audio procesado listo 🚀")