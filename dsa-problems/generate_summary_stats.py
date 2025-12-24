#!/usr/bin/env python3
"""Generate summary statistics from audit"""

topics_data = {
    # Topic: (total_files, critical_files, high_files, medium_files, perfect)
    'AdvancedGraphs': (16, 4, 0, 12, 0),
    'Arrays': (16, 3, 0, 13, 0),
    'Bitwise': (17, 4, 0, 13, 0),
    'Concurrency': (16, 0, 16, 0, 0),
    'DP': (16, 0, 16, 0, 0),
    'GameTheory': (16, 0, 16, 0, 0),
    'Geometry': (16, 0, 16, 0, 0),
    'Graphs': (18, 18, 0, 0, 0),
    'GraphsBasics': (12, 12, 0, 0, 0),
    'Greedy': (16, 16, 0, 0, 0),
    'Hashing': (16, 0, 1, 0, 15),
    'Heaps': (16, 3, 0, 13, 0),
    'LinkedLists': (16, 5, 0, 11, 0),
    'MathAdvanced': (14, 0, 0, 0, 14),
    'NumberTheory': (16, 0, 16, 0, 0),
    'Probabilistic': (16, 0, 0, 0, 16),
    'ProbabilisticDS': (16, 16, 0, 0, 0),
    'Queues': (16, 16, 0, 0, 0),
    'Recursion': (16, 0, 0, 0, 16),
    'SegmentTree': (16, 16, 0, 0, 0),
    'Sorting': (16, 0, 0, 0, 16),
    'Stacks': (16, 1, 0, 0, 15),
    'Strings': (16, 4, 0, 12, 0),
    'StringsClassic': (16, 0, 0, 0, 16),
    'Trees': (18, 0, 0, 0, 18),
    'TreesDP': (16, 0, 16, 0, 0),
    'Tries': (16, 2, 0, 14, 0),
}

total_files = sum(t[0] for t in topics_data.values())
total_critical = sum(t[1] for t in topics_data.values())
total_high = sum(t[2] for t in topics_data.values())
total_medium = sum(t[3] for t in topics_data.values())
total_perfect = sum(t[4] for t in topics_data.values())

print("=" * 80)
print("COMPREHENSIVE TEST CASES AUDIT - SUMMARY STATISTICS")
print("=" * 80)
print()
print(f"Total Topics: {len(topics_data)}")
print(f"Total Test Files: {total_files}")
print()
print("BREAKDOWN BY SEVERITY:")
print(f"  🔴 Critical Issues:  {total_critical:3d} files ({total_critical/total_files*100:5.1f}%)")
print(f"  🟡 High Priority:    {total_high:3d} files ({total_high/total_files*100:5.1f}%)")
print(f"  ⚠️  Medium Priority:  {total_medium:3d} files ({total_medium/total_files*100:5.1f}%)")
print(f"  ✅ Perfect:          {total_perfect:3d} files ({total_perfect/total_files*100:5.1f}%)")
print()
print(f"Files Needing Fixes: {total_critical + total_high + total_medium} ({(total_critical + total_high + total_medium)/total_files*100:.1f}%)")
print()
print("=" * 80)
print("TOPICS BY STATUS")
print("=" * 80)
print()

# Perfect topics
perfect_topics = [k for k, v in topics_data.items() if v[4] == v[0]]
print(f"✅ PERFECT TOPICS ({len(perfect_topics)}):")
for topic in perfect_topics:
    print(f"   • {topic} ({topics_data[topic][0]} files)")
print()

# Critical topics
critical_topics = [(k, v) for k, v in topics_data.items() if v[1] > 0]
critical_topics.sort(key=lambda x: x[1][1], reverse=True)
print(f"🔴 CRITICAL TOPICS ({len(critical_topics)}):")
for topic, data in critical_topics:
    print(f"   • {topic}: {data[1]}/{data[0]} files need critical fixes")
print()

# High priority topics
high_topics = [(k, v) for k, v in topics_data.items() if v[2] > 0]
high_topics.sort(key=lambda x: x[1][2], reverse=True)
print(f"🟡 HIGH PRIORITY TOPICS ({len(high_topics)}):")
for topic, data in high_topics:
    print(f"   • {topic}: {data[2]}/{data[0]} files need high priority fixes")
print()

print("=" * 80)
print("TOP 10 TOPICS BY FILES NEEDING FIXES")
print("=" * 80)

topics_by_issues = [(k, v[1] + v[2] + v[3]) for k, v in topics_data.items()]
topics_by_issues.sort(key=lambda x: x[1], reverse=True)

for i, (topic, count) in enumerate(topics_by_issues[:10], 1):
    data = topics_data[topic]
    print(f"{i:2d}. {topic:20s} {count:3d}/{data[0]:3d} files need fixes ({count/data[0]*100:5.1f}%)")

print()
print("=" * 80)
