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


def get_words_from_file(filename):
    with open(filename, encoding="utf-8") as file:
        content = file.read()
    
    words = content.split()
    # Return unique words
    return set(words)

# Read words from both files
words_in_dictionary = get_words_from_file("342.txt")
words_in_cleanedfile = get_words_from_file("cleaned_file.txt")

# Find difference in words
unique_words = words_in_dictionary.difference(words_in_cleanedfile)

# Output each unique word from dictionary
for word in unique_words:
    print(f"The word '{word}' from 342.txt is incorrect.")


