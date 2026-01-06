-- =====================================================
-- USER SUBMISSIONS TABLE MIGRATION
-- Complete Judge0 submission tracking with security
-- =====================================================

-- Drop existing table if exists (CAUTION: Use with care in production)
DROP TABLE IF EXISTS user_submissions CASCADE;

-- Create submissions table with all required fields
CREATE TABLE user_submissions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    -- User & Problem References
    user_id BIGINT NOT NULL,                         -- References auth.users or your users table
    problem_id VARCHAR(100) NOT NULL,                -- References problems(id)
    
    -- Submission Details - ONLY USER CODE
    language_name VARCHAR(50) NOT NULL,
    language_id INTEGER,                             -- Judge0 language ID
    source_code TEXT NOT NULL,                       -- ONLY user-written code, NEVER DB test cases
    
    -- Execution Results
    status VARCHAR(50) NOT NULL,                     -- 'Accepted', 'Wrong Answer', 'TLE', 'MLE', 'CE', 'RE', 'Running', 'Queued'
    status_code INTEGER,                             -- Numeric status code
    
    -- Test Case Results
    passed_test_cases INTEGER DEFAULT 0,
    total_test_cases INTEGER NOT NULL,
    failed_test_case_number INTEGER,
    
    -- Performance Metrics
    runtime_ms INTEGER,
    memory_mb DECIMAL(10,2),
    
    -- Error Details (sanitized)
    error_message TEXT,
    compiler_output TEXT,
    stderr TEXT,
    stdout TEXT,
    
    -- Scoring
    score DECIMAL(5,2) DEFAULT 0,
    max_score DECIMAL(5,2),
    
    -- Submission Metadata
    is_accepted BOOLEAN DEFAULT false,
    is_best_submission BOOLEAN DEFAULT false,        -- User's best submission
    submission_number INTEGER,                       -- User's nth attempt on this problem
    
    -- Judge0 Integration (SENSITIVE - internal use only, never exposed to frontend)
    judge0_token VARCHAR(150),
    judge0_batch_id VARCHAR(150),
    
    -- Code Analysis
    code_length INTEGER,
    lines_of_code INTEGER,
    
    -- Tracking
    ip_address INET,
    user_agent TEXT,
    submission_source VARCHAR(50) DEFAULT 'web',     -- 'web', 'mobile', 'api', 'ide'
    
    -- Timestamps
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP,
    submission_date DATE DEFAULT CURRENT_DATE
);

-- =====================================================
-- INDEXES FOR PERFORMANCE
-- =====================================================

-- Core lookup indexes
CREATE INDEX idx_submissions_user ON user_submissions(user_id);
CREATE INDEX idx_submissions_problem ON user_submissions(problem_id);
CREATE INDEX idx_submissions_user_problem ON user_submissions(user_id, problem_id);

-- Query optimization indexes
CREATE INDEX idx_submissions_status ON user_submissions(status);
CREATE INDEX idx_submissions_accepted ON user_submissions(is_accepted) WHERE is_accepted = true;
CREATE INDEX idx_submissions_created_at ON user_submissions(created_at DESC);
CREATE INDEX idx_submissions_date ON user_submissions(submission_date DESC);

-- Judge0 callback index
CREATE INDEX idx_submissions_judge0 ON user_submissions(judge0_token) WHERE judge0_token IS NOT NULL;

-- Best submission lookup
CREATE INDEX idx_submissions_best ON user_submissions(user_id, problem_id, is_best_submission) WHERE is_best_submission = true;

-- =====================================================
-- ROW LEVEL SECURITY (RLS) - CRITICAL FOR SECURITY
-- =====================================================

-- Enable RLS
ALTER TABLE user_submissions ENABLE ROW LEVEL SECURITY;

-- Policy: Users can only view their own submissions
CREATE POLICY "Users can view own submissions"
ON user_submissions FOR SELECT
USING (auth.uid()::bigint = user_id);

-- Policy: Users can insert their own submissions
CREATE POLICY "Users can create own submissions"
ON user_submissions FOR INSERT
WITH CHECK (auth.uid()::bigint = user_id);

-- Policy: Service role (backend) can do everything
CREATE POLICY "Service role full access"
ON user_submissions FOR ALL
USING (auth.role() = 'service_role');

-- =====================================================
-- TRIGGERS
-- =====================================================

-- Trigger to auto-update code analysis fields
CREATE OR REPLACE FUNCTION update_submission_metadata()
RETURNS TRIGGER AS $$
BEGIN
    -- Set submission date if not provided
    IF NEW.submission_date IS NULL THEN
        NEW.submission_date = CURRENT_DATE;
    END IF;
    
    -- Calculate code length
    IF NEW.code_length IS NULL AND NEW.source_code IS NOT NULL THEN
        NEW.code_length = LENGTH(NEW.source_code);
    END IF;
    
    -- Calculate lines of code
    IF NEW.lines_of_code IS NULL AND NEW.source_code IS NOT NULL THEN
        NEW.lines_of_code = array_length(string_to_array(NEW.source_code, E'\n'), 1);
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_submission_metadata
BEFORE INSERT ON user_submissions
FOR EACH ROW
EXECUTE FUNCTION update_submission_metadata();

-- =====================================================
-- COMMENTS FOR DOCUMENTATION
-- =====================================================

COMMENT ON TABLE user_submissions IS 'All user code submissions with execution results - ALL Judge0 submissions are recorded';
COMMENT ON COLUMN user_submissions.source_code IS 'SECURITY: Only user-written code, never DB test cases or internal code';
COMMENT ON COLUMN user_submissions.judge0_token IS 'INTERNAL ONLY: Never exposed to frontend, used for callback processing';
COMMENT ON COLUMN user_submissions.is_best_submission IS 'Flags the best submission for this user-problem pair based on performance';

-- =====================================================
-- GRANTS (adjust based on your auth setup)
-- =====================================================

-- Grant access to authenticated users (read their own)
GRANT SELECT ON user_submissions TO authenticated;

-- Grant insert to authenticated users
GRANT INSERT ON user_submissions TO authenticated;

-- Grant all to service role (backend API)
GRANT ALL ON user_submissions TO service_role;

-- =====================================================
-- VERIFICATION QUERIES
-- =====================================================

-- Verify table structure
SELECT 
    column_name, 
    data_type, 
    is_nullable,
    column_default
FROM information_schema.columns
WHERE table_name = 'user_submissions'
ORDER BY ordinal_position;

-- Verify indexes
SELECT 
    indexname,
    indexdef
FROM pg_indexes
WHERE tablename = 'user_submissions';

-- Verify RLS policies
SELECT 
    schemaname,
    tablename,
    policyname,
    permissive,
    roles,
    cmd,
    qual,
    with_check
FROM pg_policies
WHERE tablename = 'user_submissions';

-- Test query (will return 0 initially)
SELECT COUNT(*) as total_submissions FROM user_submissions;
