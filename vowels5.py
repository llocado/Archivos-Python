vowels=["a","e","i","o","u"]
found={}
word=input("provide a word to search for vowels: ")

for letter in word:
    if letter in vowels:
        found[letter]+=1
for k,v in sorted(found.items()):
    print(k, "was found", v, "times(s).")