import re
import string
import glob2

files = []
for filename in glob2.glob('./data_source/**/*.txt'):
    files.append(filename)


frequency = {}

for path in files:
  document_text = open(path, 'r')
  text_string = document_text.read().lower().strip()
  match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
   
  for word in match_pattern:
      count = frequency.get(word,0)
      frequency[word] = count + 1
       
frequency_list = frequency.keys()

for words in frequency_list:
    print "{},{}".format(words, frequency[words])
