#!/usr/bin/env python3

import os
import re
import sys

if len(sys.argv) != 4:
    print("Usage: python script_name.py input_file output_dir predictions_file", file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]
output_dir = sys.argv[2]
predictions_file = sys.argv[3]

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

formula_pattern = re.compile(r'^fof.([^ ,]+) *,')
prediction_pattern = re.compile(r'^(.*):(.*)')

formulas = {}
with open(input_file, 'r') as fh_in:
    for line in fh_in:
        match = formula_pattern.match(line)
        if not match:
            print(f"Error: {line}", file=sys.stderr)
            sys.exit(1)

        name = match.group(1)
        formulas[name] = line

with open(predictions_file, 'r') as fh_pred:
    for line in fh_pred:
        match = prediction_pattern.match(line)
        if not match:
            print(f"Error: {line}", file=sys.stderr)
            sys.exit(1)

        name = match.group(1)
        predictions = match.group(2)

        if name not in formulas:
            print(f"Error: Formula '{name}' not found in '{input_file}'", file=sys.stderr)
            sys.exit(1)

        conjecture = formulas[name].replace('axiom', 'conjecture')

        output_file = os.path.join(output_dir, name)
        with open(output_file, 'w') as fh_out:
            fh_out.write(conjecture)

            predicted_formulas = predictions.split()
            for formula_name in predicted_formulas:
                if formula_name not in formulas:
                    print(f"Error: Formula '{formula_name}' not found in '{input_file}'", file=sys.stderr)
                    sys.exit(1)
                fh_out.write(formulas[formula_name])
