from math import ceil

headFile = 'data-0.txt'

amount_set = set()
bitmap_array_len = 2 * 10 ** 6
bitmap_block_size = 32000
while headFile != 'null':
	fileObject = open('./database/' + headFile, 'r')
	lines = fileObject.readlines()
	nextFile = lines[-1]
	for line in lines[:-1]:
		amount = int(line.split(' ')[1])
		amount_set.add(amount)
	headFile = nextFile
	fileObject.close()

secondary_index = {amount: 'null' for amount in amount_set}

for amount in amount_set:
	headFile = 'data-0.txt'
	bitmap = [0 for i in range(bitmap_array_len)]
	while (headFile != 'null'):
		fileObject = open('./database/' + headFile, 'r')
		lines = fileObject.readlines()
		nextFile = lines[-1]
		for line in lines[:-1]:
			record = line.strip('\n').split(' ')
			if amount == int(record[1]):
				bitmap[int(record[0])] = 1
		fileObject.close()
		headFile = nextFile

	# storing bitmap for amount
	fileId = 0
	for stride in range(ceil(bitmap_array_len / bitmap_block_size)):
		startIndex = stride * bitmap_block_size
		boundaryIndex = startIndex  + bitmap_block_size
		fileName = '{}-{}.txt'.format(amount, fileId)
		if fileId == 0:
			secondary_index[amount] = fileName
		fileId += 1
		nextFile = '{}-{}.txt'.format(amount, fileId)
		if boundaryIndex > bitmap_array_len: 
			boundaryIndex = bitmap_array_len
			nextFile = 'null'
		fileObject = open('./maps/bitmap_bitarray/' + fileName, "w")
		data = '{}\n{}'.format(' '.join([str(i) for i in bitmap]), nextFile)
		fileObject.write(data)
		fileObject.close()


# storing secondary index to file
data = ''
for amount, file in secondary_index.items():
	data += '{} {}\n'.format(amount, file)
o = open('./secondary_indexes/' + 'bitmap_bitarray.txt', 'w')
o.write(data)
o.close()