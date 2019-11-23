import librosa
import vamp

data, rate = librosa.load("Adele - Rolling in the Deep-rYEDA3JcQqw.wav")
chroma = vamp.collect(data, rate, "vamp:segmentino:segmentino:segmentation")
