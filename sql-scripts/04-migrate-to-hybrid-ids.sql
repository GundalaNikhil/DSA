-- =====================================================
-- MIGRATE PROBLEM IDS TO HYBRID FORMAT
-- Meaningful names + collision-resistant hashes
-- Format: ARR_DESCRIPTION__HASH
-- =====================================================

-- BACKUP: Create backup of current state
-- IMPORTANT: Run this in a transaction!
-- BEGIN;

-- =====================================================
-- ARR-001: Snack Restock Snapshot
-- =====================================================
UPDATE problems SET id = 'ARR_PREFIX_AVG__4252' WHERE id = 'ARRAY-001';
UPDATE problem_examples SET problem_id = 'ARR_PREFIX_AVG__4252' WHERE problem_id = 'ARRAY-001';
UPDATE function_signatures SET problem_id = 'ARR_PREFIX_AVG__4252' WHERE problem_id = 'ARRAY-001';
UPDATE quizzes SET problem_id = 'ARR_PREFIX_AVG__4252' WHERE problem_id = 'ARRAY-001';

-- =====================================================
-- ARR-002: Bench Flip With Locked Ends
-- =====================================================
UPDATE problems SET id = 'ARR_REVERSE_MID__66B6' WHERE id = 'ARRAY-002';
UPDATE problem_examples SET problem_id = 'ARR_REVERSE_MID__66B6' WHERE problem_id = 'ARRAY-002';
UPDATE function_signatures SET problem_id = 'ARR_REVERSE_MID__66B6' WHERE problem_id = 'ARRAY-002';
UPDATE quizzes SET problem_id = 'ARR_REVERSE_MID__66B6' WHERE problem_id = 'ARRAY-002';

-- =====================================================
-- ARR-003: Shuttle Shift With Blackout
-- =====================================================
UPDATE problems SET id = 'ARR_ROTATE_LOCK__7DB3' WHERE id = 'ARRAY-003';
UPDATE problem_examples SET problem_id = 'ARR_ROTATE_LOCK__7DB3' WHERE problem_id = 'ARRAY-003';
UPDATE function_signatures SET problem_id = 'ARR_ROTATE_LOCK__7DB3' WHERE problem_id = 'ARRAY-003';
UPDATE quizzes SET problem_id = 'ARR_ROTATE_LOCK__7DB3' WHERE problem_id = 'ARRAY-003';

-- =====================================================
-- ARR-004: Lab Temperature Ranges
-- =====================================================
UPDATE problems SET id = 'ARR_DIFF_ARRAY__53AA' WHERE id = 'ARRAY-004';
UPDATE problem_examples SET problem_id = 'ARR_DIFF_ARRAY__53AA' WHERE problem_id = 'ARRAY-004';
UPDATE function_signatures SET problem_id = 'ARR_DIFF_ARRAY__53AA' WHERE problem_id = 'ARRAY-004';
UPDATE quizzes SET problem_id = 'ARR_DIFF_ARRAY__53AA' WHERE problem_id = 'ARRAY-004';

-- =====================================================
-- ARR-005: Weighted Balance Point
-- =====================================================
UPDATE problems SET id = 'ARR_WEIGHTED_BAL__7746' WHERE id = 'ARRAY-005';
UPDATE problem_examples SET problem_id = 'ARR_WEIGHTED_BAL__7746' WHERE problem_id = 'ARRAY-005';
UPDATE function_signatures SET problem_id = 'ARR_WEIGHTED_BAL__7746' WHERE problem_id = 'ARRAY-005';
UPDATE quizzes SET problem_id = 'ARR_WEIGHTED_BAL__7746' WHERE problem_id = 'ARRAY-005';

