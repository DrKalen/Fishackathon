# preprocessing of .wav and .ogg sound files to a common format
# then return different spectral and audio representations


import os
import librosa
import matplotlib.pyplot as plt
import numpy as np


def get_mfcc(audioFile, sampleRate=16000, n_mfcc=13):
	audio, rate = librosa.load(audioFile)
	
	# resample to a set rate
	audio = librosa.core.resample(audio, rate, sampleRate)

	# Let's make and display a mel-scaled power (energy-squared) spectrogram
	S = librosa.feature.melspectrogram(audio, sr=sampleRate, n_mels=128)

	# Convert to log scale (dB). We'll use the peak power (max) as reference.
	log_S = librosa.power_to_db(S, ref=np.max)


	# we'll extract the top 13 Mel-frequency cepstral coefficients (MFCCs)
	mfcc = librosa.feature.mfcc(S=log_S, n_mfcc=n_mfcc)

	#return mfcc time series tensor
	return mfcc




def audio_spectogram(audioFile, sampleRate=16000, complexity='magnitude'):
	audio, rate = librosa.load(audioFile)
	
	# resample to a set rate
	audio = librosa.core.resample(audio, rate, sampleRate)

	# fast mellin transform, double sided laplace transform
	audio_spec = librosa.core.fmt(audio)

	# return audio spectrogam that as a matrix

	if complexity == 'magnitude':
		magnitude, phase = librosa.core.magphase(audio_spec)
		return magnitude
	elif complexity == 'phase':
		magnitude, phase = librosa.core.magphase(audio_spec)
		return phase
	elif complexity =='complex':
		return audio_spec
	else:
		print("???. not sure what format you want from audio_spectrogram()")


def short_fft(audioFile, sampleRate=16000, window=2048, numFrames=10,
				complexity='magnitude'):
	audio, rate = librosa.load(audioFile)
	
	# resample to a set rate
	audio = librosa.core.resample(audio, rate, sampleRate)

	fft_transform = librosa.core.stft(audio, 
									n_fft=window,
									hop_length=numFrames)

	if complexity=='magnitude': # if we only want the signal magnitude
		magnitude, phase = librosa.core.magphase(fft_transform)
		return magnitude
	elif complexity=='phase': # if we only want the phase
		magnitude, phase = librosa.core.magphase(fft_transform)
		return phase
	elif complexity=='complex': # if we want the real and imaginary parts
		return fft_transform
	else:
		print("WOOPS, not sure what short_fft return format you want")
	# return the short time fourier transform of the audiofile 





#######################################################
## MAIN ##
#######################################################
def main():
	audioFiles = os.listdir("sounds")
	'''
	audio = {}
	for file in audioFiles[:2]: # just do the first few for now
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
	'''

	audioFile = "sounds/"+audioFiles[0]
	print('---------------------')

	mfcc = get_mfcc(audioFile, sampleRate=16000, n_mfcc=13)
	print(mfcc.shape)
	print('---------------------')

	audioSpec = audio_spectogram(audioFile, sampleRate=16000)
	# return audio spectrogam that as a matrix
	print(audioSpec.shape)
	print('---------------------')


	fft = short_fft(audioFile, sampleRate=16000, window=2048, numFrames=10)
	# return the short time fourier transform of the audiofile 
	print(fft.shape)
	print('---------------------')


	# TO-DO: break up these spectra into training samples


	plt.figure()
	plt.plot(mfcc.T)

	plt.figure()
	plt.plot(audioSpec)

	#plt.figure()
	#plt.plot(fft)

	plt.show()


if __name__ == '__main__':
	main()


