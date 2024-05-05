#!/usr/bin/env python
# coding: utf-8

# In[21]:


import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import speech_recognition as sr
from pydub import AudioSegment
import pickle

class SignLanguageConverter:
    def __init__(self):
        pass
    
    def live_audio_to_text(self):
        recognizer = sr.Recognizer()
    
        # Use the default system microphone as the audio source
        with sr.Microphone() as source:
            print("Speak something...")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            
            while True:
                try:
                    audio_data = recognizer.listen(source, timeout=3)  
                    
                    # Perform speech recognition on the audio data
                    text = recognizer.recognize_google(audio_data)
                    print("You said:", text)
                    return text
                
                except sr.UnknownValueError:
                    print("Sorry, could not understand audio.")
                except sr.RequestError as e:
                    print(f"Error: {e}")
                if 'stop' in text.lower():
                        print("Stopping the session...")
                        break
            return ''
    
    def text_to_sign_language(self, text):
        sign_language_dict = {
            'A': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\A.jpg",
            'B': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\B.jpg",
            'C': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\C.jpg",
            'D': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\D.jpg",
            'E': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\E.jpg",
            'F': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\F.jpg",
            'G': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\G.jpg",
            'H': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\H.jpg",
            'I': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\I.jpg",
            'J': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\J.jpg",
            'K': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\K.jpg",
            'L': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\L.jpg",
            'M': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\M.jpg",
            'N': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\N.jpg",
            'O': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\O.jpg",
            'P': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\P.jpg",
            'Q': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\Q.jpg",
            'R': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\R.jpg",
            'S': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\S.jpg",
            'T': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\T.jpg",
            'U': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\U.jpg",
            'V': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\V.jpg",
            'W': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\W.jpg",
            'X': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\X.jpg",
            'Y': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\Y.jpg",
            'Z': "C:\\Users\\Dell\\Desktop\\12\\ISL data\\Z.jpg"
        }

        sign_language_images = []
        for letter in text.upper():
            if letter in sign_language_dict:
                image_path = sign_language_dict[letter]
                try:
                    img = Image.open(image_path)
                    sign_language_images.append(img)
                except FileNotFoundError:
                    print(f"Image not found for letter: {letter}")
        return sign_language_images
    
    def display_sign_language_images(self, sign_language_images):
        if sign_language_images:
            # Calculate the total width and height of the combined image
            total_width = sum(img.width for img in sign_language_images)
            max_height = max(img.height for img in sign_language_images)

            # Create a new image with the total width and height
            combined_image = Image.new('RGB', (total_width, max_height))

            # Calculate the x offset for each image
            x_offset = 0
            for img in sign_language_images:
                combined_image.paste(img, (x_offset, 0))
                x_offset += img.width

            # Display the combined image
            plt.imshow(combined_image)
            plt.axis('off')
            plt.show()
        
        
    def live_audio_to_sign_language(self):
        while True:
            text = self.live_audio_to_text()
            if text:
                translated_images = self.text_to_sign_language(text)
                self.display_sign_language_images(translated_images)
            if 'stop' in text.lower():
                break
                
            else:
                print("No speech detected. Please try again.")
    
    
converter = SignLanguageConverter()




# In[23]:


converter.live_audio_to_sign_language()


# In[24]:


with open('A2SLtest.pkl', 'wb') as f:
    pickle.dump(converter, f)


# In[32]:


