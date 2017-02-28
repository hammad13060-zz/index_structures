print('Bitmap RowId Query Results\n')


secondary_index = {}
o = open('./secondary_indexes/bitmap_rowid.txt');
lines = o.readlines()
for line in lines:
	line = line.strip('\n').split(' ')
	secondary_index[int(line[0])] = line[1]
o.close()



for i in range(6):
	print('Experiment {}'.format(i+1))
	# query loading code
	fileName = 'query-{}.txt'.format(i)
	o = open('./queries/' + fileName, 'r')
	query = o.readlines()
	o.close()

	qRowIds = set([i for i in range(len(query)) if query[i].strip('\n') == '1'])

	s = 0
	diskBlockCount = 0
	for amount, headFile in secondary_index.items():
		rowIds = []
		while (headFile != 'null'):
			o = open('./maps/bitmap_rowid/{}'.format(headFile), 'r')
			lines = o.readlines()
			diskBlockCount += 1
			o.close()
			headFile = lines[-1]
			rowIds.extend([int(i.strip('\n')) for i in lines[:-1]])
		rowIds = set(rowIds)
		s += (len(rowIds.intersection(qRowIds)) * amount)

	print('sum: {}'.format(s))
	print('disk block(s) accessed: {}'.format(diskBlockCount))
	print('\n')


