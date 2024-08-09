# I'll read the newly uploaded Terraform file to extract mandatory variables.
# The process is the same as before: mandatory variables are those that do not have a default value.

file_path = '/mnt/data/variables (1).tf'

mandatory_vars = []

with open(file_path, 'r') as file:
    lines = file.readlines()

current_var = None
for line in lines:
    line = line.strip()
    if line.startswith('variable'):
        current_var = line.split('"')[1]
    if line.startswith('default'):
        current_var = None
    if current_var and (line == "}" or line == ''):
        mandatory_vars.append(current_var)
        current_var = None

mandatory_vars
