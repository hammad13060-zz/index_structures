print('No Index Query Results\n')
for i in range(6):
	print('Experiment {}'.format(i+1))
	# query loading code
	fileName = 'query-{}.txt'.format(i)
	o = open('./queries/' + fileName, 'r')
	query = o.readlines()
	o.close()

	# evaluation code
	s = 0
	diskBlockCount = 0
	prev = -1
	blockSize = 300
	for qRowId in range(len(query)):
		bit = query[qRowId].strip('\n')
		if bit == '1':
			fileId = int(qRowId / blockSize)
			o = open('./database/data-{}.txt'.format(fileId), 'r')
			lines = o.readlines()
			line = lines[qRowId % blockSize].split(' ')
			amount = int(line[1])
			s += amount
			if prev != fileId: diskBlockCount += 1
			prev = fileId
			o.close()


	print('sum: {}'.format(s))
	print('disk block(s) accessed: {}'.format(diskBlockCount))
	print('\n')