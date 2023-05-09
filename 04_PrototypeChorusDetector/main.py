#Import configuration values
import config

#Import other necessary libraries
import numpy as np
import math
import os

#Imports for machine learning
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder

#Imports for handling audio
import librosa

#Tk GUI toolkit
import tkinter as tk
from tkinter import filedialog

#Global Variables
input_file_path = ''
is_valid_path_selected = False
is_valid_result_available = False

#Function Declarations------------------------------------------------

#Function to pad MFCC 2D array
#Idea for cleanly writing padding function is taken from the below 2 posts.
#https://stackoverflow.com/questions/59241216/padding-numpy-arrays-to-a-specific-size
#https://towardsdatascience.com/cnns-for-audio-classification-6244954665ab
def pad_features(feature_array,expected_height,expected_width):
    array_height = feature_array.shape[0]
    array_width = feature_array.shape[1]
    
    pad_height = max(expected_height-array_height,0)
    pad_height1 = math.floor(pad_height/2)
    pad_height2 = max(pad_height-pad_height1,0)
    
    pad_width = max(expected_width-array_width,0)
    pad_width1 = math.floor(pad_width/2)
    pad_width2 = max(pad_width-pad_width1,0)
    
    #print('h->'+str(pad_height)+'|| w->'+str(pad_width))
    return np.pad(array=feature_array,pad_width=((pad_height1,pad_height2),
                                                 (pad_width1,pad_width2)),mode='constant')

#Handling button clicks--
#Check for .wav files
def is_file_wav(file_path):
    if (os.path.isfile(file_path)):
        file_path_splits = file_path.split('.')
        file_path_extension = file_path_splits[len(file_path_splits)-1]
        if(file_path_extension==config.WAV_FILE_EXTENSION):
            return True
        else:
            return False
    else:
        return False


#File selection
def select_file_clicked():
    file_path = filedialog.askopenfilename(filetypes=config.FILE_TYPES_SUPPORTED)

    result_label.config(text=config.NO_RESULT_TEXT)
    
    global input_file_path
    global is_valid_path_selected
    global is_valid_result_available

    #Update global variables
    is_valid_result_available = False
    input_file_path = file_path
    
    #Validation to filter only .wav files
    if(is_file_wav(input_file_path)):
        is_valid_path_selected = True
    else:
        is_valid_path_selected = False

    #Validation for correct file path
    if(is_valid_path_selected):
        detect_chorus_button.config(state="normal")
        filepath_label.config(text=file_path)
    else:
        detect_chorus_button.config(state="disabled")
        filepath_label.config(text="<Please select a valid .wav file>")

#Chorus detection
def detect_chorus_clicked():
    #Loading the saved ML model
    model = keras.models.load_model(config.ML_MODEL_PATH)
    global is_valid_result_available

    try:
        #Load audio file to a pythoon list of sample values
        audio, sample_rate = librosa.load(input_file_path, res_type='kaiser_fast')

        #Extraction of features after padding
        mfccs_features1 = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=config.N_MFCC)
        mfccs_features = pad_features(mfccs_features1,config.N_MFCC,config.WIDTH_MFCC)

        #Predict
        label = model.predict(np.array([mfccs_features]))
        prediction_weights = label[0]
        is_valid_result_available = True
    except Exception as e:
        print('EXCEPTION: '+str(e))
        is_valid_result_available = False

    #Output text generation based on the result
    if(prediction_weights[0]>prediction_weights[1]):
        prediction = config.VANILLA_SOUND_TEXT
        certainity = round(prediction_weights[0]*100,config.CERATAINITY_DEC_POINTS)
    elif(prediction_weights[0]<prediction_weights[1]):
        prediction = config.CHORUS_SOUND_TEXT
        certainity = round(prediction_weights[1]*100,config.CERATAINITY_DEC_POINTS)
    else:
        prediction = config.VANILLA_CHORUS_TEXT
        certainity = '100.00'
    
    # display the prediction to the user
    if(is_valid_result_available):
        result_label.config(text=prediction +' with certainity of ' +str(certainity)+'%')
    else:
        result_label.config(text=config.NO_RESULT_TEXT)
#---------------------------------------------------------------------

#GUI with Layout Specification----------------------------------------

#main window
window = tk.Tk()
window.iconbitmap(config.ICON_PATH)

#window title
window.title("Chorus Detector")

#window size
window.geometry(config.WIDTHXHEIGHT)

# create a label to display the file path selected
filepath_label = tk.Label(text='<Select audio file>')
filepath_label.place(x=10, y=10)

#button to upload input data
select_file_button = tk.Button(text="Select audio file...", 
                                command=select_file_clicked, width=20, height=1)
select_file_button.config(state="normal")
select_file_button.place(x=10, y=40)

#button to invoke chorus detection
detect_chorus_button = tk.Button(text="Detect Chorus",
                                    command=detect_chorus_clicked, width=20, height=1)
detect_chorus_button.config(state="disabled")
detect_chorus_button.place(x=10, y=80)

# create a label to display the predicted output
result_label = tk.Label(text=config.NO_RESULT_TEXT)
result_label.place(x=10, y=120)

# Display the window
window.mainloop()
#--------------------------------------------------------------------