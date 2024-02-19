"""
# re's validate the users input 
[]	A set of characters	                                                            : "[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	    : "\d"	
.	Any character (except newline character)           	                            : "he..o"	
^	Starts with	                                                                    : "^hello"	
$	Ends with	                                                                    : "planet$"	
*	Zero or more occurrences                                                        : "he.*o"	
+	One or more occurrences	                                                        : "he.+o"	
?	Zero or one occurrences	                                                        : "he.?o"	
{}	Exactly the specified number of occurrences	                                    : "he.{2}o"	
|	Either or	                                                                    : "falls|stays"	
()	Capture and group
[^] Complementing the set                                                           : [^@]  means anything except @ symbol

\d          : decimal digit
\D          : not a decimal digit
\s          : whitespace characters
\S          : not a whitespace character
\w          : word character ... as well as numbers and the underscore
\W          : not a word : maybe . symbol or something like that

re.IGNORECASE
re.MULTILINE
re.
A|B         : either A or B

"""

import re

email = input("What's your email : ").strip()

if re.search(r"^\w+@(\w+\.)?\.edu|\.com", email, re.IGNORECASE):           #(\w+\.)?\.edu|\.com : this entire expression is for sub domain 
    print("Valid")
else:
    print("Invalid")
