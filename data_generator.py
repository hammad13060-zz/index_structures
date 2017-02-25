import random, string

totalRecords = 2 * (10**6) # 20 Lakhs

filePrefix = 'data'
createFile = True
fileId = 0
fileObject = 'abc'
blockRecordCount = 0
for i in range(totalRecords):
	random_record = [
		i, random.randint(1, 5 * (10 ** 4)),
		''.join([random.choice(string.ascii_lowercase) for j in range(3)])
	]
	if createFile:
		fileName = '{}-{}.txt'.format(filePrefix, fileId)
		if fileObject != 'abc':
			fileObject.write(fileName)
			fileObject.close()
		fileId += 1
		fileObject = open('./database/' + fileName, "w")
		createFile = False

	fileObject.write('{} {} {}\n'.format(random_record[0], random_record[1], random_record[2]))

	blockRecordCount += 1

	if blockRecordCount == 300:
		createFile = True
		blockRecordCount = 0

if fileObject != 'abc':
	fileObject.write('null')
	fileObject.close()
