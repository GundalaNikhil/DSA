# 🏗️ Platform SQL Architecture Guide

## Overview
**File**: `platform.sql`  
**Version**: 3.0  
**Database**: PostgreSQL 14+  
**Philosophy**: Clean, minimal, production-ready

---

## 📊 Schema Statistics

| Component | Count |
|-----------|-------|
| **Tables** | 14 |
| **Indexes** | 40+ |
| **Triggers** | 6 |
| **Functions** | 6 |
| **Views** | 3 |

---

## 🗂️ Table Structure

### **1. Core Tables**

#### `problems`
```sql
Primary Key: problem_id (TEXT) -- "ARR-001"
Unique: display_id, slug
```
**Features Added:**
- ✅ Statistics tracking (acceptance_rate, total_submissions, total_accepted)
- ✅ `subcategory` field for granular categorization
- ✅ `description` field for plain text (SEO/search)
- ✅ Feature flags (has_editorial, has_video)
- ✅ Default time/memory limits
- ✅ 4 indexes for optimal query performance

**Key Indexes:**
- `idx_problems_difficulty` - Filtered by published
- `idx_problems_category` - Filtered by published
- `idx_problems_slug` - Fast slug lookup
- `idx_problems_acceptance` - Sorting by difficulty

---

#### `editorials`
```sql
Primary Key: problem_id (FK to problems)
```
**Features Added:**
- ✅ `summary` field for preview text
- ✅ `solutions` JSONB for multi-language code
- ✅ Complexity analysis fields (time/space)
- ✅ Engagement metrics (helpful_count, view_count)
- ✅ 2 indexes

---

#### `problem_images`
```sql
Primary Key: image_id (UUID)
Unique: (problem_id, image_key)
```
**Features Added:**
- ✅ `is_placeholder` flag - Track images needing replacement
- ✅ `is_optimized` flag - CDN optimization status
- ✅ `alt_text`, `caption` for accessibility
- ✅ `display_order` for sorting
- ✅ Extended image_type values (header, visualization)
- ✅ 3 indexes including placeholder tracking

**Image Types:**
- `problem` - Problem statement images
- `editorial` - Editorial explanation images
- `example` - Example walkthrough images
- `diagram` - Algorithmic diagrams
- `header` - Problem header banners
- `visualization` - Step-by-step visualizations

---

### **2. Problem Components**

#### `problem_examples` ⭐ NEW
```sql
Primary Key: example_id (UUID)
Unique: (problem_id, example_number)
```
**Purpose:** Store sample input/output examples separately from problem HTML
- Input, output, explanation
- Display ordering
- Easier to query and manage

---

#### `function_signatures`
**Features Added:**
- ✅ 3 indexes (problem, language, active status)

---

#### `test_cases`
**Features Added:**
- ✅ `test_case_number` with UNIQUE constraint
- ✅ `test_group` field (basic, edge-cases, stress)
- ✅ 4 indexes for efficient querying

**Test Groups:**
- `basic` - Simple test cases
- `edge-cases` - Boundary conditions
- `stress` - Large inputs, performance tests

---

### **3. Quizzes**

#### `quizzes`
**Features Added:**
- ✅ Statistics (total_attempts, avg_score)
- ✅ 2 indexes

---

#### `quiz_questions`
**Features Added:**
- ✅ `display_order` field
- ✅ Statistics (total_attempts, correct_attempts)
- ✅ 2 indexes

---

#### `quiz_options`
**Features Added:**
- ✅ `display_order` field
- ✅ 1 index

---

### **4. User Interactions**

#### `user_submissions`
**Features Added:**
- ✅ `passed_test_cases` and `total_test_cases` fields
- ✅ 5 comprehensive indexes
  - user lookup
  - problem lookup
  - user+problem composite
  - verdict filtering
  - time-series (created_at DESC)

---

#### `user_problem_progress`
**Features Added:**
- ✅ Engagement tracking (bookmarked, viewed_editorial, viewed_solution)
- ✅ Best performance tracking (runtime, memory)
- ✅ `last_attempted_at` timestamp
- ✅ `created_at`, `updated_at` timestamps
- ✅ 4 indexes including bookmark filtering

---

#### `user_quiz_attempts`
**Features Added:**
- ✅ `max_score` field
- ✅ `time_taken_seconds`
- ✅ `answers` JSONB - Store detailed answer breakdown
- ✅ Changed UNIQUE constraint to allow multiple attempts
- ✅ 3 indexes

---

### **5. Tagging & Categorization** ⭐ NEW

#### `tags`
```sql
Primary Key: tag_id (SERIAL)
Unique: name, slug
```
**Purpose:** Flexible tagging system for problems
- Algorithms (Kadane, Two Pointers, etc.)
- Data Structures (Arrays, Trees, etc.)
- Techniques (Sliding Window, Prefix Sum, etc.)
- Auto-counts problems per tag
- 2 indexes

