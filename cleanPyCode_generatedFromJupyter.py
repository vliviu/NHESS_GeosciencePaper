import re

with open("nonlinearRegression.py", "r") as f:
    lines = f.readlines()

cleaned_lines = []
skip_next_empty_line = False

for line in lines:
    if line.startswith("# In["):
        skip_next_empty_line = True
    elif skip_next_empty_line and line == '\n':
        skip_next_empty_line = False
    else:
        cleaned_lines.append(line)

content = ''.join(cleaned_lines)
content = re.sub(r'^\s*# In\[\d*\]:.*\n?', '', content, flags=re.MULTILINE)
content = re.sub(r'^\s*\n', '', content, flags=re.MULTILINE)

with open("cleaned_nonlinearRegression.py", "w") as f:
    f.write(content)