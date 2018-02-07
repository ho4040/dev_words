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


invalid_files = []
for filename in glob2.glob('./invalid_data_source/**/*.txt'):
    invalid_files.append(filename)

for path in invalid_files:
  document_text = open(path, 'r')
  text_string = document_text.read().lower().strip()
  match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
   
  for word in match_pattern:
      count = frequency.get(word,0)
      frequency[word] = count - 1
       
frequency_word_list = frequency.keys()
frequency_data_list = []
for words in frequency_word_list:
    frequency_data_list.append([words, frequency[words]])

frequency_data_list = sorted(frequency_data_list, key=lambda item: item[1], reverse=True)

for i in range(5000):
  print("{}, {}".format(frequency_data_list[i][0], frequency_data_list[i][1]))