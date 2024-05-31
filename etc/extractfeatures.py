#!/usr/bin/env python3

import re
import sys

pattern = re.compile(r'^fof.([^ ,]+) *, *axiom, (.*)')
variable_pattern = re.compile(r'[a-z0-9A-Z_]+')

for line in sys.stdin:
    match = pattern.match(line)
    if not match:
        print(f"Error: {line}", file=sys.stderr)
        sys.exit(1)

    name = match.group(1)
    formula = match.group(2)
    variables = set()

    for variable in variable_pattern.finditer(formula):
#        variables.add(variable.group(0))
        variables.add(f'"{variable.group(0)}"')

        
    print(f"{name}: {', '.join(variables)}")
