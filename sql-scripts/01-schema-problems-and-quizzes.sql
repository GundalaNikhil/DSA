-- =====================================================
-- DSA PROBLEMS & QUIZZES - COMPLETE SCHEMA
-- =====================================================
-- Version: 2.0
-- Date: December 14, 2025
-- Purpose: Complete schema for DSA problems with function signatures and quizzes
-- =====================================================

SET search_path TO public;

-- =====================================================
-- 1. PROBLEMS TABLE (Enhanced)
-- =====================================================
DROP TABLE IF EXISTS problems CASCADE;

CREATE TABLE problems (
    -- Primary identifiers
    id VARCHAR(100) PRIMARY KEY,  -- e.g., 'ARRAY-001'
    display_id VARCHAR(20) NOT NULL,  -- e.g., 'A001'
    slug VARCHAR(150) UNIQUE NOT NULL,  -- e.g., 'snack-restock-snapshot'
    
    -- Basic info
    title VARCHAR(300) NOT NULL,
    description TEXT NOT NULL,
    difficulty VARCHAR(20) NOT NULL CHECK (difficulty IN ('Easy', 'Medium', 'Hard')),
    
    -- Categorization
    category VARCHAR(100),  -- 'Arrays', 'Dynamic Programming', etc.
    subcategory VARCHAR(100),  -- 'Prefix Sum', 'String DP', etc.
    
    -- Problem details
    hint TEXT,
    constraints JSONB,  -- Structured constraints
    
    -- Premium & Status
    is_premium BOOLEAN DEFAULT false,
    is_active BOOLEAN DEFAULT true,
    is_featured BOOLEAN DEFAULT false,
    
    -- Statistics
    acceptance_rate DECIMAL(5,2) DEFAULT 0,
    total_submissions INTEGER DEFAULT 0,
    total_accepted INTEGER DEFAULT 0,
    total_views INTEGER DEFAULT 0,
    difficulty_score DECIMAL(5,2),  -- Calculated difficulty
    
    -- SEO & UI
    meta_title VARCHAR(200),
    meta_description TEXT,
    og_image_url VARCHAR(500),
    
    -- Versioning
    version INTEGER DEFAULT 1,
    
    -- Timestamps
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    published_at TIMESTAMP,
    
    -- Soft delete
    is_deleted BOOLEAN DEFAULT false,
    deleted_at TIMESTAMP
);

-- Indexes
CREATE INDEX idx_problems_difficulty ON problems(difficulty) WHERE is_active = true AND is_deleted = false;
CREATE INDEX idx_problems_category ON problems(category) WHERE is_active = true;
CREATE INDEX idx_problems_slug ON problems(slug) WHERE is_deleted = false;
CREATE INDEX idx_problems_active ON problems(is_active, is_deleted);
CREATE INDEX idx_problems_premium ON problems(is_premium) WHERE is_active = true;
CREATE INDEX idx_problems_created_at ON problems(created_at DESC);


-- =====================================================
-- 2. PROBLEM EXAMPLES TABLE
-- =====================================================
DROP TABLE IF EXISTS problem_examples CASCADE;

CREATE TABLE problem_examples (
    id SERIAL PRIMARY KEY,
    problem_id VARCHAR(100) REFERENCES problems(id) ON DELETE CASCADE,
    
    example_number INTEGER NOT NULL,
    input TEXT NOT NULL,
    output TEXT NOT NULL,
    explanation TEXT,
    
    display_order INTEGER DEFAULT 0,
    is_hidden BOOLEAN DEFAULT false,  -- For premium examples
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT unique_problem_example UNIQUE (problem_id, example_number)
);

CREATE INDEX idx_examples_problem ON problem_examples(problem_id);


-- =====================================================
-- 3. FUNCTION SIGNATURES TABLE (NEW)
-- =====================================================
DROP TABLE IF EXISTS function_signatures CASCADE;

