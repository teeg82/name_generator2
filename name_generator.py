from gram_frequency import (
	ALL_GRAMS_LETTERS, 
	ALL_GRAMS_VOWELS, 
	ALL_GRAMS_LETTERS_WEIGHT, 
	ALL_GRAMS_VOWELS_WEIGHT,
	WORD_BEGIN_LETTER, 
	WORD_BEGIN_VOWEL,
	WORD_BEGIN_LETTER_WEIGHT,
	WORD_BEGIN_VOWEL_WEIGHT, 
	WORD_END_LETTER,
	WORD_END_VOWEL, 
	WORD_END_LETTER_WEIGHT,
	WORD_END_VOWEL_WEIGHT
)
import random

def generate_name(gram_count=4, name_count=2):
	names = []
	
	for name_count_index in range(name_count):
		name = ""
		use_vowel = bool(random.getrandbits(1))
		
		if type(gram_count) is tuple:
			target_gram_count = int(random.uniform(gram_count[0], gram_count[1] + 1))
		else:
			target_gram_count = gram_count
		for gram_count_index in range(target_gram_count):
			if gram_count_index == 0:
				if use_vowel:
					start_gram_collection = WORD_BEGIN_VOWEL
					start_gram_weight = WORD_BEGIN_VOWEL_WEIGHT
				else:
					start_gram_collection = WORD_BEGIN_LETTER
					start_gram_weight = WORD_BEGIN_LETTER_WEIGHT
					
				rand_val = random.uniform(0, start_gram_weight)
				gram = fetch_gram(rand_val, start_gram_collection)
			elif gram_count_index == (target_gram_count - 1):
				if use_vowel:
					end_gram_collection = WORD_END_VOWEL
					end_gram_weight = WORD_END_VOWEL_WEIGHT
				else:
					end_gram_collection = WORD_END_LETTER
					end_gram_weight = WORD_BEGIN_LETTER_WEIGHT
				rand_val = random.uniform(0, end_gram_weight)
				gram = fetch_gram(rand_val, end_gram_collection)
			else:
				if use_vowel:
					gram_collection = ALL_GRAMS_VOWELS
					gram_weight = ALL_GRAMS_VOWELS_WEIGHT
				else:
					gram_collection = ALL_GRAMS_LETTERS
					gram_weight = ALL_GRAMS_LETTERS_WEIGHT
				rand_val = random.uniform(0, gram_weight)
				gram = fetch_gram(rand_val, gram_collection)
			
			name += gram
			use_vowel = not use_vowel
		names.append(name)
	
	return " ".join(names).title()

def fetch_gram(rand_val, gram_list):
	upto = 0
	for gram, weight in gram_list.items():
		if upto + weight >= rand_val:
			return gram
		upto += weight
	assert False, "shouldn't get here"