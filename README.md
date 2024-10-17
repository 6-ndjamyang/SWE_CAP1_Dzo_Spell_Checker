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
1. Time Complexity:
* Dictionary Loading: O(D), where D is the number of words in the dictionary.
* Spell Checking (for N words): O(N), where N is the number of words in the input text.

* Total Time Complexity:
O(D + N + M * D * L)

2. Space Complexity:
* Dictionary Storage: O(D * L), where L is the average word length.
* Input Text Storage: O(N * W), where W is the average length of words in the input text.

* Total Space Complexity:
O(D * L + N * W)

## Challenges and Solutions
1. Character Encoding Issues:

    * Challenge: Misinterpretation of Dzongkha characters due to inconsistent encodings.
    * Solution: Use UTF-8 encoding consistently.

2. Dictionary Completeness:

    * Challenge: Missing words can lead to false positives.
    * Solution: Continuously update and expand the dictionary.

3. Handling Compound Words and Affixes:

    * Challenge: Missed valid words due to compounds and affixes not in the dictionary.
    * Solution: Recognize common compounds and affixes.
4. User Interface and Usability:

    * Challenge: Difficulty for non-technical users to utilize the tool.
    * Solution: Develop a user-friendly GUI.
5. Performance with Large Files:

    * Challenge: Slow processing times with large input and dictionary files.
    * Solution: Optimize algorithms for better performance.
6. Regular Expression Limitations:

    * Challenge: Edge cases may not be handled correctly.
    * Solution: Thoroughly test and adjust regex patterns.
7. Maintenance and Updates:

    * Challenge: Keeping the dictionary current can be resource-intensive.
    * Solution: Establish a regular update process.
8. Error Handling:

    * Challenge: Robust error handling for file operations is needed.
    * Solution: Implement thorough exception handling.

## References
1. Dzongkha Language Resources
    * Dzongkha Unicode. (n.d.). Unicode Consortium. Retrieved from https://www.unicode.org/charts/PDF/U0F00.pdf 
2. Programming Libraries and Tools
    * python-docx. (n.d.). python-docx Documentation. Retrieved from https://python-docx.readthedocs.io/en/latest/
    * Requests: HTTP for Humans. (n.d.). Requests Documentation. Retrieved from https://docs.python-requests.org/en/latest/
    * Regular Expressions. (n.d.). Python re module documentation. Retrieved from https://docs.python.org/3/library/re.html
    * AI like chatGPT, BlackBox