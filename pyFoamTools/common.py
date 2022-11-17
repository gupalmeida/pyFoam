import os
import yaml

# loads default existing case dictionaries
__file_dir__ = os.path.split(__file__)[0]
with open(os.path.join(__file_dir__,'default_case_dictionaries.yaml'),'r') as file:
    case_dictionaries = yaml.safe_load(file)

print(case_dictionaries)