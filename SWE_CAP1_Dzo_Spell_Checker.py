##########################
# https://github.com/6-ndjamyang/SWE_CAP1_Dzo_Spell_Checker.git
# Jamyang Ngawang Dorji
# Section: A
# ID : 02240342
##########################
#REFERENCE : Youtube, Co-pilot
#Ref Links
#
#
#

#########################
# Solution
#########################




import re

def extract_words(text):
    
    words = re.findall(r'[\u0F00-\u0FFF]+', text) #In this part I got help from AI as I didn't know how dzongkha characters were represented
    return set(words)  

with open("342.txt", encoding="utf-8") as file:
    content1 = file.read()
    word1 = extract_words(content1)

with open("cleaned_file.txt", encoding="utf-8") as file:
    content2 = file.read()
    word2 =extract_words(content2)

unique_to_file1 = word1.difference(word2)  

for word in unique_to_file1:
    print(f"The word '{word}' from 342.txt is incorrect.")
