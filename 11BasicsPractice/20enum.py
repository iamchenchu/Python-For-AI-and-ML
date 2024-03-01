"""
* Enumerations in Python are implemented by using the module named “enum“. Enumerations are created using classes. Enums have names and
  values associated with them. Let’s cover the different concepts of Python Enum in this article.
* Enumerations or Enums is a set of symbolic names bound to unique values. It can be iterated over to return its canonical members in often
  definition order. It provides a way to create more readable and self-documenting code by using meaningful names instead of arbitrary values.

* Properties of Enum : Enums can be displayed as string or repr.
Enums can be checked for their types using type().
The “name” keyword is used to display the name of the enum member.

What are the Advantages of Enum
    Some of the advantages of using enums include:
    Ease of maintenance: Enums centralize the definition of name values which makes it easier to upgrade or extend the set of values as per our requirements.
    Readability and Self-Documentation: Enums provide meaningful names to values, making the code more human-readable and self-explanatory.
    Type safety: Enums provide some level of type safety, ensuring that only valid values can be used.
    Reduced risk of errors: Enums help prevent the use of incorrect or inconsistent values in your code, reducing the risk of bugs and errors.
"""

from enum import Enum

class Season(Enum):
	SPRING = 1
	SUMMER = 2
	AUTUMN = 3
	WINTER = 4
print(Season.SPRING)
print(Season.SPRING.name)
print(Season.SPRING.value)
print(type(Season.SPRING))
print(repr(Season.SPRING))
print(list(Season))

print()
print()

