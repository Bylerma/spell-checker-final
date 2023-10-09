import re
from spellchecker import SpellChecker

def fix_misspellings(text, spell_checker):
    # Tokenize the text into words
    words = re.findall(r'\b\w+\b', text)

    # Initialize a dictionary to store corrections
    corrections = {}

    for word in words:
        # Check if the word is misspelled
        if not spell_checker.correction(word.lower()) == word.lower():
            # Store the corrected word
            corrections[word] = spell_checker.correction(word.lower())

    # Replace misspelled words with corrections in the text
    for misspelled, corrected in corrections.items():
        text = text.replace(misspelled, corrected)

    return text

