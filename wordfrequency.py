import csv
import operator

punctuation = [".",",","?","!",")","(","\"",":",";","'s","'","-","--","_","\\"]

f = open('ulysses.txt', 'r')
text = f.read();

freq = {}

def remove_punctuation(w):
	for p in punctuation:
	 	if p in w:
				w = w.replace(p,"")
	return w

words = text.lower().split()

for w in words:
	w = remove_punctuation(w)
	if freq.has_key(w):
		freq[w] = freq[w] + 1
	else:
		freq[w] = 1

freq = sorted(freq.items(), key=lambda x:x[1], reverse = True)
print(freq)

with open('ulysses-30.csv','w') as out:
	csv_out = csv.writer(out)
	csv_out.writerow(['word','frequency'])
	for row in freq:
		csv_out.writerow(row)