CREATE TABLE function_signatures (
    id SERIAL PRIMARY KEY,
    problem_id VARCHAR(100) REFERENCES problems(id) ON DELETE CASCADE,
    
    -- Language info
    language_name VARCHAR(50) NOT NULL,  -- 'Java', 'Python', 'C++', 'JavaScript'
    language_id INTEGER,  -- Judge0 language ID (71=Python, 62=Java, etc.)
    
    -- Function details
    function_name VARCHAR(150) NOT NULL,
    return_type VARCHAR(100),
    parameters JSONB,  -- [{"name": "arr", "type": "int[]", "description": "input array"}]
    
    -- Code templates
    solution_template TEXT NOT NULL,  -- Code with function signature
    starter_code TEXT,  -- Initial code user sees (may be same as solution_template)
    
    -- Custom input handling code
    custom_input_code TEXT NOT NULL,  -- Main method / runner code
    
    -- Test runner (for Judge0)
    test_runner_code TEXT,  -- Code to wrap solution and run tests
    
    -- Metadata
    display_order INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT true,
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT unique_problem_language UNIQUE (problem_id, language_name)
);

CREATE INDEX idx_signatures_problem ON function_signatures(problem_id);
CREATE INDEX idx_signatures_language ON function_signatures(language_name);


-- =====================================================
-- 4. QUIZZES TABLE (NEW)
-- =====================================================
DROP TABLE IF EXISTS quizzes CASCADE;

CREATE TABLE quizzes (
    id SERIAL PRIMARY KEY,
    problem_id VARCHAR(100) REFERENCES problems(id) ON DELETE CASCADE,
    
    -- Quiz content
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    
    -- Answer
    correct_answer CHAR(1) NOT NULL CHECK (correct_answer IN ('A', 'B', 'C', 'D')),
    explanation TEXT NOT NULL,
    
    -- Metadata
    difficulty VARCHAR(20) CHECK (difficulty IN ('Easy', 'Medium', 'Hard')),
    quiz_type VARCHAR(50) DEFAULT 'conceptual',  -- 'conceptual', 'complexity', 'implementation'
    
    -- Display
    display_order INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT true,
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT unique_problem_quiz UNIQUE (problem_id, display_order)
);

CREATE INDEX idx_quizzes_problem ON quizzes(problem_id);
CREATE INDEX idx_quizzes_active ON quizzes(is_active);


-- =====================================================
-- 5. TAGS TABLE
-- =====================================================
DROP TABLE IF EXISTS tags CASCADE;

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    slug VARCHAR(100) UNIQUE NOT NULL,
    
    category VARCHAR(100),  -- 'Algorithm', 'Data Structure', 'Technique'
    description TEXT,
    
    -- UI
    icon VARCHAR(100),
    color VARCHAR(50),
    
    -- SEO
    meta_description TEXT,
    
    -- Stats
    problem_count INTEGER DEFAULT 0,
    
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_tags_slug ON tags(slug);
CREATE INDEX idx_tags_category ON tags(category);


-- =====================================================
-- 6. PROBLEM_TAGS (Many-to-Many)
-- =====================================================
DROP TABLE IF EXISTS problem_tags CASCADE;

