##########################
# https://github.com/6-ndjamyang/SWE_CAP1_Dzo_Spell_Checker.git
# Jamyang Ngawang Dorji
# Section: A
# ID : 02240342
##########################
#REFERENCE : Youtube, Co-pilot, Google 
#Ref Links
#https://copilot.microsoft.com/
#https://www.youtube.com/watch?v=L2BDTy4bEcg
#https://www.youtube.com/watch?v=Mi3j54ZMxOc
#https://www.youtube.com/watch?v=L2BDTy4bEcg
#https://www.google.com/search?q=utf-8+encoding&sca_esv=757e01b514b177ca&ei=gh0RZ5yRDcKM4-EPgarq0As&ved=0ahUKEwic2pDEzpWJAxVCxjgGHQGVGroQ4dUDCA8&uact=5&oq=utf-8+encoding&gs_lp=Egxnd3Mtd2l6LXNlcnAiDnV0Zi04IGVuY29kaW5nMgUQABiABDILEAAYgAQYkQIYigUyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEisN1CQD1jSNHABeAGQAQCYAeEBoAHMEqoBBjAuMTIuMrgBA8gBAPgBAZgCD6AClBOoAgTCAhYQABgDGLQCGOUCGOoCGIwDGI8B2AEBwgIUEC4YgAQYsQMY0QMYgwEYxwEYigXCAgsQLhiABBixAxiDAcICERAuGIAEGLEDGNEDGIMBGMcBwgIIEC4YgAQYsQPCAgUQLhiABMICCxAAGIAEGLEDGIMBwgIKEAAYgAQYQxiKBcICCxAuGIAEGMcBGK8BwgIMEAAYgAQYQxiKBRgKwgILEC4YgAQY0QMYxwGYAwfiAwUSATEgQLoGBAgBGAqSBwYxLjEyLjKgB_JY&sclient=gws-wiz-serp

#########################
# Solution
#########################

#I imported the external files. The re stands for “regular expressions”, and helps to work with the methods of re.
import re

def extract_words(text):
    #In this part I got help from AI as I didn't know how dzongkha characters were represented
    words = re.findall(r'[\u0F00-\u0FFF]+', text) 
    return set(words)  
    
    #Here open() function opens a file in read mode ('r').The "utf-8" argument ensures that the file is read using UTF-8 encoding which handles various character sets.
with open("342.txt", encoding="utf-8") as file:
    content1 = file.read()
    word1 = extract_words(content1)
    # Again i opened the file using open() function to open the cleaned fileand it reads the content inside into the variable named content2.
with open("cleaned_file.txt", encoding="utf-8") as file:
    content2 = file.read()
    word2 =extract_words(content2)
    #In this part it calculates the difference between two sets word1 and word2.
unique_to_file1 = word1.difference(word2)  
    #This loop iterates over a collection of words and prtints out incorrect if there is difference in word1 and word2.
for word in unique_to_file1:
    print(f"The word '{word}' from 342.txt is incorrect.")
