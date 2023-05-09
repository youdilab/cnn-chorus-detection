# cnn-chorus-detection
Repository includes source code used in a research project to develop a machine learning model to detect the presence of chorus effect in synthesized organ-like sounds.

Abstract 

Chorus audio effect is used widely in the music industry like many other common 
audio effects such as reverb, distortion, compression, pitch shifting. The purpose of 
the effect is to make a given single source audio input, sound like it is coming from 
multiple sources to create an ensemble effect. Identifying the presence of chorus or 
ensemble effect in a sound is performed manually by listening to the sound. If it 
must be done for many sounds, it becomes tedious. In this research the possibility of 
implementation of a machine learning model to detect the presence of chorus effect 
in synthesized organ-like sounds is explored.

Initially, a dataset of synthesized organ-like sounds is generated. The chorus effect is 
applied to each sound using varying chorus parameters to create a similar-sized 
dataset of sounds with chorus. Both vanilla and chorus datasets are labelled, 
combined, and Mel-frequency cepstral coefficients (MFCCs) are extracted from each 
of the sounds. Those data are then used to train a convolutional neural network 
(CNN). The trained model is tuned by varying the feature extraction parameters, 
hyperparameters of the CNN and measuring its performance in detecting chorus 
effect in synthesized organ-like sounds. Additionally, the same is measured for 
acoustic sounds. The final trained model can detect the chorus effect in synthesized 
organ-like sounds with an accuracy of 90%. The research also shows that CNN 
models trained with extracted MFCC data can be used to detect chorus audio effect 
and hence provides a foundation for future work to detect other more sophisticated 
audio effects in more dynamic sounds.

Keywords: Chorus Effect, Audio Effect Detection, Audio Classification, MFCC, CNN
