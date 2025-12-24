#!/bin/bash
# Test Python solutions for a DSA topic

TOPIC_DIR=${1:-"AdvancedGraphs"}
PROBLEM_IDS=${@:2}

echo "=========================================="
echo "Testing Python Solutions"
echo "Topic: $TOPIC_DIR"
echo "=========================================="

cd "$(dirname "$0")"

if [ -z "$PROBLEM_IDS" ]; then
    python3 test_language.py python "$TOPIC_DIR"
else
    python3 test_language.py python "$TOPIC_DIR" $PROBLEM_IDS
fi
