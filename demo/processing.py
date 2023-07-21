import numpy as np
import pandas as pd

df = pd.read_json("bbc_final.jsonl", lines=True)
# print(df.head())

char_set = [' ', 'ँ', 'ं', 'ः', 'अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ऋ', 'ए', 'ऐ', 'ऑ', 'ओ', 'औ', 'क', 'ख', 'ग', 'घ','ङ', 'च', 'छ', 'ज', 'झ', 'ञ', 'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न', 'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'क्ष', 'त्र' ,'ज्ञ', 'श्र' ,'ा', 'ि', 'ी', 'ु', 'ू', 'ृ', 'े', 'ै', 'ॉ', 'ो', 'ौ', '्', 'ज़', 'ड़', 'ढ़', 'फ़',
'़', 'ॅ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '%', '(', ')', '/', '!'
]
cnt = 0
for article in df["Content"]:
    for para in article:
        sentences = para.split(".")
        for sentence in sentences:
            sentence = sentence.strip()
            sentence = sentence.replace(",", "")
            sentence = sentence.replace("?", "")
            sentence = sentence.replace("'", "")
            sentence = sentence.replace(":", "")
            sentence = sentence.replace("-", "")
            sentence = sentence.replace('"', "")
            sentence = sentence.replace("“", "")
            sentence = sentence.replace("”", "")
            sentence = sentence.replace("‘", "")
            sentence = sentence.replace("’", "")    
            sentence = sentence.strip()
            if sentence == "" or sentence == "”" or sentence == '"' or sentence == '" "':
                None
            else:
                flag = True
                for char in sentence:
                    if char not in char_set:
                        flag = False
                        # if char.isalpha() == False:
                        #     print(char)
                    else:
                        None
                if flag == True:    
                    # print(sentence)
                    cnt += 1
                    with open('output.txt', 'a') as file:
                        file.write(sentence + "\n") 

print(cnt)        