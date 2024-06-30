import os, sys

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
examples_path = os.path.join(root_path, 'examples')
examples = ['hello-world', 'sample-project']
sys.path.append(root_path)
for example in examples:
    sys.path.append(os.path.join(examples_path, example))
