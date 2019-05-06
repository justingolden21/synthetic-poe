import random

# input_text: the text used to generate our synthetic text
# size: number of characters we look back
# num_chars: the approx size of our output str
def synthesize(input_text, size, num_chars):
	# create char dict
	char_dict = {}
	# for every char except the last (size) chars
	for i in range(len(input_text)-size):

	  # our substring is (size) chars after index i
	  sub_str = input_text[i:i+size]

	  # make obj if doesnt exist
	  if not sub_str in char_dict:
	    char_dict[sub_str] = {}
	  # if we havent seen this combo before, init to 1, else incremement 
	  # number of times we've seen these size characters
	  #correspond to the next character after them
	  if not input_text[i+size] in char_dict[sub_str]:
	    char_dict[sub_str][input_text[i+size]] = 1
	  else:
	    char_dict[sub_str][input_text[i+size]] += 1

	# ----------------
	# generate ouput

	#our output str
	generated_sentence = ""

	# star us off at a random point in the input, to (size) chars
	# after that point (so we have context to begin our loop)
	rand_idx = random.randint(0, len(input_text)-size)
	generated_sentence += input_text[rand_idx:rand_idx+size]

	# for every char we want to make
	for i in range(num_chars-size):
	  # the next char is a weighted random char from our helper function
	  next_char = get_next_char(char_dict, generated_sentence[-size:])
	  # if we have no data, pick random char
	  if next_char == -1:
	    next_char = random.choice(input_text) #change this?
	  generated_sentence += next_char

	# ----------------
	# almost done, now fix the start and end

	# for end, we repeat above loop until an end of sentence character is found
	# keep adding chars like we did before until the last one is an end of sentence char
	while not isSentenceEnd(generated_sentence[-1]):
	  next_char = get_next_char(char_dict, generated_sentence[-size:])
	  if next_char == -1:
	    next_char = random.choice(input_text)

	  generated_sentence += next_char

	#delete chars from beginning until the first char is the char after an end of sentence char
	while not isSentenceEnd(generated_sentence[0]):
	  generated_sentence = generated_sentence[1:]
	generated_sentence = generated_sentence[1:]

	return generated_sentence

# ----------------
# helper functions

# given an input str of size (size), get a weighted random character
# given all combos of characters we've seen after that str
def get_next_char(char_dict, input_str):
  if input_str not in char_dict:
    return -1 # if we don't have data for that char, handle in loop

  rand_max = 0 #number of all total times that sequence occured
  for key in char_dict[input_str]:
    rand_max += char_dict[input_str][key]

  # choose a random one of those sequences  
  rand_choice = random.randint(0, rand_max)

  for key in char_dict[input_str]:
    rand_choice -= char_dict[input_str][key]
    # and choose the character at that index
    if rand_choice <= 0:
      return key

# returns true if given char is an end of sentence char
def isSentenceEnd(test_char):
  return test_char in ". ! ? \n".split(" ")
