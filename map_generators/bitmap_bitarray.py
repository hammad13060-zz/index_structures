from math import ceil
import gzip

headFile = 'data-0.txt'

bitmap_array_len = 2 * 10 ** 6
bitmap_block_size = 32000
bitmap_table = {amount + 1: [] for amount in range(5 * 10**4)}

while (headFile != 'null'):
	fileObject = open('./database/' + headFile, 'r')
	lines = fileObject.readlines()
	nextFile = lines[-1]
	records = [line.strip('\n').split(' ') for line in lines[:-1]]
	records = [[int(record[0]), int(record[1]), record[2]] for record in records]
	for record in records:
		index = record[0]
		amount = record[1]
		bitmap_table[amount].append(index)
	headFile = nextFile
	fileObject.close()

secondary_index = {amount+1: 'null' for amount in range(5 * 10**4)}

for amount, rowids in bitmap_table.items():
	bitmap = [0 for i in range(bitmap_array_len)]
	for rowid in rowids:
		bitmap[rowid] = 1

	# storing bitmap for amount
	fileId = 0
	for stride in range(ceil(bitmap_array_len / bitmap_block_size)):
		startIndex = stride * bitmap_block_size
		boundaryIndex = startIndex + bitmap_block_size
		fileName = '{}-{}.txt.gz'.format(amount, fileId)
		if fileId == 0:
			secondary_index[amount] = fileName
		fileId += 1
		nextFile = '{}-{}.txt.gz'.format(amount, fileId)
		if boundaryIndex > bitmap_array_len:
			boundaryIndex = bitmap_array_len
			nextFile = 'null'
		data = '{}\n{}'.format('\n'.join([str(i) for i in bitmap[startIndex:boundaryIndex]]), nextFile)
		fileObject = gzip.open('./maps/bitmap_bitarray/' + fileName, 'wb')
		fileObject.write(bytearray(data, 'utf-8'))

# storing secondary index to file
data = ''
for amount, file in secondary_index.items():
	if file != 'null':
		data += '{} {}\n'.format(amount, file)
o = open('./secondary_indexes/' + 'bitmap_bitarray.txt', 'w')
o.write(data)
o.close()