-- =====================================================
-- ARR-006: Zero Slide With Limit
-- =====================================================
UPDATE problems SET id = 'ARR_ZERO_SLIDE__7E16' WHERE id = 'ARRAY-006';
UPDATE problem_examples SET problem_id = 'ARR_ZERO_SLIDE__7E16' WHERE problem_id = 'ARRAY-006';
UPDATE function_signatures SET problem_id = 'ARR_ZERO_SLIDE__7E16' WHERE problem_id = 'ARRAY-006';
UPDATE quizzes SET problem_id = 'ARR_ZERO_SLIDE__7E16' WHERE problem_id = 'ARRAY-006';

-- =====================================================
-- ARR-007: Hostel Roster Merge With Priority
-- =====================================================
UPDATE problems SET id = 'ARR_MERGE_PRIOR__3B97' WHERE id = 'ARRAY-007';
UPDATE problem_examples SET problem_id = 'ARR_MERGE_PRIOR__3B97' WHERE problem_id = 'ARRAY-007';
UPDATE function_signatures SET problem_id = 'ARR_MERGE_PRIOR__3B97' WHERE problem_id = 'ARRAY-007';
UPDATE quizzes SET problem_id = 'ARR_MERGE_PRIOR__3B97' WHERE problem_id = 'ARRAY-007';

-- =====================================================
-- ARR-008: Partner Pair Sum Forbidden
-- =====================================================
UPDATE problems SET id = 'ARR_PAIR_FORBID__25BE' WHERE id = 'ARRAY-008';
UPDATE problem_examples SET problem_id = 'ARR_PAIR_FORBID__25BE' WHERE problem_id = 'ARRAY-008';
UPDATE function_signatures SET problem_id = 'ARR_PAIR_FORBID__25BE' WHERE problem_id = 'ARRAY-008';
UPDATE quizzes SET problem_id = 'ARR_PAIR_FORBID__25BE' WHERE problem_id = 'ARRAY-008';

-- =====================================================
-- ARR-009: Best Streak Smoothing
-- =====================================================
UPDATE problems SET id = 'ARR_KADANE_SMOOTH__4460' WHERE id = 'ARRAY-009';
UPDATE problem_examples SET problem_id = 'ARR_KADANE_SMOOTH__4460' WHERE problem_id = 'ARRAY-009';
UPDATE function_signatures SET problem_id = 'ARR_KADANE_SMOOTH__4460' WHERE problem_id = 'ARRAY-009';
UPDATE quizzes SET problem_id = 'ARR_KADANE_SMOOTH__4460' WHERE problem_id = 'ARRAY-009';

-- =====================================================
-- ARR-010: Early Discount Window
-- =====================================================
UPDATE problems SET id = 'ARR_SLIDE_WINDOW__96A0' WHERE id = 'ARRAY-010';
UPDATE problem_examples SET problem_id = 'ARR_SLIDE_WINDOW__96A0' WHERE problem_id = 'ARRAY-010';
UPDATE function_signatures SET problem_id = 'ARR_SLIDE_WINDOW__96A0' WHERE problem_id = 'ARRAY-010';
UPDATE quizzes SET problem_id = 'ARR_SLIDE_WINDOW__96A0' WHERE problem_id = 'ARRAY-010';

-- =====================================================
-- ARR-011: Leaky Roof Reinforcement
-- =====================================================
UPDATE problems SET id = 'ARR_DP_COST__1FA6' WHERE id = 'ARRAY-011';
UPDATE problem_examples SET problem_id = 'ARR_DP_COST__1FA6' WHERE problem_id = 'ARRAY-011';
UPDATE function_signatures SET problem_id = 'ARR_DP_COST__1FA6' WHERE problem_id = 'ARRAY-011';
UPDATE quizzes SET problem_id = 'ARR_DP_COST__1FA6' WHERE problem_id = 'ARRAY-011';

-- =====================================================
-- ARR-012: Longest Zero Sum Even
-- =====================================================
UPDATE problems SET id = 'ARR_ZERO_SUM_EVEN__3900' WHERE id = 'ARRAY-012';
UPDATE problem_examples SET problem_id = 'ARR_ZERO_SUM_EVEN__3900' WHERE problem_id = 'ARRAY-012';
UPDATE function_signatures SET problem_id = 'ARR_ZERO_SUM_EVEN__3900' WHERE problem_id = 'ARRAY-012';
UPDATE quizzes SET problem_id = 'ARR_ZERO_SUM_EVEN__3900' WHERE problem_id = 'ARRAY-012';

