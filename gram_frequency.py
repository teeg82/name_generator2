WORD_BEGIN_LETTER = {
"t": 0.1594,
"s": 0.0775,
"c": 0.0597,
"m": 0.0426,
"f": 0.0408,
"p": 0.040,
"w": 0.0382
}

WORD_BEGIN_VOWEL = {
"a": 0.155,
"i": 0.0823,
"o": 0.0712
}

WORD_BEGIN_LETTER_WEIGHT = sum(weight for gram, weight in WORD_BEGIN_LETTER.items())
WORD_BEGIN_VOWEL_WEIGHT = sum(weight for gram, weight in WORD_BEGIN_VOWEL.items())

WORD_END_LETTER = {
"s": 0.1435,
"d": 0.0923,
"t": 0.0864,
"n": 0.0786,
"y": 0.0730,
"r": 0.0693,
"l": 0.0456,
"f": 0.0408
}

WORD_END_VOWEL = {
"e": 0.1917,
"o": 0.0467,
}

WORD_END_LETTER_WEIGHT = sum(weight for gram, weight in WORD_END_LETTER.items())
WORD_END_VOWEL_WEIGHT = sum(weight for gram, weight in WORD_END_VOWEL.items())

GRAMS_LETTER = {
'c': 0.02782, 
'b': 0.01492, 
'd': 0.04253, 
'g': 0.02015, 
'f': 0.02228, 
'h': 0.06094, 
'k': 0.00772, 
'j': 0.00153, 
'm': 0.02406, 
'l': 0.04025, 
'n': 0.06749, 
'q': 0.00095, 
'p': 0.01929, 
's': 0.06327, 
'r': 0.05987, 
't': 0.09056, 
'w': 0.0236, 
'v': 0.00978, 
'x': 0.0015, 
'z': 0.00074
}

GRAMS_VOWEL = {
'a': 0.08167, 
'e': 0.12702, 
'i': 0.06966, 
'o': 0.07507, 
'u': 0.02758, 
'y': 0.01974
}

BIGRAMS_LETTER = {
'th': 0.03882543,
'he': 0.03681391,
're': 0.01749394,
'nd': 0.01571977,
'ha': 0.01274742,
'to': 0.01169655,
'hi': 0.01092302,
'ng': 0.01053385
}

BIGRAMS_VOWEL = {
'in': 0.02283899,
'er': 0.02178042,
'an': 0.02140460,
'on': 0.01418244,
'en': 0.01383239,
'at': 0.01335523,
'ou': 0.01285484,
'ed': 0.01275779,
'or': 0.01151094,
'it': 0.01134891,
'is': 0.01109877,
'es': 0.01092301
}

TRIGRAMS_LETTER = {
'he': 0.03508232,
'nd': 0.01593878,
'ng': 0.01147042,
'ha': 0.00593593,
're': 0.00560594,
'ter': 0.00461099,
'was': 0.00460487,
'ver': 0.00430732,
'wit': 0.00397290,
'thi': 0.00394796,
'tio': 0.00378058
}

TRIGRAMS_VOWEL = {
'er': 0.00822444,
'at': 0.00650715,
'is': 0.00596748,
'or': 0.00555372,
'ent': 0.00530771,
'ion': 0.00506454,
'you': 0.00437213,
'ith': 0.00431250,
'all': 0.00422758
}

QUADRIGRAMS_LETTER = {
'that': 0.00761242,
'ther': 0.00604501,
'with': 0.00573866,
'tion': 0.00551919,
'have': 0.00290544,
'hich': 0.00284292,
'whic': 0.00283826,
'this': 0.00276333,
'thin': 0.00270413,
'they': 0.00262421,
'from': 0.00258580,
'were': 0.00231089,
'hing': 0.00229944,
'ment': 0.00223347
}

QUADRIGRAMS_VOWEL = {
'ould': 0.00369920,
'ight': 0.00309440,
'atio': 0.00262386,
'ever': 0.00260695,
'ough': 0.00253447,
}

# ALL_GRAMS = dict(GRAMS.items() + BIGRAMS.items() + TRIGRAMS.items() + QUADRIGRAMS.items())
#ALL_GRAMS = dict(GRAMS.items() + BIGRAMS.items())
#ALL_GRAMS = dict(BIGRAMS.items() + TRIGRAMS.items())
#ALL_GRAMS_LETTERS = dict(GRAMS_LETTER.items() + BIGRAMS_LETTER.items() + TRIGRAMS_LETTER.items() + QUADRIGRAMS_LETTER.items())
#ALL_GRAMS_VOWELS = dict(GRAMS_VOWEL.items() + BIGRAMS_VOWEL.items() + TRIGRAMS_VOWEL.items() + QUADRIGRAMS_VOWEL.items())
ALL_GRAMS_LETTERS = dict(GRAMS_LETTER.items() + BIGRAMS_LETTER.items() + TRIGRAMS_LETTER.items())
ALL_GRAMS_VOWELS = dict(GRAMS_VOWEL.items() + BIGRAMS_VOWEL.items() + TRIGRAMS_VOWEL.items())
ALL_GRAMS_LETTERS_WEIGHT = sum(weight for gram, weight in ALL_GRAMS_LETTERS.items())
ALL_GRAMS_VOWELS_WEIGHT = sum(weight for gram, weight in ALL_GRAMS_VOWELS.items())