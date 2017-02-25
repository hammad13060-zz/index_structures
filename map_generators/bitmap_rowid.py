from math import ceil

headFile = 'data-0.txt'

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

secondary_index = {amount + 1: 'null' for amount in range(5 * 10**4)}
# storing bitmap to file
for amount, rowids in bitmap_table.items():
	fileId = 0
	for stride in range(ceil(len(rowids) / 1000)):
		startIndex = stride * 1000
		boundaryIndex = startIndex  + 1000
		fileName = '{}-{}.txt'.format(amount, fileId)
		if fileId == 0:
			secondary_index[amount] = fileName
		fileId += 1
		nextFile = '{}-{}.txt'.format(amount, fileId)
		if boundaryIndex > len(rowids): 
			boundaryIndex = len(rowids)
			nextFile = 'null'
		fileObject = open('./maps/bitmap_rowid/' + fileName, "w")
		data = '{}\n{}'.format(' '.join([str(i) for i in rowids[startIndex:boundaryIndex]]), nextFile)
		fileObject.write(data)
		fileObject.close()

# storing secondary index to file
data = ''
for amount, file in secondary_index.items():
	if file != 'null':
		data += '{} {}\n'.format(amount, file)
o = open('./secondary_indexes/' + 'bitmap_rowid.txt', 'w')
o.write(data)
o.close()