# Stacks Test Cases Directory

Place test case YAML files here following the format:

**Filename:** `STK-XXX-[slug].yaml`

**Example:** `STK-001-valid-parentheses.yaml`

## Required Structure

```yaml
problem_id: STK_[DESCRIPTION_CAPS]__[4_DIGITS]
samples:
  - input: |-
      [multi-line input]
    output: |-
      [multi-line output]
  - input: |-
      [second sample]
    output: |-
      [second sample output]
public:
  - input: |-
      [test case 1]
    output: |-
      [output 1]
  - input: |-
      [test case 2]
    output: |-
      [output 2]
  - input: |-
      [test case 3]
    output: |-
      [output 3]
hidden:
  - input: |-
      [hidden test 1]
    output: |-
      [output 1]
  # ... 35+ total hidden tests
```

## CRITICAL Requirements

✅ **MUST HAVE:**
- `problem_id` (top level)
- `samples`, `public`, `hidden` sections
- `input` and `output` fields only
- Use `|-` for multi-line values

❌ **NEVER INCLUDE:**
- `id` field
- `type` field
- `explanation` field
- `difficulty` field

## Test Distribution

- Samples: 2
- Public: 3
- Hidden: 35+
- Total: 40+ minimum

See `UNIVERSAL_DSA_GENERATION_PROMPT.md` for complete details.
