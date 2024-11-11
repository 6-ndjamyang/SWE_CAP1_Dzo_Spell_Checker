# Dzongkha Spell Checker

## Project Overview
This was a project for us to create a spell checker for Dzongkha.The spell checker reads an input text file containing Dzongkha words and checks each word with the dzongkha. The sole purpose of the this project is to check the misspelled dzongkha words. The main features I used in this project are downloading input and cleaning dictionary file

# Table of Contents

## Usage
The use of this project is to check the spelling of dzongkha wordsin between lines or paragraph. A input txt file is required which we want it to be checked comparing it with the provided dzongkha dictionary.

bash 
python SWE_CAP1_Dzo_Spell_Checker.py 342.txt


## Implementation
This project is constructed in such a way that each component is responsible for spell-checking process. it takes two input files a txt file containing the words to be checked, and a dzongkha dictionary file which has the correctly spelled Dzongkha words.


## Data Structures
File operations was used to open the files to read and write on the files, 'with open' file operation is used so that I can open the files to read line by line. 'string' operation is also used for processing the texts having the contents of the dictionary and input file which needs to be check for spelling error.


## Algorithms
1. Conversion Algorithm: Converting of word document file to txt file. 
2. Text Cleanup Algorithm: Removing non-dzongkha characters in the dzongkha dictionary.
3. Cleaned Dictionary Algorithm: It reads the cleaned dictionary file.
4. Spell Checker Algorithm: iterates through each word in the input file and checks its existence in the dictionary.

## Performance Analysis
The code has a time complexity of O(n) where n is the number of words in the text

## Challenges And Solutions
1. problem : It was difficult for me to get the right links and guides on the internet to tackle the problem.
2. problem : One of the main challenge was to clear the non-dongkha characters from the dzongkha dictionary, and comparing it with the given txt, i had no idea how to go about with the problem.
1. solution : AI Copilot guided me with the links to videos and sometimes with codelines.
2. solution : by using UTF-8 encoding helped me remove non-dzongkha characters.


## References
1. Dzongkha Resources
    * [Dzongkha Unicode. (n.d.). Unicode Consortium]('https://www.unicode.org/charts/PDF/U0F00.pdf') 
2. Programming Libraries and Tools
    * [YouTube Video](https://www.youtube.com/watch?v=Mi3j54ZMxOc)
    * #https://www.youtube.com/watch?v=L2BDTy4bEcg
    
    * AI like chatGPT, Copilot, BlackBox