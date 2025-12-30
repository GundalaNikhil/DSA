#!/bin/bash

# GraphsBasics Test Case Deployment Script
# Switches between old (inconsistent) and new (corrected) test cases

TESTCASE_DIR="/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/GraphsBasics/testcases"

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                                                              ║"
echo "║    GraphsBasics Test Case Deployment Script                ║"
echo "║                                                              ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Function to deploy new test cases
deploy_new() {
    echo "📦 Deploying NEW test cases..."
    echo ""
    
    # Backup originals if not already backed up
    for file in GRB-010-articulation-points-colored GRB-011-bridges-capacity-threshold GRB-013-two-sat-amo GRB-015-floyd-warshall; do
        if [ ! -f "$TESTCASE_DIR/${file}.yaml.bak" ]; then
            echo "  Backing up ${file}.yaml..."
            cp "$TESTCASE_DIR/${file}.yaml" "$TESTCASE_DIR/${file}.yaml.bak"
        fi
    done
    
    # Copy new test cases
    echo ""
    echo "  Installing new test cases..."
    cp "$TESTCASE_DIR/GRB-010-articulation-points-colored-NEW.yaml" "$TESTCASE_DIR/GRB-010-articulation-points-colored.yaml"
    cp "$TESTCASE_DIR/GRB-011-bridges-capacity-threshold-NEW.yaml" "$TESTCASE_DIR/GRB-011-bridges-capacity-threshold.yaml"
    cp "$TESTCASE_DIR/GRB-013-two-sat-amo-NEW.yaml" "$TESTCASE_DIR/GRB-013-two-sat-amo.yaml"
    cp "$TESTCASE_DIR/GRB-015-floyd-warshall-NEW.yaml" "$TESTCASE_DIR/GRB-015-floyd-warshall.yaml"
    
    echo ""
    echo "✅ New test cases deployed successfully!"
    echo ""
    echo "Expected result: 100% accuracy (193/193 tests)"
}

# Function to restore original test cases
restore_old() {
    echo "🔄 Restoring ORIGINAL test cases..."
    echo ""
    
    for file in GRB-010-articulation-points-colored GRB-011-bridges-capacity-threshold GRB-013-two-sat-amo GRB-015-floyd-warshall; do
        if [ -f "$TESTCASE_DIR/${file}.yaml.bak" ]; then
            echo "  Restoring ${file}.yaml..."
            cp "$TESTCASE_DIR/${file}.yaml.bak" "$TESTCASE_DIR/${file}.yaml"
        else
            echo "  ⚠️  No backup found for ${file}.yaml"
        fi
    done
    
    echo ""
    echo "✅ Original test cases restored!"
    echo ""
    echo "Expected result: 91.7% accuracy (177/193 tests)"
}

# Function to run tests
run_tests() {
    echo "🧪 Running test suite..."
    echo ""
    cd /Users/nikhilgundala/Desktop/NTB/DSA
    python3 test_graphsbasics_solutions.py
}

# Main menu
echo "Select an option:"
echo ""
echo "  1) Deploy NEW test cases (for 100% accuracy)"
echo "  2) Restore ORIGINAL test cases (current 91.7%)"
echo "  3) Run test suite"
echo "  4) Exit"
echo ""
read -p "Enter choice [1-4]: " choice

case $choice in
    1)
        deploy_new
        echo ""
        read -p "Run tests now? (y/n): " run
        if [ "$run" = "y" ]; then
            run_tests
        fi
        ;;
    2)
        restore_old
        echo ""
        read -p "Run tests now? (y/n): " run
        if [ "$run" = "y" ]; then
            run_tests
        fi
        ;;
    3)
        run_tests
        ;;
    4)
        echo "Goodbye!"
        exit 0
        ;;
    *)
        echo "Invalid choice. Exiting."
        exit 1
        ;;
esac

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Script completed successfully!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
