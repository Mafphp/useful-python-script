import os
import re

# Directory path where your TypeScript files are located
directory_path = "./src/"

# Regular expression pattern to match decorators and their content
pattern_decorators = r'(@ApiProperty(?:Optional)?\s*\(\s*\{[\s\S]*?\}\s*\))'

# Function to wrap decorators in a comment block
def wrap_in_comment(match):
    decorator = match.group(0)
    comment_block = f'/* {decorator} */'
    return comment_block

# Iterate through files in the directory
for root, dirs, files in os.walk(directory_path):
    for file in files:
        if file.endswith("request.dto.ts"):
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file:
                content = file.read()

            # Wrap decorators in a comment block
            content = re.sub(pattern_decorators, wrap_in_comment, content)

            with open(file_path, 'w') as file:
                file.write(content)
