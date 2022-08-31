"""Resource converter for iOS"""

from dataclasses import dataclass
import os

@dataclass
class Config():
    """
    App-level config
    """
    ios_project_dir = '/Users/yutaro/work/iOSResourceConverter'

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
