#Application winodw size
WIDTHXHEIGHT="300x200"

#Path where ML model is saved.
ML_MODEL_PATH = 'MLmodels\\tuned_model_00.hdf5'

#Number of Mel-frequency cepstral coefficients
N_MFCC =128

#Maximum width of the 2D matrix containing MFCC data.
#This depends on the width of MFCC in training data.
WIDTH_MFCC = 173

#File selection window.
WAV_FILE_EXTENSION = 'wav'
FILE_TYPES_SUPPORTED = (("Wave files", "*.wav"), ("All files", "*.*"))

#Application result output text customization parameters
VANILLA_SOUND_TEXT = 'Vanilla'
CHORUS_SOUND_TEXT = 'Chorus'
VANILLA_CHORUS_TEXT = 'Vanilla and Chorus both.'
SELECT_WAV_MESSAGE_TEXT = "<Please select a .wav file of appropriate length.>"
CERATAINITY_DEC_POINTS = 2
NO_RESULT_TEXT = '<No result to display.>'

#Application icon
ICON_PATH = 'ChorusDetectorIcon.ico'