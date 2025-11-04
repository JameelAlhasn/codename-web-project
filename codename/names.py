import requests
import random

# Quran unique word list
url = "https://raw.githubusercontent.com/a3f/arabic-wordlists/master/quran.wordlist"
url = "https://raw.githubusercontent.com/a3f/arabic-wordlists/master/propernames.wordlist"
url = "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2016/ar/ar_50k.txt"
r = requests.get(url)
r.raise_for_status()

# Clean up lines
words = [line.strip() for line in r.text.splitlines() if line.strip()]

# Show 25 random codenames
for word in random.sample(words, 25):
    print(word)
