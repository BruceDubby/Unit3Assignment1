# inspired by https://exercism.io/tracks/javascript/exercises/etl/solutions/91f99a3cca9548cebe5975d7ebca6a85


old_point_structure = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

def old_scrabble_scorer(word):
    word = word.upper()
    letterPoints = ""

    for char in word:

        for point_value in old_point_structure:

            if char in old_point_structure[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)

    return letterPoints

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

def initial_prompt():
   print("Let's play some Scrabble!\n")
   user_word = input("Enter a word to score: ")
   return user_word


def simple_scorer(word):
    return len(word)

def vowel_bonus_scorer(word):
    vowels = "aeiou"
    count = 0
    for char in word:
        if char in vowels.lower():
            count += 3
        else:
            count += 1
    return count

def scrabble_scorer(word):
    
    letterPoints = 0

    for char in word.lower():
        if char in new_point_structure:
            letterPoints += new_point_structure[char]

    return letterPoints


scoring_algorithms = ({"Name": "Simple Score", "Description": "Each letter is worth 1 point.", "Score Function": "A function with a parameter for user input that returns a score."},
                      {"Name": "Bonus Vowels", "Description" : "Vowels are 3 pts, consonants are 1 pt.", "Score Function" : "A function that returns a score based on the number of vowels and consonants. "},
                      {"Name": "Scrabble", "Description" : "The traditional scoring algorithm.", "Score Function" : "Uses the old_scrabble_scorer() function to determine the score for a given word."})
    #{old_scrabble_scorer(), simple_scorer(), vowel_bonus_scorer()}

def scorer_prompt(word):
    print(f"Which scoring algorithm would you like to use?\n"
          f"0 - {scoring_algorithms[0]['Name']}: {scoring_algorithms[0]['Description']}\n"
          f"1 - {scoring_algorithms[1]['Name']}: {scoring_algorithms[1]['Description']}\n"
          f"2 - {scoring_algorithms[2]['Name']}: {scoring_algorithms[2]['Description']}")

    which_game = int(input("Enter 0, 1, or 2\n"))
    if which_game == 0:
        print(f"{scoring_algorithms[0]['Name']} it is!")
        return simple_scorer(word)
    elif which_game == 1:
        print(f"{scoring_algorithms[1]['Name']} it is!")
        return vowel_bonus_scorer(word)
    elif which_game == 2:
        print(f"{scoring_algorithms[2]['Name']} it is!")
        #print(old_scrabble_scorer(word))
        return scrabble_scorer(word)
        
    else:
        print("not a valid choice")
    
def transform(old_point_structure):
    new_dict = {}
    for (key, value) in old_point_structure.items():
        for letter in value:
            new_dict[letter.lower()] = key
    return new_dict

new_point_structure = transform(old_point_structure)

def run_program():
    word = initial_prompt()
    #print(old_scrabble_scorer(word))    
    scorer_prompt(word)
    output = scrabble_scorer(word)
    print(f"Score for {word}: {output}")