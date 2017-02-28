import random

total_bits = 2 * 10**6

one_bit_counts = [100000, 10000, 2000, 500, 100, 25]

for i in range(len(one_bit_counts)):
	one_bit_count = one_bit_counts[i]
	zero_bit_count = total_bits - one_bit_count
	query = ['1' for i in range(one_bit_count)] + ['0' for i in range(zero_bit_count)]
	random.shuffle(query)
	data = '\n'.join(query)
	o = open('./queries/query-{}.txt'.format(i), 'w')
	o.write(data)
	o.close()

