"""Resource converter for iOS"""

from dataclasses import dataclass
import os
import re

@dataclass
class Config():
    """
    App-level config
    """
    ios_project_dir = '/Users/yutaro/work/iOSResourceConverter'

def convert_underscore_to_period(input_str: str) -> str:
    """
    Convert strings separated by underscore into ones by period
    """
    result = re.findall('\"\\w*\"', input_str)
    key = result[0].replace('_', '.')
    value = result[1]
    return f"{key} = {value};"

# Get list of all swift files and resource files
os.chdir(Config().ios_project_dir)
string_resource_files = []
swift_files = []
for root, dirs, files in os.walk("./"):
    for file in files:
        if file.endswith(".strings"):
            string_resource_files.append(os.path.join(root, file))
        elif file.endswith(".swift"):
            swift_files.append(os.path.join(root, file))

# Read resource files
for file in string_resource_files:
    # Prepare file to be used
    TMP_FILE_NAME = "tmp.strings"
    new_file = open(TMP_FILE_NAME, "a", encoding="utf-8")

    content = open(file, "r", encoding="utf-8")
    lines = content.readlines()
    # Perform necessary modifications
    for line in lines:
        period_strs = convert_underscore_to_period(line)
        new_file.write(period_strs)
        new_file.write("\n")
    content.close()
    new_file.close()
    # Remove old file
    os.remove(file)
    os.replace(TMP_FILE_NAME, file)
