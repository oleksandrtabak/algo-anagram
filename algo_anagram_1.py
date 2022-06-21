def is_anagram(string1, string2):
    
    # Словники для підрахунку букв
    string1_letters = {}
    string2_letters = {}

    # Підрахунок слів у першому слові
    for letter in string1:
        if letter.lower() in string1_letters:
            string1_letters[letter.lower()] += 1
        else:
            string1_letters[letter.lower()] = 1

    # Підрахунок слів у другому слові
    for letter in string2:
        if letter.lower() in string2_letters:
            string2_letters[letter.lower()] += 1
        else:
            string2_letters[letter.lower()] = 1

    # Порівняння наборів слів
    anagram = True
    for letter, count in string1_letters.items():
        if letter in string2_letters and string2_letters[letter] != count:
            anagram = False
            break
        elif not letter in string2_letters:
            anagram = False
            break

    # Повернення результату на основі булевої змінної
    return anagram    

is_anagram('Wordee', 'worDee')
