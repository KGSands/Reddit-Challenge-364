# https://www.reddit.com/r/dailyprogrammer/comments/8s0cy1/20180618_challenge_364_easy_create_a_dice_roller/
# Input:  #die, #sides
# e.g. "3d6" = 3 die, 6-sided
# Output: sum of die outputs and each die output
# e.g. 12: [6, 4, 2]

import numpy as np

while True:
	user_input = input("Enter: ").split('d')
	num_die = int(user_input[0])
	num_sides = int(user_input[1])
	die_outputs = []

	for i in range(int(num_die)):
		die_outputs.append(np.random.randint(num_sides)+1)

	die_sum = np.sum(die_outputs)
	print(die_sum, ' : ', die_outputs)