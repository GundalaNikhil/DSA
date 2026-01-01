import glob

files = glob.glob("dsa-problems/AdvancedGraphs/solutions/javascript/*.js")
old_pat = "data.push(...line.trim().split(/\\s+/));"
new_pat = "const parts = line.trim().split(/\\s+/); for (const p of parts) if (p) data.push(p);"

count = 0
for fpath in files:
    with open(fpath, 'r') as f:
        content = f.read()
    
    broken_pat = "rl.on(\"line\", (line) => const parts = line.trim().split(/\\s+/); for (const p of parts) if (p) data.push(p));"
    correct_pat = "rl.on(\"line\", (line) => { const parts = line.trim().split(/\\s+/); for (const p of parts) if (p) data.push(p); });"

    if broken_pat in content:
        content = content.replace(broken_pat, correct_pat)
        with open(fpath, 'w') as f:
            f.write(content)
        count += 1
        print(f"Fixed {fpath}")

print(f"Fixed {count} files.")
