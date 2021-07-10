# Automatic-music-Generation
In this topic titled ‘Automatic music generation’ we will be focussing on generating small pieces of music as the output. Our devised model will be trained using small music files (MIDI). MIDI (Musical Instrument Digital interface) is the type of music files used as they not only contain the actual audio but also some instructions. We then will be using the python library ‘music21’ which will break down these music files into chords and notes and separate them based on their frequency. We will be doing this to get the understanding of what type of frequency notes are combined together to form the actual music. We will be using the LSTM network to ensure the model does not lack structure and long-term dependencies. Being trained on this, now our trained model will take notes and chords as inputs and combine them to try to predict some meaningful music.
  
  # Instructions for setup
  AMG.html and index.html are the web pages that have been designed for our project. Move your project report inside AMG/static
  
  ## Code Folder
  Code Folder contains the datasets we have used for our project. This zip file also contains two main files AMG.ipynb and AMGtrain.ipynb. AMG.ipynb is the code which we have used for training our model on different datasets. AMG.ipynb is the file which used these pretrained models to generate music.
  
  ## AMG Folder
  AMG Folder contains the django project wherein we have integrated our project with the website designed.
  
  # UML diagrams for better understanding of the project
  ![AMG UML use case diagram](https://user-images.githubusercontent.com/66869179/117314523-796d2e00-aea4-11eb-9625-0775773aa047.jpg)
![AMG UML class diagram](https://user-images.githubusercontent.com/66869179/117314566-838f2c80-aea4-11eb-8e2e-72034b214fd7.jpg)
![AMG Sequence Diagram](https://user-images.githubusercontent.com/66869179/117314603-90ac1b80-aea4-11eb-860f-5c4ded145a1b.png)
![AMG Activity Diagram](https://user-images.githubusercontent.com/66869179/117314632-96a1fc80-aea4-11eb-88ae-9d6da4f028ef.JPG)
