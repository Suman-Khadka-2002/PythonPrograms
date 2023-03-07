import re

# words that start with letter 'a'
pattern1 = r"^a.*"
word1 = "apple"

# pattern that matches the word that ends with a
pattern2 = r".*a$"
word2 = "a"

# pattern that matches the word that has one or more characters from a-z A-Z and 0-9

pattern3 = r"[a-zA-Z0-9]+"
word3 = "sumangoleG112G"

print(re.match(pattern3, word3))
print(re.match(pattern1, word1))
print(re.match(pattern2, word2))
