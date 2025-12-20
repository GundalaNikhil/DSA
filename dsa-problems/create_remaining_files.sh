#!/bin/bash

# Script to create all empty files for Greedy, Stacks, and StringsClassic

BASE_DIR="/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems"

echo "=========================================="
echo "Creating Empty Problem Files"
echo "=========================================="
echo ""

# Counter
TOTAL_CREATED=0

# Function to create files for a topic
create_topic_files() {
    local topic=$1
    local prefix=$2
    shift 2
    local problems=("$@")
    
    echo "Processing $topic..."
    
    cd "$BASE_DIR/$topic" || exit
    
    local count=0
    
    for problem_def in "${problems[@]}"; do
        local num=$(echo "$problem_def" | cut -d':' -f1)
        local slug=$(echo "$problem_def" | cut -d':' -f2)
        local filename="${prefix}-${num}-${slug}"
        
        # Create quiz file
        if [ ! -f "quizzes/${filename}.yaml" ]; then
            touch "quizzes/${filename}.yaml"
            ((count++))
        fi
        
        # Create image directory and README
        mkdir -p "images/${prefix}-${num}"
        if [ ! -f "images/${prefix}-${num}/README.md" ]; then
            touch "images/${prefix}-${num}/README.md"
            ((count++))
        fi
    done
    
    echo "  ✅ Created $count files for $topic"
    TOTAL_CREATED=$((TOTAL_CREATED + count))
}

# Greedy problems
GREEDY_PROBLEMS=(
    "001:campus-shuttle-driver-swaps"
    "002:lab-kit-distribution"
    "003:festival-stall-placement"
    "004:library-power-backup"
    "005:shuttle-overtime-minimizer"
    "006:robotics-component-bundling-loss-quality"
    "007:campus-wifi-expansion"
    "008:exam-proctor-allocation"
    "009:shuttle-refuel-with-refund"
    "010:library-merge-queues"
    "011:campus-event-ticket-caps"
    "012:workshop-task-cooldown-priority"
    "013:auditorium-seat-refunds"
    "014:festival-bandwidth-split"
    "015:robotics-median-after-batches-stale"
    "016:shuttle-schedule-delay-minimizer"
)

# Stacks problems
STACKS_PROBLEMS=(
    "001:notebook-undo-simulator"
    "002:lab-mixed-bracket-repair"
    "003:conveyor-weighted-deduplication"
    "004:rooftop-sunset-count"
    "005:workshop-next-taller-width"
    "006:assembly-previous-greater-parity"
    "007:trading-desk-threshold-jump"
    "008:canteen-token-climb-span"
    "009:lab-sliding-min-stack"
    "010:stadium-max-tracker"
    "011:circuit-postfix-variables"
    "012:campus-expression-optimizer"
    "013:auditorium-histogram-one-booster"
    "014:shuttle-validation-time-windows"
    "015:bike-repair-plates"
    "016:assembly-line-span-reset"
)

# StringsClassic problems
STRINGSCLASSIC_PROBLEMS=(
    "001:kmp-prefix-function"
    "002:pattern-search-kmp"
    "003:z-function"
    "004:pattern-search-z"
    "005:suffix-array-doubling"
    "006:lcp-array-kasai"
    "007:longest-repeated-substring-sa"
    "008:distinct-substrings-sa"
    "009:minimal-rotation-sa"
    "010:lcp-two-suffixes"
    "011:lcs-two-strings-sa"
    "012:diff-substrings-two-strings"
    "013:palindromic-tree-eertree"
    "014:longest-palindrome-one-wildcard"
    "015:aho-corasick-cooldown-scoring"
    "016:suffix-automaton-queries"
)

# Create files for each topic
create_topic_files "Greedy" "GRD" "${GREEDY_PROBLEMS[@]}"
create_topic_files "Stacks" "STK" "${STACKS_PROBLEMS[@]}"
create_topic_files "StringsClassic" "STC" "${STRINGSCLASSIC_PROBLEMS[@]}"

echo ""
echo "=========================================="
echo "✅ TOTAL: Created $TOTAL_CREATED files"
echo "=========================================="
echo ""
echo "Summary:"
echo "  • Greedy: 16 problems"
echo "  • Stacks: 16 problems"
echo "  • StringsClassic: 16 problems"
echo "  • TOTAL: 48 problems"
echo ""