---

#### `problem_tags`
```sql
Primary Key: (problem_id, tag_id)
```
**Purpose:** Many-to-many relationship
- Display ordering
- 2 indexes

---

## ⚙️ Triggers & Functions

### **1. Auto-Update Timestamps**
**Function:** `update_updated_at_column()`  
**Applied to:** problems, editorials, function_signatures, user_problem_progress

---

### **2. Problem Statistics** ⭐
**Function:** `update_problem_stats()`  
**Trigger:** After INSERT on user_submissions  
**Updates:**
- `total_submissions` += 1
- `total_accepted` += 1 (if verdict = 'AC')
- `acceptance_rate` = (accepted / total) * 100

---

### **3. Quiz Statistics** ⭐
**Function:** `update_quiz_stats()`  
**Trigger:** After INSERT on user_quiz_attempts  
**Updates:**
- `total_attempts` += 1
- `avg_score` = AVG of all attempts

---

### **4. Question Statistics** ⭐
**Function:** `update_question_stats()`  
**Trigger:** After INSERT on user_quiz_attempts  
**Updates:** Parses answers JSONB and updates each question's:
- `total_attempts` += 1
- `correct_attempts` += 1 (if correct)

---

### **5. Tag Count** ⭐
**Function:** `update_tag_count()`  
**Trigger:** After INSERT/DELETE on problem_tags  
**Updates:** `problem_count` on tags table

---

### **6. Editorial Flag** ⭐
**Function:** `update_editorial_flag()`  
**Trigger:** After INSERT/DELETE on editorials  
**Updates:** `has_editorial` flag on problems

---

## 📈 Views

### **1. `vw_problems_list`**
**Purpose:** Optimized for problem listing pages  
**Includes:**
- All problem fields
- Tags as aggregated array
- Published problems only

**Usage:**
```sql
SELECT * FROM vw_problems_list 
WHERE difficulty = 'Easy' 
ORDER BY acceptance_rate DESC;
```

---

### **2. `vw_user_progress_summary`**
**Purpose:** User dashboard statistics  
**Includes:**
- Total problems viewed
- Attempted/solved counts
- Easy/Medium/Hard breakdown
- Last active timestamp

**Usage:**
```sql
SELECT * FROM vw_user_progress_summary 
WHERE user_id = 12345;
```

---

### **3. `vw_media_status`** ⭐
**Purpose:** Track image placeholder status  
**Includes:**
- Total images per problem
- Placeholder count
- Optimized count
- Has header/visualization flags

**Usage:**
```sql
-- Find problems with placeholder images
SELECT * FROM vw_media_status 
WHERE placeholder_count > 0 
ORDER BY placeholder_count DESC;
```

---

## 🎯 Key Features

### **1. Automatic Statistics**
- ✅ Problem acceptance rates auto-calculate
- ✅ Quiz performance metrics auto-update
- ✅ Tag counts auto-maintain
- ✅ No manual counting needed

### **2. Image Management**
- ✅ Track placeholder vs real images
- ✅ CDN optimization status
- ✅ Easy to query which problems need images

### **3. Flexible Data Storage**
- ✅ JSONB for test cases (input/output)
- ✅ JSONB for quiz answers
- ✅ JSONB for editorial solutions (multi-language)
- ✅ JSONB for function parameters

### **4. Performance Optimized**
- ✅ 40+ strategic indexes
- ✅ Partial indexes (WHERE clauses)
- ✅ Composite indexes for common queries
- ✅ Views for complex joins

### **5. Data Integrity**
- ✅ Foreign key constraints with CASCADE
- ✅ CHECK constraints on enums
- ✅ UNIQUE constraints on natural keys
- ✅ NOT NULL on critical fields

---

## 🚀 Usage Examples

### **Insert a Problem with Images**
```sql
-- 1. Insert problem
INSERT INTO problems (problem_id, display_id, slug, title, difficulty, category, problem_html)
VALUES ('ARR-001', 'ARR-001', 'snack-restock-snapshot', 'Snack Restock Snapshot', 'Easy', 'Arrays', '<div>...</div>');

-- 2. Add images (with placeholder flags)
INSERT INTO problem_images (problem_id, image_key, image_url, image_type, is_placeholder)
VALUES 
  ('ARR-001', 'header.png', 'https://cdn.example.com/placeholder.png', 'header', true),
  ('ARR-001', 'diagram.png', 'https://cdn.example.com/placeholder.png', 'diagram', true);

-- 3. Add tags
INSERT INTO tags (name, slug, category) VALUES ('Prefix Sum', 'prefix-sum', 'Technique');
INSERT INTO problem_tags (problem_id, tag_id) 
VALUES ('ARR-001', (SELECT tag_id FROM tags WHERE slug = 'prefix-sum'));

-- 4. Add editorial (automatically sets has_editorial flag)
INSERT INTO editorials (problem_id, editorial_html, is_premium)
VALUES ('ARR-001', '<div>...</div>', false);
```