CREATE TABLE problem_tags (
    problem_id VARCHAR(100) REFERENCES problems(id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES tags(id) ON DELETE CASCADE,
    
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    PRIMARY KEY (problem_id, tag_id)
);

CREATE INDEX idx_problem_tags_problem ON problem_tags(problem_id);
CREATE INDEX idx_problem_tags_tag ON problem_tags(tag_id);


-- =====================================================
-- 7. TEST CASES TABLE
-- =====================================================
DROP TABLE IF EXISTS test_cases CASCADE;

CREATE TABLE test_cases (
    id SERIAL PRIMARY KEY,
    problem_id VARCHAR(100) REFERENCES problems(id) ON DELETE CASCADE,
    
    -- Test data
    input JSONB NOT NULL,  -- {"arr": [1,2,3], "k": 2}
    expected_output JSONB NOT NULL,
    
    -- Metadata
    test_case_number INTEGER NOT NULL,
    is_hidden BOOLEAN DEFAULT false,
    is_sample BOOLEAN DEFAULT false,
    
    test_group VARCHAR(100),  -- 'basic', 'edge-cases', 'large-inputs', 'stress'
    difficulty VARCHAR(20),
    
    -- Execution limits
    time_limit_ms INTEGER DEFAULT 2000,
    memory_limit_mb INTEGER DEFAULT 256,
    
    -- Description
    description TEXT,
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_testcases_problem ON test_cases(problem_id);
CREATE INDEX idx_testcases_hidden ON test_cases(is_hidden);


-- =====================================================
-- 8. USER SUBMISSIONS TABLE
-- =====================================================
DROP TABLE IF EXISTS user_submissions CASCADE;

CREATE TABLE user_submissions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    user_id BIGINT NOT NULL,  -- References users(id)
    problem_id VARCHAR(100) REFERENCES problems(id) ON DELETE CASCADE,
    
    -- Submission details
    language_name VARCHAR(50) NOT NULL,
    language_id INTEGER,
    source_code TEXT NOT NULL,
    
    -- Results
    status VARCHAR(50) NOT NULL,  -- 'Accepted', 'Wrong Answer', 'TLE', 'MLE', 'CE', 'RE'
    passed_test_cases INTEGER DEFAULT 0,
    total_test_cases INTEGER NOT NULL,
    
    -- Performance
    runtime_ms INTEGER,
    memory_mb DECIMAL(10,2),
    
    -- Error details
    error_message TEXT,
    failed_test_case_number INTEGER,
    
    -- Metadata
    is_accepted BOOLEAN DEFAULT false,
    submission_number INTEGER,  -- User's nth attempt
    
    -- Judge0 integration
    judge0_token VARCHAR(150),
    
    -- IP tracking
    ip_address INET,
    user_agent TEXT,
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_submissions_user ON user_submissions(user_id);
CREATE INDEX idx_submissions_problem ON user_submissions(problem_id);
CREATE INDEX idx_submissions_status ON user_submissions(status);
CREATE INDEX idx_submissions_created_at ON user_submissions(created_at DESC);


-- =====================================================
-- 9. USER PROBLEM PROGRESS TABLE
-- =====================================================
DROP TABLE IF EXISTS user_problem_progress CASCADE;

CREATE TABLE user_problem_progress (
    user_id BIGINT NOT NULL,
    problem_id VARCHAR(100) REFERENCES problems(id) ON DELETE CASCADE,
    
    -- Status
    status VARCHAR(30) NOT NULL DEFAULT 'not_started',  -- 'not_started', 'attempted', 'solved'
    
    -- Attempts
    total_attempts INTEGER DEFAULT 0,
    first_attempt_at TIMESTAMP,
    solved_at TIMESTAMP,
    last_attempted_at TIMESTAMP,
    
    -- Best submission
    best_runtime_ms INTEGER,
    best_memory_mb DECIMAL(10,2),
    best_submission_id UUID,
    
    -- Engagement
    viewed_solution BOOLEAN DEFAULT false,
    viewed_hints BOOLEAN DEFAULT false,
    bookmarked BOOLEAN DEFAULT false,
    notes TEXT,
    
    -- Timestamps
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    PRIMARY KEY (user_id, problem_id)
);

CREATE INDEX idx_progress_user ON user_problem_progress(user_id);
CREATE INDEX idx_progress_status ON user_problem_progress(status);
CREATE INDEX idx_progress_solved ON user_problem_progress(solved_at DESC);


-- =====================================================
-- 10. USER QUIZ ATTEMPTS TABLE (NEW)
-- =====================================================
DROP TABLE IF EXISTS user_quiz_attempts CASCADE;

CREATE TABLE user_quiz_attempts (
    id SERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    quiz_id INTEGER REFERENCES quizzes(id) ON DELETE CASCADE,
    problem_id VARCHAR(100) REFERENCES problems(id) ON DELETE CASCADE,
    
    -- Answer
    selected_answer CHAR(1) NOT NULL CHECK (selected_answer IN ('A', 'B', 'C', 'D')),
    is_correct BOOLEAN NOT NULL,
    
    -- Timing
    time_taken_seconds INTEGER,
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT unique_user_quiz UNIQUE (user_id, quiz_id)
);

CREATE INDEX idx_quiz_attempts_user ON user_quiz_attempts(user_id);
CREATE INDEX idx_quiz_attempts_quiz ON user_quiz_attempts(quiz_id);
CREATE INDEX idx_quiz_attempts_problem ON user_quiz_attempts(problem_id);


-- =====================================================
-- FUNCTIONS & TRIGGERS
-- =====================================================

-- Auto-update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_problems_updated_at
    BEFORE UPDATE ON problems
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_signatures_updated_at
    BEFORE UPDATE ON function_signatures
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_quizzes_updated_at
    BEFORE UPDATE ON quizzes
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_progress_updated_at
    BEFORE UPDATE ON user_problem_progress
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();


-- Update tag problem count
CREATE OR REPLACE FUNCTION update_tag_problem_count()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        UPDATE tags SET problem_count = problem_count + 1 WHERE id = NEW.tag_id;
    ELSIF TG_OP = 'DELETE' THEN
        UPDATE tags SET problem_count = problem_count - 1 WHERE id = OLD.tag_id;
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_tag_count
AFTER INSERT OR DELETE ON problem_tags
FOR EACH ROW
EXECUTE FUNCTION update_tag_problem_count();


-- =====================================================
-- VIEWS
-- =====================================================

-- Problem list view with all details
CREATE OR REPLACE VIEW problem_list_view AS
SELECT 
    p.id,
    p.display_id,
    p.title,
    p.slug,
    p.difficulty,
    p.category,
    p.subcategory,
    p.is_premium,
    p.acceptance_rate,
    p.total_submissions,
    p.total_views,
    ARRAY_AGG(DISTINCT t.name) FILTER (WHERE t.name IS NOT NULL) as tags,
    COUNT(DISTINCT pe.id) as example_count,
    COUNT(DISTINCT fs.id) as language_count,
    COUNT(DISTINCT tc.id) as test_case_count,
    COUNT(DISTINCT q.id) as quiz_count,
    p.created_at,
    p.updated_at
FROM problems p
LEFT JOIN problem_tags pt ON p.id = pt.problem_id
LEFT JOIN tags t ON pt.tag_id = t.id
LEFT JOIN problem_examples pe ON p.id = pe.problem_id
LEFT JOIN function_signatures fs ON p.id = fs.problem_id AND fs.is_active = true
LEFT JOIN test_cases tc ON p.id = tc.problem_id
LEFT JOIN quizzes q ON p.id = q.problem_id AND q.is_active = true
WHERE p.is_active = true AND p.is_deleted = false
GROUP BY p.id;


-- =====================================================
-- COMMENTS
-- =====================================================

COMMENT ON TABLE problems IS 'Core DSA problems with enhanced metadata';
COMMENT ON TABLE function_signatures IS 'Language-specific function signatures and starter code';
COMMENT ON TABLE quizzes IS 'Multiple choice quizzes for each problem';
COMMENT ON TABLE user_quiz_attempts IS 'User attempts at quizzes';
COMMENT ON COLUMN problems.display_id IS 'Human-readable ID like A001, A002';
COMMENT ON COLUMN problems.is_featured IS 'Featured problems shown on homepage';
COMMENT ON COLUMN function_signatures.custom_input_code IS 'Code for handling custom user input (main method)';
COMMENT ON COLUMN quizzes.quiz_type IS 'Type of quiz: conceptual, complexity, implementation';

-- =====================================================
-- END OF SCHEMA
-- =====================================================
