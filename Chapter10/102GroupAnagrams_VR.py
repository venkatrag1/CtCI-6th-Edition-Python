def GroupAnagrams():
    strings = initialise_anagrams()
    anagrams = {}
    for s in strings:
        key = ''.join(sorted(s)).lower()
        if key not in anagrams:
            anagrams.setdefault(key, [])
        anagrams[key].append(s)
    k = 0
    for key, strarr in anagrams.items():
        for s in strarr:
            strings[k] = s
            k += 1
    print strings


def initialise_anagrams():
    strings = [0] * 8
    strings[0] = "abed"
    strings[1] = "later"
    strings[2] = "bead"
    strings[3] = "alert"
    strings[4] = "altered"
    strings[5] = "bade"
    strings[6] = "alter"
    strings[7] = "alerted"
    return strings

GroupAnagrams()
