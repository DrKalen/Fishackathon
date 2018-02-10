# preprocessing of .wav and .ogg sound files to a common format
# then return different spectral and audio representations


import os
import librosa
import matplotlib.pyplot as plt
import numpy as np




def get_mfcc(audioFile, sampleRate=16000, n_mfcc=13):
	audio, rate = librosa.load(audioFile)
	
	# resample to a set rate
	audio = librosa.core.resample(audioData, rate, sampleRate)

	# Let's make and display a mel-scaled power (energy-squared) spectrogram
	S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)

	# Convert to log scale (dB). We'll use the peak power (max) as reference.
	log_S = librosa.power_to_db(S, ref=np.max)


	# we'll extract the top 13 Mel-frequency cepstral coefficients (MFCCs)
	mfcc = librosa.feature.mfcc(S=log_S, n_mfcc=n_mfcc)

	#return mfcc time series tensor
	return mfcc




def audio_spectogram(audioFile, sampleRate=16000,):
	audio, rate = librosa.load(audioFile)
	
	# resample to a set rate
	audio = librosa.core.resample(audioData, rate, sampleRate)



	# return audio spectrogam that as a matrix
	return 


def two_D_spectrogram(audioFile, sampleRate=16000,):
	audio, rate = librosa.load(audioFile)
	
	# resample to a set rate
	audio = librosa.core.resample(audioData, rate, sampleRate)


	# return static 2d spectrogram


def short_fft(audioFile, sampleRate=16000,):
	audio, rate = librosa.load(audioFile)
	
	# resample to a set rate
	audio = librosa.core.resample(audioData, rate, sampleRate)



	# return the short time fourier transform of the audiofile 





#######################################################
## MAIN ##
#######################################################
def main():
	audioFiles = os.listdir("sounds")

	audio = {}
	for file in audioFiles[:3]: # just do the first few for now
		try:
			audio[file] = librosa.load("sounds/"+file)
		except:
			print("failed to load %s" %file)


	sampleRates = [rate[1] for rate in audio.values()]
	sampleRate = np.median(sampleRates)

	# make sure all the files are at the same sample rate
	for file in audio.values():
		if (file[1] != sampleRate):
			file = librosa.core.resample(file[0], file[1], sampleRate)


	# take the short fourier transform 
	windowSize = 4


	# plot some stuff for visual checking
	for file in audio.values():
		print(file[0].shape)
		print("sample rate %d" %file[1])
		plt.figure()
		plt.plot(file[0])
	plt.show()



if __name__ == '__main__':
	main()


