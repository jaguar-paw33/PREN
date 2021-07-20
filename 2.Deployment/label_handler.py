import numpy as np
import tensorflow as tf
from utils import *

class LabelEncoderDecoder():
    def __init__(self, max_label_length, alphabets=alphabets):
        
        self.alphabets = alphabets
        
        self.characters_dict = {}
        self.characters_dict['<pad>'] = 0
        self.characters_dict['<eos>'] = 1
        self.characters_dict['<unk>'] = 2

        for i, character in enumerate(self.alphabets):
            self.characters_dict[character] = i+3 

        
    def encode(self, labels):
        
        encoded_labels = []
        
        for label in labels:
            
            encoded_label = []
            
            for character in label:

                if character in self.characters_dict.keys():
                    encoded_label.append(self.characters_dict[character])

                else:
                    encoded_label.append(self.characters_dict['<unk>'])

            if(len(encoded_label)>=max_label_length):
                encoded_label = encoded_label[:max_label_length-1]

            encoded_label.append(self.characters_dict['<eos>'])
                
            if(len(encoded_label)<max_label_length):
                encoded_label+=[self.characters_dict['<pad>']]*(max_label_length-len(encoded_label))

            encoded_labels.append(encoded_label)
    
        return encoded_labels
        
    def decode(self, encoded_labels):
        
        decoded_labels = []
        
        for label in encoded_labels:
            
            encoded_label = label

            if(tf.is_tensor(label)):
                encoded_label = label.numpy()
            
            end = encoded_label.shape[0]
            
            if(1 in encoded_label):
                end = np.where(encoded_label==1)[0][0]
            
            encoded_label=encoded_label[:end]

            decoder_dict = dict(zip(self.characters_dict.values(), self.characters_dict.keys()))
            
            decoded_label = [decoder_dict[val] for val in encoded_label if val != 0]

            decoded_labels.append(''.join(decoded_label).upper())
        
        return decoded_labels

label_handler = LabelEncoderDecoder(max_label_length, alphabets)