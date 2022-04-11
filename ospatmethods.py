# basename function
import os
out = os.path.basename("/baz/foo")
print(out)
# dirname function

ou = os.path.dirname("/baz/foo")
print(ou)
# isabs function
import os
out = os.path.isabs("baz/foo")
print(out)
# isdir function
import os
out = os.path.isdir("c:\\Users")
print(out)
import re

s = 'GeeksforGeeks: my name is dharmapu sai kiran'

match = re.search(r'dhar', s)

print('Start Index:', match.start())
print('End Index:', match.end())