### **Query Problems with Missing Images**
```sql
SELECT * FROM vw_media_status 
WHERE placeholder_count > 0 OR total_images = 0
ORDER BY display_id;
```

### **Get User Dashboard**
```sql
SELECT * FROM vw_user_progress_summary WHERE user_id = 12345;
```

### **Track Quiz Performance**
```sql
SELECT 
    q.title,
    q.total_attempts,
    q.avg_score,
    qq.question_text,
    qq.total_attempts as q_attempts,
    ROUND((qq.correct_attempts::DECIMAL / NULLIF(qq.total_attempts, 0)) * 100, 2) as success_rate
FROM quizzes q
JOIN quiz_questions qq ON q.quiz_id = qq.quiz_id
WHERE q.problem_id = 'ARR-001'
ORDER BY success_rate ASC;
```

---

## 📝 Migration from Old Schema

If you have data in the old schema (`01-schema-problems-and-quizzes.sql`):

### **Key Differences:**
1. **IDs**: Old used `VARCHAR(100)`, new uses `TEXT` (more flexible)
2. **Examples**: Old had no separate table, new has `problem_examples`
3. **Images**: Old had no placeholder tracking, new has `is_placeholder` flag
4. **Statistics**: Old had fewer triggers, new auto-calculates more
5. **Quiz Attempts**: Old limited to 1 attempt, new allows multiple

### **Migration Steps:**
```sql
-- 1. Export data from old schema
-- 2. Run platform.sql to create new schema
-- 3. Import data with field mapping
-- 4. Set placeholder flags on images that need replacement
```

---

## 🔧 Maintenance Tasks

### **Weekly:**
```sql
-- Recalculate problem statistics (if needed)
UPDATE problems p
SET 
    total_submissions = (SELECT COUNT(*) FROM user_submissions WHERE problem_id = p.problem_id),
    total_accepted = (SELECT COUNT(*) FROM user_submissions WHERE problem_id = p.problem_id AND verdict = 'AC'),
    acceptance_rate = ROUND((total_accepted::DECIMAL / NULLIF(total_submissions, 0)) * 100, 2);
```

### **Monthly:**
```sql
-- Analyze tables for query optimization
ANALYZE problems;
ANALYZE user_submissions;
ANALYZE user_problem_progress;

-- Vacuum to reclaim space
VACUUM ANALYZE;
```

### **Check Placeholder Images:**
```sql
SELECT display_id, title, placeholder_count 
FROM vw_media_status 
WHERE placeholder_count > 0;
```

---

## 🎨 Best Practices

1. **Always use transactions** for multi-table inserts
2. **Set placeholder flags** when inserting temporary images
3. **Use views** for complex queries instead of raw JOINs
4. **Let triggers handle** statistics updates (don't manually update)
5. **Use JSONB** for flexible, semi-structured data
6. **Add indexes** if you notice slow queries on new columns
7. **Regular backups** before schema changes

---

## 🔄 Future Enhancements

Potential additions without breaking changes:

- [ ] `problem_hints` table - Progressive hints system
- [ ] `user_notes` table - Personal notes on problems
- [ ] `discussions` table - Community discussions
- [ ] `problem_companies` table - Track which companies ask which problems
- [ ] `contests` table - Timed contests
- [ ] `user_achievements` table - Badges and achievements
- [ ] Full-text search indexes on problem descriptions
- [ ] Partitioning for `user_submissions` by date

---

## 📚 Related Files

- `platform.sql` - This schema file
- `01-schema-problems-and-quizzes.sql` - Original comprehensive schema
- `03-insert-all-16-problems-COMPLETE.sql` - Sample data

---

## ✅ Comparison: platform.sql vs 01-schema

| Feature | platform.sql | 01-schema |
|---------|--------------|-----------|
| **Simplicity** | ✅ Minimal | ⚠️ Complex |
| **Tables** | 14 | 21 |
| **Image Tracking** | ✅ Placeholders | ❌ No |
| **Auto Statistics** | ✅ 6 triggers | ✅ 4 triggers |
| **Examples Table** | ✅ Separate | ❌ Embedded |
| **Tags** | ✅ Simple | ✅ Complex |
| **Companies** | ❌ No | ✅ Yes |
| **Views** | 3 | 6 |
| **Learning Curve** | ✅ Easy | ⚠️ Moderate |
| **Production Ready** | ✅ Yes | ✅ Yes |

---

**Recommendation:** Use `platform.sql` for new projects. It's cleaner, easier to maintain, and has all essential features with room to grow.
