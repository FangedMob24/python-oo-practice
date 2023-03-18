"""Word Finder: finds random words from a dictionary."""
from random import choice as random_word


class WordFinder:
    """Will read in a dictionary and print a random word from it"""
    def __init__(self,file_location):
        """will initialize the location of the file and call the function to read in the dictionary"""
        self.file_location = file_location
        self.dict_of_words = self.read_in_words()
        print(f"{len(self.dict_of_words)} words read")
        

    def read_in_words(self):
        """Reads in the dictionary into a variable"""
        words = []
        with open(self.file_location,"r") as file:
            for line in file:
                words.append(line.strip())
        return words
    
    def random(self):
        """Selects one random word"""
        return random_word(self.dict_of_words)
    
class SpecialWordFinder(WordFinder):
    """Will edit the list of words to remove comments and blank lines"""
    def __init__(self,dict_location):
        super().__init__(dict_location)
        self.dict_of_words = [word for word in self.dict_of_words if word != "" and word.startswith("#") == False]