# To strip (remove) whitespace from a string in Python, you can use the strip() method.
# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) whitespace from a string.

text = "   Hello, World!   "
clean_text = text.strip()
print(clean_text)  # Output: "Hello, World!"

#strip() – removes both leading and trailing whitespace
# lstrip() – removes leading (left-side) whitespace
# rstrip() – removes trailing (right-side) whitespace

text = "   Hello   "
print(text.lstrip())  # Output: "Hello   "
print(text.rstrip())  # Output: "   Hello"
