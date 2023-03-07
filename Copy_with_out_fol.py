import re

# assume data is a byte string containing the input data


# Replace line breaks, end-of-line characters, and multiple spaces with a single space

with open('1.txt', 'r') as file:
    
    text = file.read().replace('\n', ' ').replace('\r', ' ')
    text = re.sub(r'\s{2,}', ' ', text)
    print(text)