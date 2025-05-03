# In Python, you can remove prefixes from strings using the .removeprefix() method (available in Python 3.9 and above).

text = "unhappy"
cleaned = text.removeprefix("un")
print(cleaned)  # Output: "happy"


# .removeprefix() removes the prefix only if it exists at the start of the string.
# If the prefix is not present, the string remains unchanged.

text = "unhappy"
prefix = "un"
if text.startswith(prefix):
    text = text[len(prefix):]
print(text)  # Output: "happy"


nostarch_url = 'https://www.youtube.com/'
nostarch_url.removeprefix('https://')
print('www.youtube.com/')

nostarch_url = 'https://github.com/muhammadasif4485'
nostarch_url.removeprefix('https://')
print('github.com/muhammadasif4485')
# In Python, you can also remove suffixes from strings using the .removesuffix() method (available in Python 3.9 and above).
