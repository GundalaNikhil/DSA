#!/bin/bash
# Test C++ solutions for a DSA topic

TOPIC_DIR=${1:-"AdvancedGraphs"}
PROBLEM_IDS=${@:2}

echo "=========================================="
echo "Testing C++ Solutions"
echo "Topic: $TOPIC_DIR"
echo "=========================================="

cd "$(dirname "$0")"

if [ -z "$PROBLEM_IDS" ]; then
    python3 test_language.py cpp "$TOPIC_DIR"
else
    python3 test_language.py cpp "$TOPIC_DIR" $PROBLEM_IDS
fi
