import ast
import re
import sys

def enforce_snake_case(name):
    # Check if the name is already in snake_case
    if name.islower() and "_" in name:
        return name

    # Replace spaces with underscores and enforce snake_case
    name = re.sub(r'\s+', '_', name)
    # Remove non-alphanumeric characters except underscores
    name = re.sub(r'[^a-zA-Z0-9_]', '', name)
    return ('v_' + name)
 

def extract_variables_and_types(file_path):
    with open(file_path, 'r') as file:
        source_code = file.read()

    tree = ast.parse(source_code)

    variables_and_types = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    variable_name = target.id
                    variable_type = None

                    if node.value:
                        variable_type = node.value.__class__.__name__

                    variables_and_types.append((variable_name, variable_type))
        elif isinstance(node, ast.FunctionDef):
            for arg in node.args.args:
                argument_name = arg.arg
                argument_type = None

                # You can add logic here to infer the argument type if needed.

                variables_and_types.append((argument_name, argument_type))

    return variables_and_types

if __name__ == "__main__":
    file_path = "app.py"  # Replace with the path to your Python script
    variables_and_types = extract_variables_and_types(file_path)

    for variable_name, variable_type in variables_and_types:
        snake_case_name = enforce_snake_case(variable_name)
        if snake_case_name != variable_name:
            print(f"Original Name: {variable_name}, Snake Case: {snake_case_name}", file=sys.stdout, flush=True)
        else:
            print(f"Original Name: {variable_name}, Snake Case Compliant", file=sys.stdout, flush=True)
