from pyspark import SparkContext
text_file = SparkContext.textFile(FileName.txt)#https://www.gutenberg.org/files/2600/2600-0.txt
type(text_file)

words = text_file.flatMap(lambda line: line.split(" "))
not_empty = words.filter(lambda x: x!='')
key_values= not_empty.map(lambda word: (word, 1))
counts=     key_values.reduceByKey(lambda a, b: a + b)

print(counts.toDebugString().decode())

#Run

Count=counts.count() # Count = the number of different words
Sum=counts.map(lambda x:x[1]).reduce(lambda x,y:x+y) 
print(Count)
