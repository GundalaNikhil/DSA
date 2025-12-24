#!/bin/bash

echo "========================================="
echo "BITWISE Test Cases - Final Verification"
echo "========================================="
echo ""

echo "1. Checking all 16 YAML files exist..."
count=0
for i in {001..016}; do
    file=$(ls BIT-$i-*.yaml 2>/dev/null | head -1)
    if [ -n "$file" ]; then
        ((count++))
        echo "  ✅ $file"
    else
        echo "  ❌ BIT-$i missing"
    fi
done
echo "  Total: $count/16 files"
echo ""

echo "2. Validating YAML syntax..."
python3 << 'PYEOF'
import yaml
import glob

files = sorted([f for f in glob.glob("BIT-*.yaml") if not f.endswith("COMPLETE.yaml")])
errors = 0
for f in files:
    try:
        with open(f) as file:
            yaml.safe_load(file)
        print(f"  ✅ {f}")
    except Exception as e:
        print(f"  ❌ {f}: {e}")
        errors += 1

print(f"\n  Validation: {len(files) - errors}/{len(files)} files passed")
PYEOF
echo ""

echo "3. Test case counts..."
python3 count_tests.py | grep -E "^✅|^⚠️"
echo ""

echo "4. Files summary..."
ls -lh BIT-*.yaml | grep -v COMPLETE | awk '{print "  " $9 " - " $5}'
echo ""

echo "========================================="
echo "VERIFICATION COMPLETE"
echo "========================================="
