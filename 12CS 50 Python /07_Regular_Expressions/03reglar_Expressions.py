"""
we can always make our code more precisly using other functionalities in the python but to handle this effectively we have a library called 
Regular Expressions (re). we can import re and perform certain actions to prevent the mistakes in the code
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

"""

import re  # imports the regular expression 

email = input("What's your email : ").strip()

if re.search(".+@+.", email):
    print("valid")
else:
    print("Invalid")
    



