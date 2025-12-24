import yaml
import glob

files = sorted(glob.glob("BIT-*.yaml"))
files = [f for f in files if not f.endswith("COMPLETE.yaml")]

print("Test Case Count Summary")
print("=" * 70)

for file in files:
    with open(file, 'r') as f:
        data = yaml.safe_load(f)
    
    samples = len(data.get('samples', []))
    public = len(data.get('public', []))
    hidden = len(data.get('hidden', []))
    total = samples + public + hidden
    
    status = "✅" if total >= 25 else "⚠️"
    print(f"{status} {file:50s} S:{samples:2d} P:{public:2d} H:{hidden:2d} Total:{total:3d}")

print("=" * 70)