-- =====================================================
-- ARR-013: Tool Frequency Top K with Recency Decay
-- =====================================================
UPDATE problems SET id = 'ARR_FREQ_DECAY__E31B' WHERE id = 'ARRAY-013';
UPDATE problem_examples SET problem_id = 'ARR_FREQ_DECAY__E31B' WHERE problem_id = 'ARRAY-013';
UPDATE function_signatures SET problem_id = 'ARR_FREQ_DECAY__E31B' WHERE problem_id = 'ARRAY-013';
UPDATE quizzes SET problem_id = 'ARR_FREQ_DECAY__E31B' WHERE problem_id = 'ARRAY-013';

-- =====================================================
-- ARR-014: Boarding Order Fixed Ones
-- =====================================================
UPDATE problems SET id = 'ARR_PARTITION_3WAY__308B' WHERE id = 'ARRAY-014';
UPDATE problem_examples SET problem_id = 'ARR_PARTITION_3WAY__308B' WHERE problem_id = 'ARRAY-014';
UPDATE function_signatures SET problem_id = 'ARR_PARTITION_3WAY__308B' WHERE problem_id = 'ARRAY-014';
UPDATE quizzes SET problem_id = 'ARR_PARTITION_3WAY__308B' WHERE problem_id = 'ARRAY-014';

-- =====================================================
-- ARR-015: Seat Gap Removals
-- =====================================================
UPDATE problems SET id = 'ARR_MIN_REMOVE__1DC9' WHERE id = 'ARRAY-015';
UPDATE problem_examples SET problem_id = 'ARR_MIN_REMOVE__1DC9' WHERE problem_id = 'ARRAY-015';
UPDATE function_signatures SET problem_id = 'ARR_MIN_REMOVE__1DC9' WHERE problem_id = 'ARRAY-015';
UPDATE quizzes SET problem_id = 'ARR_MIN_REMOVE__1DC9' WHERE problem_id = 'ARRAY-015';

-- =====================================================
-- ARR-016: Power Window Drop
-- =====================================================
UPDATE problems SET id = 'ARR_SLIDE_MAX__14AE' WHERE id = 'ARRAY-016';
UPDATE problem_examples SET problem_id = 'ARR_SLIDE_MAX__14AE' WHERE problem_id = 'ARRAY-016';
UPDATE function_signatures SET problem_id = 'ARR_SLIDE_MAX__14AE' WHERE problem_id = 'ARRAY-016';
UPDATE quizzes SET problem_id = 'ARR_SLIDE_MAX__14AE' WHERE problem_id = 'ARRAY-016';

-- =====================================================
-- VERIFICATION QUERIES
-- =====================================================

-- Verify all updates were successful
SELECT 'Problems Updated:' AS check_type, COUNT(*) AS count 
FROM problems 
WHERE id LIKE 'ARR_%__%';

SELECT 'Examples Updated:' AS check_type, COUNT(DISTINCT problem_id) AS count 
FROM problem_examples 
WHERE problem_id LIKE 'ARR_%__%';

SELECT 'Signatures Updated:' AS check_type, COUNT(DISTINCT problem_id) AS count 
FROM function_signatures 
WHERE problem_id LIKE 'ARR_%__%';

SELECT 'Quizzes Updated:' AS check_type, COUNT(DISTINCT problem_id) AS count 
FROM quizzes 
WHERE problem_id LIKE 'ARR_%__%';

-- List all new IDs
SELECT id, title, difficulty 
FROM problems 
WHERE id LIKE 'ARR_%__%'
ORDER BY display_id;

-- =====================================================
-- COMMIT OR ROLLBACK
-- =====================================================
-- COMMIT;   -- Uncomment to commit changes
-- ROLLBACK; -- Uncomment to rollback if something went wrong
