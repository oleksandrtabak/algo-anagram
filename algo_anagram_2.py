def is_anagram(string1, string2):

    # Видалення пробілів та зведення до малих літер 
    string1 = string1.replace(' ', '').lower()
    string2 = string2.replace(' ', '').lower()

    return sorted(string1) == sorted(string2)
