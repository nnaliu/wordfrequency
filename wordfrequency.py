import csv
import operator

punctuation = [".",",","?","!",")","(","\"",":",";","'s","'","-","--","_","\\"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]

f = open('texts/ulysses.txt', 'r')
text = f.read();

freq = {}

def remove_punctuation(w):
	for p in punctuation:
	 	if p in w:
			w = w.replace(p,"")

	for n in numbers:
		if n in w:
			w = w.replace(n,"")
			
	return w

words = text.lower().split()

for w in words:
	w = remove_punctuation(w)
	if freq.has_key(w):
		freq[w] = freq[w] + 1
	else:
		freq[w] = 1

freq = sorted(freq.items(), key=lambda x:x[1], reverse = True)

with open('data/ulysses.csv','w') as out:
	csv_out = csv.writer(out)
	csv_out.writerow(['word','frequency'])
	for row in freq:
		csv_out.writerow(row)
