from gram_frequency import ALL_GRAMS, ALL_GRAM_WEIGHT, WORD_BEGIN, WORD_BEGIN_WEIGHT, WORD_END, WORD_END_WEIGHT
import random

def generate_name(gram_count=4, name_count=2):
	names = []
	
	for name_count_index in range(name_count):
		name = ""
		for gram_count_index in range(gram_count):
			if gram_count_index == 0:
				rand_val = random.uniform(0, WORD_BEGIN_WEIGHT)
				gram = fetch_gram(rand_val, WORD_BEGIN)
			elif gram_count_index == (gram_count - 1):
				rand_val = random.uniform(0, WORD_END_WEIGHT)
				gram = fetch_gram(rand_val, WORD_END)
			else:
				rand_val = random.uniform(0, ALL_GRAM_WEIGHT)
				gram = fetch_gram(rand_val, ALL_GRAMS)
			
			name += gram
		names.append(name)
	
	return " ".join(names)

def fetch_gram(rand_val, gram_list):
	upto = 0
	for gram, weight in gram_list.items():
		if upto + weight >= rand_val:
			return gram
		upto += weight
	assert False, "shouldn't get here"