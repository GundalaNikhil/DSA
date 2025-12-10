#!/usr/bin/env python3
"""
Script to add legal notices to all DSA problem files
Adds copyright notice and disclaimer if missing
"""

import os
import re
from pathlib import Path

# Legal notices to add
COPYRIGHT_NOTICE = """
---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---
"""

DISCLAIMER = """
---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
"""

COMPANY_DISCLAIMER = """
**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.
"""

def has_copyright_notice(content):
    """Check if file already has copyright notice"""
    return "Copyright Notice" in content or "© 2025" in content

def has_disclaimer(content):
    """Check if file already has disclaimer"""
    return "Disclaimer:" in content and "original content" in content

def has_company_disclaimer(content):
    """Check if file has company disclaimer"""
    return "do not imply endorsement" in content or "for illustrative purposes" in content

def add_legal_notices(file_path):
    """Add missing legal notices to a problem file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        modified = False

        # Check if copyright notice is needed (add after tags line)
        if not has_copyright_notice(content):
            # Find the line with Tags
            tags_pattern = r'(\*\*Tags:\*\*.*\n)'
            if re.search(tags_pattern, content):
                content = re.sub(tags_pattern, r'\1' + COPYRIGHT_NOTICE, content)
                modified = True
                print(f"✅ Added copyright notice to {file_path}")

        # Add company disclaimer before "Asked by Companies" section
        if "Asked by Companies" in content and not has_company_disclaimer(content):
            content = content.replace(
                "## Asked by Companies\n\n",
                f"## Asked by Companies\n\n{COMPANY_DISCLAIMER}\n\n"
            )
            modified = True
            print(f"✅ Added company disclaimer to {file_path}")

        # Add disclaimer at the end if missing
        if not has_disclaimer(content):
            # Add before the last line or at the very end
            content = content.rstrip() + "\n" + DISCLAIMER
            modified = True
            print(f"✅ Added disclaimer to {file_path}")

        # Write back if modified
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        else:
            print(f"⏭️  Skipped {file_path} (already has all notices)")
            return False

    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False

def process_all_problems():
    """Process all problem files in dsa-problems directory"""
    base_dir = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems")

    if not base_dir.exists():
        print(f"❌ Directory not found: {base_dir}")
        return

    total_files = 0
    modified_files = 0

    # Process all .md files
    for md_file in base_dir.rglob("*.md"):
        # Skip the SAFE version and only process regular problems
        if "SAFE" in md_file.name:
            continue

        total_files += 1
        if add_legal_notices(md_file):
            modified_files += 1

    print(f"\n" + "="*60)
    print(f"📊 SUMMARY:")
    print(f"Total files processed: {total_files}")
    print(f"Files modified: {modified_files}")
    print(f"Files already compliant: {total_files - modified_files}")
    print("="*60)

if __name__ == "__main__":
    print("🚀 Starting legal notice addition process...\n")
    process_all_problems()
    print("\n✅ Process complete!")
