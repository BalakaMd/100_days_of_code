import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {}
# Loop through rows of a data frame
for (index, row) in data.iterrows():
    phonetic_dict[row.letter] = row.code


# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Insert value: ").upper()
code_list = [phonetic_dict[latter] for latter in user_input]

print(code_list)

