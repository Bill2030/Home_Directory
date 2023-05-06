import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_data = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_data)

word = input("Enter a word \n").upper()
output_list = [phonetic_data[letter] for letter in word ]
print(output_list)


