print("""
(1) what is varibale?
In Python, a variable is like a container that holds data or a value. 
You can think of it as a name that refers to something stored in the computer's memory.

x = 10
name = "Muhammad Asif"
is_active = True

x is a variable that holds the number 10
name holds the string "Muhammad Asif"
is_active holds the Boolean value True
""")


print("""
(2) Rules for Naming Variables:
Must start with a letter or an underscore (_)
Cannot start with a number
Can only contain letters, numbers, and underscores
Case-sensitive (name and Name are different)
Avoid using Python keywords as variable names (like if, class, for, etc.)

Examples of valid variable names:
age = 25
_first_name = "Ali"
user_123 = "John"
""")

print("""
(3)Naming and Using Variables
When you’re using variables in Python, you need to adhere to a few rules and guidelines. Breaking some of these rules will cause errors; other guide- lines just help you write code that’s easier to read and understand. Be sure to keep the following rules in mind when working with variables:
• Variable names can contain only letters, numbers, and underscores. They can start with a letter or an underscore, but not with a number. For instance, you can call a variable message_1 but not 1_message.
• Spaces are not allowed in variable names, but underscores can be used to separate words in variable names. For example, greeting_message works but greeting message will cause errors.
• Avoid using Python keywords and function names as variable names. For example, do not use the word print as a variable name; Python has reserved it for a particular programmatic purpose. (See “Python Keywords and Built-in Functions” on page 466.)
• Variable names should be short but descriptive. For example, name is better than n, student_name is better than s_n, and name_length is better than length_of_persons_name.
• Be careful when using the lowercase letter l and the uppercase letter O because they could be confused with the numbers 1 and 0.
It can take some practice to learn how to create good variable names, especially as your programs become more interesting and complicated. As you write more programs and start to read through other people’s code, you’ll get better at coming up with meaningful names.

NOTE The Python variables you’re using at this point should be lowercase. You won’t get errors if you use uppercase letters, but uppercase letters in variable names have spe- cial meanings that we’ll discuss in later chapters.
""")