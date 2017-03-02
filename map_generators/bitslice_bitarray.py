from math import ceil

headFile = 'data-0.txt'

bitmap_array_len = 2 * 10 ** 6
bitmap_block_size = 32000
bitmap_table = {bit: [] for bit in range(12)} # ceil(log2(2500)) = 12

while (headFile != 'null'):
    fileObject = open('./database/' + headFile, 'r')
    lines = fileObject.readlines()
    nextFile = lines[-1]
    records = [line.strip('\n').split(' ') for line in lines[:-1]]
    records = [[int(record[0]), int(record[1]), record[2]] for record in records]
    for record in records:
        index = record[0]
        amount = record[1]
        binaryString = bin(amount)[2:]
        l = len(binaryString)
        for idx in range(l-1,-1,-1):
            x = int(binaryString[idx])
            bit = (l-1) - idx
            if x == 1 : bitmap_table[bit].append(index)
    headFile = nextFile
    fileObject.close()

secondary_index = {bit: 'null' for bit in range(12)}

for bit, rowids in bitmap_table.items():
    bitmap = [0 for i in range(bitmap_array_len)]
    for rowid in rowids:
        bitmap[rowid] = 1

    # storing bitmap for bit
    fileId = 0
    for stride in range(ceil(bitmap_array_len / bitmap_block_size)):
        startIndex = stride * bitmap_block_size
        boundaryIndex = startIndex + bitmap_block_size
        fileName = '{}-{}.txt'.format(bit, fileId)
        if fileId == 0:
            secondary_index[bit] = fileName
        fileId += 1
        nextFile = '{}-{}.txt'.format(bit, fileId)
        if boundaryIndex > bitmap_array_len:
            boundaryIndex = bitmap_array_len
            nextFile = 'null'
        fileObject = open('./maps/bitslice_bitarray/' + fileName, "w")
        data = '{}\n{}'.format('\n'.join([str(i) for i in bitmap[startIndex:boundaryIndex]]), nextFile)
        fileObject.write(data)
        fileObject.close()


# storing secondary index to file
data = ''
for bit, file in secondary_index.items():
    data += '{} {}\n'.format(bit, file)
o = open('./secondary_indexes/' + 'bitslice_bitarray.txt', 'w')
o.write(data)
o.close()