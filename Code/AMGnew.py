#loading best model
from keras.models import load_model
import datetime
import numpy as np
from music21 import *
import random
import sys

model_given = sys.argv[1]
print(model_given)

if model_given == 'blues':
    model = load_model('D:/Study Related/SEM 6/Mini Project/Code/Models/blues.h5')
    file1 = open("D:/Study Related/SEM 6/Mini Project/Code/xval_blues.txt", 'r')
    file2 = open("D:/Study Related/SEM 6/Mini Project/Code/unique_x_blues.txt", 'r')
elif model_given == 'instrumental':
    model = load_model('D:/Study Related/SEM 6/Mini Project/Code/Models/instrumental.h5')
    file1 = open("D:/Study Related/SEM 6/Mini Project/Code/xval_instrumental.txt", 'r')
    file2 = open("D:/Study Related/SEM 6/Mini Project/Code/unique_x_instrumental.txt", 'r')
elif model == 'piano':
    model = load_model('D:/Study Related/SEM 6/Mini Project/Code/Models/piano.h5')
    file1 = open("D:/Study Related/SEM 6/Mini Project/Code/xval_piano.txt", 'r')
    file2 = open("D:/Study Related/SEM 6/Mini Project/Code/unique_x_piano.txt", 'r')

lines = file1.readlines()
array_string = ""
for line in lines:
    array_string += str(line)
file1.close()
array_string = array_string.replace("[","").replace("]","")
x_val = np.fromstring(array_string, dtype=int, sep=' ')
x_val = x_val.reshape(-1,32)

ind = np.random.randint(0,len(x_val)-1)

random_music = x_val[ind]
no_of_timesteps = 32

predictions=[]
for i in range(100):

    random_music = random_music.reshape(1,no_of_timesteps)

    prob  = model.predict(random_music)[0]
    y_pred= np.argmax(prob,axis=0)
    predictions.append(y_pred)

    random_music = np.insert(random_music[0],len(random_music[0]),y_pred)
    random_music = random_music[1:]

print("\n"*4)   
print(predictions)

unique_x = file2.readline()
file2.close()

unique_x = unique_x.replace("'","").replace(" ","").replace("[","").replace("]","").split(",")
x_int_to_note = dict((number, note_) for number, note_ in enumerate(unique_x)) 
predicted_notes = [x_int_to_note[i] for i in predictions]

def convert_to_midi(prediction_output):
   
    offset = 0
    output_notes = []

    # create note and chord objects based on the values generated by the model
    for pattern in prediction_output:
        
        # pattern is a chord
        if ('.' in pattern) or pattern.isdigit():
            notes_in_chord = pattern.split('.')
            notes = []
            for current_note in notes_in_chord:
                
                cn=int(current_note)
                new_note = note.Note(cn)
                new_note.storedInstrument = instrument.Piano()
                notes.append(new_note)
                
            new_chord = chord.Chord(notes)
            new_chord.offset = offset
            output_notes.append(new_chord)
            
        # pattern is a note
        else:
            
            new_note = note.Note(pattern)
            new_note.offset = offset
            new_note.storedInstrument = instrument.Piano()
            output_notes.append(new_note)

        # increase offset each iteration so that notes do not stack
        offset += 1
    midi_stream = stream.Stream(output_notes)
    midi_stream.write('midi', fp='D:/Study Related/SEM 6/Mini Project/AMG/static/music/music.mid')

convert_to_midi(predicted_notes)