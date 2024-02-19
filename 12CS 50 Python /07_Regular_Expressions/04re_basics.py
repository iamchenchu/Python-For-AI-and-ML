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
[^] Complementing the set
"""

import re 

email = input("what's the email address : ").strip()

if re.search(r"^.+@.+\.edu$", email):  # r means it's a raw sting just like we use for f string, it treats \ symbol as new sequence of letters not as a new line aslo it take the raw input what ever will be there right after the back slash
    print("Valid")

else:
    print("Invalid")