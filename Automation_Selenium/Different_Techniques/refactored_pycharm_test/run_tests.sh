#!/bin/bash

echo "Loading config from YAML..."

MARKERS=$(python3 -c "
import yaml
with open('config.yaml') as f:
    config = yaml.safe_load(f)
print(' and '.join([f'marker == \"{m}\"' for m in config['pytest']['markers']]))
")

VERBOSITY=$(python3 -c "
import yaml
with open('config.yaml') as f:
    config = yaml.safe_load(f)
print(config['pytest'].get('verbosity', ''))
")

REPORT="--html=report.html --self-contained-html"

CMD="pytest -m \"$MARKERS\" $VERBOSITY $REPORT"

echo "Executing: $CMD"
eval $CMD