def live_audio_to_text():
    recognizer = sr.Recognizer()
    
    # Use the default system microphone as the audio source
    with sr.Microphone() as source:
        print("Speak something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        
        while True:
            try:
                audio_data = recognizer.listen(source, timeout=3)  # Listen to microphone input for up to 3 seconds
                
                # Perform speech recognition on the audio data
                text = recognizer.recognize_google(audio_data)
                print("You said:", text)
                
                if 'stop' in text.lower():
                    print("Stopping the session...")
                    break
                    
                return text
                
            except sr.UnknownValueError:
                print("Sorry, could not understand audio.")
            except sr.RequestError as e:
                print(f"Error: {e}")
        return None

# Call the function to start live audio-to-text conversion
#live_audio_to_text()


# In[39]:


def text_to_sign_language(text):
    sign_language_dict = {
        'A': "C:\\Users\\Dell\\Desktop\\ISL data\\A.jpg",
        'B': "C:\\Users\\Dell\\Desktop\\ISL data\\B.jpg",
        'C': "C:\\Users\\Dell\\Desktop\\ISL data\\C.jpg",
        'D': "C:\\Users\\Dell\\Desktop\\ISL data\\D.jpg",
        'E': "C:\\Users\\Dell\\Desktop\\ISL data\\E.jpg",
        'F': "C:\\Users\\Dell\\Desktop\\ISL data\\F.jpg",
        'G': "C:\\Users\\Dell\\Desktop\\ISL data\\G.jpg",
        'H': "C:\\Users\\Dell\\Desktop\\ISL data\\H.jpg",
        'I': "C:\\Users\\Dell\\Desktop\\ISL data\\I.jpg",
        'J': "C:\\Users\\Dell\\Desktop\\ISL data\\J.jpg",
        'K': "C:\\Users\\Dell\\Desktop\\ISL data\\K.jpg",
        'L': "C:\\Users\\Dell\\Desktop\\ISL data\\L.jpg",
        'M': "C:\\Users\\Dell\\Desktop\\ISL data\\M.jpg",
        'N': "C:\\Users\\Dell\\Desktop\\ISL data\\N.jpg",
        'O': "C:\\Users\\Dell\\Desktop\\ISL data\\O.jpg",
        'P': "C:\\Users\\Dell\\Desktop\\ISL data\\P.jpg",
        'Q': "C:\\Users\\Dell\\Desktop\\ISL data\\Q.jpg",
        'R': "C:\\Users\\Dell\\Desktop\\ISL data\\R.jpg",
        'S': "C:\\Users\\Dell\\Desktop\\ISL data\\S.jpg",
        'T': "C:\\Users\\Dell\\Desktop\\ISL data\\T.jpg",
        'U': "C:\\Users\\Dell\\Desktop\\ISL data\\U.jpg",
        'V': "C:\\Users\\Dell\\Desktop\\ISL data\\V.jpg",
        'W': "C:\\Users\\Dell\\Desktop\\ISL data\\W.jpg",
        'X': "C:\\Users\\Dell\\Desktop\\ISL data\\X.jpg",
        'Y': "C:\\Users\\Dell\\Desktop\\ISL data\\Y.jpg",
        'Z': "C:\\Users\\Dell\\Desktop\\ISL data\\Z.jpg"
    }

    sign_language_images = []
    for letter in text.upper():
        if letter in sign_language_dict:
            image_path = sign_language_dict[letter]
            try:
                img = Image.open(image_path)
                sign_language_images.append(img)
            except FileNotFoundError:
                print(f"Image not found for letter: {letter}")
    return sign_language_images


# In[22]:


def display_sign_language_images(sign_language_images):
    if sign_language_images:
        # Calculate the total width and height of the combined image
        total_width = sum(img.width for img in sign_language_images)
        max_height = max(img.height for img in sign_language_images)

        # Create a new image with the total width and height
        combined_image = Image.new('RGB', (total_width, max_height))

        # Calculate the x offset for each image
        x_offset = 0
        for img in sign_language_images:
            combined_image.paste(img, (x_offset, 0))
            x_offset += img.width

        # Display the combined image
        plt.imshow(combined_image)
        plt.axis('off')
        plt.show()


# In[14]:


def live_audio_to_sign_language():
    while True:
        text = live_audio_to_text()
        if text:
            print("Text from microphone:", text)
            translated_images = text_to_sign_language(text)
            display_sign_language_images(translated_images)


# In[37]:


live_audio_to_sign_language()


# In[41]:


import pickle

with open('sign_language_functions.pkl', 'wb') as f:
    pickle.dump((live_audio_to_text, text_to_sign_language, display_sign_language_images, live_audio_to_sign_language), f)


# In[ ]:




