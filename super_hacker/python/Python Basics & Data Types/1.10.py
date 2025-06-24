#!usr/bin/python3
import re
#"aeiouAEIOU@0"
r = "*"
password = "P@ssw0rd"
result = re.sub(r'[aeiouAEIOU@0]', r, password)
print(result)
