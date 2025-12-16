-- =====================================================
-- DSA PLATFORM - COMPLETE DATABASE SCHEMA
-- =====================================================
-- Version: 3.0 - Complete Architecture
-- Date: December 15, 2025
-- Purpose: Comprehensive schema for DSA learning platform
-- Includes: Problems, Editorials, Images, Quizzes, Tests, Submissions
-- =====================================================
-- Author: System Architect
-- Database: PostgreSQL 14+
-- =====================================================

SET search_path TO public;

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm"; -- For text search

-- =====================================================
-- SECTION 1: CORE ENTITIES
-- =====================================================

-- =====================================================
-- 1.1 PROBLEMS TABLE (Enhanced)
-- =====================================================
DROP TABLE IF EXISTS problems CASCADE;

CREATE TABLE problems (
    -- Primary identifiers
    id VARCHAR(100) PRIMARY KEY,                    -- Internal: 'ARRAY-001', 'DP-042'
    display_id VARCHAR(20) NOT NULL UNIQUE,         -- Public: 'ARR-001', 'DP-042'
    slug VARCHAR(150) UNIQUE NOT NULL,              -- URL-friendly: 'snack-restock-snapshot'
    
    -- Core content
    title VARCHAR(300) NOT NULL,
    description TEXT NOT NULL,                       -- Brief problem statement
    problem_statement TEXT,                          -- Full detailed statement
    
    -- Difficulty & categorization
    difficulty VARCHAR(20) NOT NULL CHECK (difficulty IN ('Easy', 'Medium', 'Hard')),
    difficulty_score DECIMAL(5,2) DEFAULT 0,        -- 0-100 calculated difficulty
    category VARCHAR(100) NOT NULL,                  -- 'Arrays', 'Dynamic Programming', etc.
    subcategory VARCHAR(100),                        -- 'Prefix Sum', 'String DP', etc.
    
    -- Problem details
    hint TEXT,
    constraints JSONB,                               -- {"n_range": {"min": 1, "max": 100000}}
    time_complexity VARCHAR(50),                     -- 'O(n)', 'O(n log n)'
    space_complexity VARCHAR(50),                    -- 'O(1)', 'O(n)'
    
    -- Real-world context
    real_world_scenario TEXT,                        -- Story/context for the problem
    scenario_title VARCHAR(200),                     -- e.g., 'Campus Snack Shop Manager'
    
    -- Premium & Status
    is_premium BOOLEAN DEFAULT false,
    subscription_tier VARCHAR(50),                   -- 'basic', 'pro', 'enterprise', null
    is_active BOOLEAN DEFAULT true,
    is_featured BOOLEAN DEFAULT false,
    is_published BOOLEAN DEFAULT false,
    
    -- Statistics (auto-updated)
    acceptance_rate DECIMAL(5,2) DEFAULT 0,
    total_submissions INTEGER DEFAULT 0,
    total_accepted INTEGER DEFAULT 0,
    total_views INTEGER DEFAULT 0,
    total_attempts INTEGER DEFAULT 0,
    average_runtime_ms DECIMAL(10,2),
    
    -- Engagement metrics
    upvotes INTEGER DEFAULT 0,
    downvotes INTEGER DEFAULT 0,
    bookmark_count INTEGER DEFAULT 0,
    discussion_count INTEGER DEFAULT 0,
    
    -- SEO & Metadata
    meta_title VARCHAR(200),
    meta_description TEXT,
    meta_keywords TEXT[],
    og_image_url VARCHAR(500),
    
    -- Editorial reference
    has_editorial BOOLEAN DEFAULT false,
    editorial_premium BOOLEAN DEFAULT false,
    
    -- Content flags
    has_video_solution BOOLEAN DEFAULT false,
    has_interactive_viz BOOLEAN DEFAULT false,
    has_company_tags BOOLEAN DEFAULT false,
    
    -- Versioning & audit
    version INTEGER DEFAULT 1,
    created_by VARCHAR(100),
    updated_by VARCHAR(100),
    
    -- Timestamps
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    published_at TIMESTAMP,
    
    -- Soft delete
    is_deleted BOOLEAN DEFAULT false,
    deleted_at TIMESTAMP,
    deleted_by VARCHAR(100)
);

-- Indexes for problems
CREATE INDEX idx_problems_difficulty ON problems(difficulty) WHERE is_active = true AND is_deleted = false;
CREATE INDEX idx_problems_category ON problems(category) WHERE is_active = true;
CREATE INDEX idx_problems_subcategory ON problems(subcategory) WHERE is_active = true;
CREATE INDEX idx_problems_slug ON problems(slug) WHERE is_deleted = false;
CREATE INDEX idx_problems_active_published ON problems(is_active, is_published, is_deleted);
CREATE INDEX idx_problems_premium ON problems(is_premium) WHERE is_active = true;
CREATE INDEX idx_problems_featured ON problems(is_featured) WHERE is_active = true AND is_featured = true;
CREATE INDEX idx_problems_created_at ON problems(created_at DESC);
CREATE INDEX idx_problems_acceptance_rate ON problems(acceptance_rate DESC);
CREATE INDEX idx_problems_display_id ON problems(display_id);

-- Full-text search on problems
CREATE INDEX idx_problems_title_search ON problems USING gin(to_tsvector('english', title));
CREATE INDEX idx_problems_description_search ON problems USING gin(to_tsvector('english', description));

COMMENT ON TABLE problems IS 'Core DSA problems with enhanced metadata and statistics';
COMMENT ON COLUMN problems.display_id IS 'Human-readable public ID (ARR-001, DP-042)';
COMMENT ON COLUMN problems.difficulty_score IS 'Calculated difficulty score 0-100 based on acceptance rate and user feedback';


-- =====================================================
-- 1.2 EDITORIALS TABLE
-- =====================================================
DROP TABLE IF EXISTS editorials CASCADE;

CREATE TABLE editorials (
    id SERIAL PRIMARY KEY,
    problem_id VARCHAR(100) UNIQUE REFERENCES problems(id) ON DELETE CASCADE,
    
    -- Content sections
    summary TEXT,                                    -- Brief editorial summary
    approach_overview TEXT,                          -- High-level approach
    intuition TEXT,                                  -- Intuitive explanation
    algorithm_description TEXT,                      -- Detailed algorithm steps
    
    -- Implementation sections
    implementation_notes TEXT,
    edge_cases TEXT,
    optimization_tips TEXT,
    
    -- Analysis
    time_complexity_analysis TEXT,
    space_complexity_analysis TEXT,
    
    -- Code solutions (stored as JSON for multiple languages)
    solutions JSONB,                                 -- {"java": "code...", "python": "code..."}
    
    -- Alternative approaches
    alternative_approaches JSONB,                    -- [{"title": "Approach 2", "description": "...", "code": "..."}]
    
    -- Related content
    similar_problems TEXT[],                         -- Array of problem IDs
    prerequisites TEXT[],                            -- Array of concept names
    follow_up_questions TEXT[],                      -- Array of follow-up problems
    
    -- Learning resources
    video_url VARCHAR(500),
    video_duration_seconds INTEGER,
    external_resources JSONB,                        -- [{"title": "Article", "url": "..."}]
    
    -- Visualization
    has_step_by_step_viz BOOLEAN DEFAULT false,
    visualization_url VARCHAR(500),
    
    -- Premium
    is_premium BOOLEAN DEFAULT false,
    preview_available BOOLEAN DEFAULT true,          -- Show first 2 sections for free
    
    -- Statistics
    helpful_count INTEGER DEFAULT 0,
    not_helpful_count INTEGER DEFAULT 0,
    view_count INTEGER DEFAULT 0,
    
    -- Metadata
    author_id VARCHAR(100),
    reviewer_id VARCHAR(100),
    last_reviewed_at TIMESTAMP,
    
    -- Versioning
    version INTEGER DEFAULT 1,
    changelog JSONB,                                 -- [{"version": 1, "changes": "...", "date": "..."}]
    
    -- Status
    is_published BOOLEAN DEFAULT false,
    is_active BOOLEAN DEFAULT true,
    
    -- Timestamps
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    published_at TIMESTAMP
);

CREATE INDEX idx_editorials_problem ON editorials(problem_id);
CREATE INDEX idx_editorials_premium ON editorials(is_premium);
CREATE INDEX idx_editorials_published ON editorials(is_published) WHERE is_active = true;
CREATE INDEX idx_editorials_helpful ON editorials(helpful_count DESC);

COMMENT ON TABLE editorials IS 'Detailed editorial solutions and explanations for problems';
COMMENT ON COLUMN editorials.solutions IS 'JSON object with language-specific complete solutions';
COMMENT ON COLUMN editorials.preview_available IS 'Whether non-premium users can see a preview';


-- =====================================================
-- 1.3 MEDIA ASSETS TABLE (Images, Videos, Diagrams)
-- =====================================================
DROP TABLE IF EXISTS media_assets CASCADE;

CREATE TABLE media_assets (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    problem_id VARCHAR(100) REFERENCES problems(id) ON DELETE CASCADE,
    editorial_id INTEGER REFERENCES editorials(id) ON DELETE CASCADE,
    
    -- Asset details
    asset_type VARCHAR(50) NOT NULL,                 -- 'image', 'video', 'diagram', 'animation'
    asset_category VARCHAR(100) NOT NULL,            -- 'header', 'problem-illustration', 'algorithm-steps', etc.
    
    -- File information
    file_name VARCHAR(300) NOT NULL,
    file_path VARCHAR(500) NOT NULL,                 -- Relative path: 'images/ARR-001/header.png'
    file_url VARCHAR(500),                           -- Full URL if using CDN
    file_size_kb INTEGER,
    
    -- Image-specific
    width INTEGER,
    height INTEGER,
    format VARCHAR(20),                              -- 'png', 'jpg', 'svg', 'gif', 'mp4'
    alt_text TEXT,
    caption TEXT,
    
    -- Usage context
    display_section VARCHAR(100),                    -- 'problem', 'editorial', 'solution', 'example'
    display_order INTEGER DEFAULT 0,
    
    -- Status
    is_placeholder BOOLEAN DEFAULT false,            -- True if placeholder, needs replacement
    is_optimized BOOLEAN DEFAULT false,              -- Image optimization status
    is_active BOOLEAN DEFAULT true,
    
    -- CDN & Performance
    cdn_url VARCHAR(500),
    cloudinary_id VARCHAR(200),
    s3_key VARCHAR(300),
    
    -- Metadata
    uploaded_by VARCHAR(100),
    processing_status VARCHAR(50) DEFAULT 'pending', -- 'pending', 'processing', 'completed', 'failed'
    
    -- Prompt for AI generation (if applicable)
    generation_prompt TEXT,
    
    -- Timestamps
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    uploaded_at TIMESTAMP
);

CREATE INDEX idx_media_problem ON media_assets(problem_id);
CREATE INDEX idx_media_editorial ON media_assets(editorial_id);
CREATE INDEX idx_media_type ON media_assets(asset_type);
CREATE INDEX idx_media_category ON media_assets(asset_category);
CREATE INDEX idx_media_placeholder ON media_assets(is_placeholder) WHERE is_placeholder = true;
CREATE INDEX idx_media_active ON media_assets(is_active);

COMMENT ON TABLE media_assets IS 'All media assets (images, videos, diagrams) for problems and editorials';
COMMENT ON COLUMN media_assets.asset_category IS 'Specific category: header, problem-illustration, algorithm-steps, visualization, example-1, etc.';
COMMENT ON COLUMN media_assets.generation_prompt IS 'AI prompt used to generate the image (for documentation)';


-- =====================================================
-- SECTION 2: PROBLEM COMPONENTS
-- =====================================================

-- =====================================================
-- 2.1 PROBLEM EXAMPLES TABLE
-- =====================================================
DROP TABLE IF EXISTS problem_examples CASCADE;

CREATE TABLE problem_examples (
    id SERIAL PRIMARY KEY,
    problem_id VARCHAR(100) REFERENCES problems(id) ON DELETE CASCADE,
    
    -- Example data
    example_number INTEGER NOT NULL,
    input TEXT NOT NULL,
    output TEXT NOT NULL,
    explanation TEXT,
    
    -- Visual representation
    diagram_url VARCHAR(500),
    has_visualization BOOLEAN DEFAULT false,
    
    -- Metadata
    display_order INTEGER DEFAULT 0,
    is_hidden BOOLEAN DEFAULT false,                 -- For premium examples
    is_sample BOOLEAN DEFAULT true,                  -- Shown in problem statement
    
    -- Timestamps
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT unique_problem_example UNIQUE (problem_id, example_number)
);

CREATE INDEX idx_examples_problem ON problem_examples(problem_id);
CREATE INDEX idx_examples_sample ON problem_examples(is_sample) WHERE is_sample = true;

COMMENT ON TABLE problem_examples IS 'Sample input/output examples for problems';


-- =====================================================
-- 2.2 FUNCTION SIGNATURES TABLE
-- =====================================================
DROP TABLE IF EXISTS function_signatures CASCADE;

CREATE TABLE function_signatures (
    id SERIAL PRIMARY KEY,
    problem_id VARCHAR(100) REFERENCES problems(id) ON DELETE CASCADE,
    
    -- Language information
    language_name VARCHAR(50) NOT NULL,              -- 'Java', 'Python', 'C++', 'JavaScript'
    language_id INTEGER,                             -- Judge0 language ID (71=Python, 62=Java)
    language_version VARCHAR(50),                    -- 'Python 3.10', 'Java 17'
    
    -- Function details
    function_name VARCHAR(150) NOT NULL,
    return_type VARCHAR(100),
    parameters JSONB,                                -- [{"name": "arr", "type": "int[]", "description": "..."}]
    
    -- Code templates
    solution_template TEXT NOT NULL,                 -- Full template with function signature
    starter_code TEXT,                               -- Initial code shown to user
    
    -- Input/Output handling
    custom_input_code TEXT NOT NULL,                 -- Main method / runner code for custom input
    output_formatter TEXT,                           -- Code to format output
    
    -- Testing infrastructure
    test_runner_code TEXT,                           -- Code to wrap solution and run all tests
    test_harness_code TEXT,                          -- Advanced test harness
    
    -- Imports and setup
    default_imports TEXT,                            -- Default imports for the language
    boilerplate_code TEXT,                           -- Additional boilerplate
    
    -- Validation
    has_syntax_check BOOLEAN DEFAULT true,
    has_type_hints BOOLEAN DEFAULT false,
    
    -- Metadata
    display_order INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT true,
    is_popular BOOLEAN DEFAULT false,                -- Mark popular languages
    
    -- Timestamps
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT unique_problem_language UNIQUE (problem_id, language_name)
);

CREATE INDEX idx_signatures_problem ON function_signatures(problem_id);
CREATE INDEX idx_signatures_language ON function_signatures(language_name);
CREATE INDEX idx_signatures_active ON function_signatures(is_active);
CREATE INDEX idx_signatures_popular ON function_signatures(is_popular) WHERE is_popular = true;

COMMENT ON TABLE function_signatures IS 'Language-specific function signatures and starter code templates';
COMMENT ON COLUMN function_signatures.test_runner_code IS 'Code that runs all test cases and validates output';


-- =====================================================
-- 2.3 TEST CASES TABLE
-- =====================================================
DROP TABLE IF EXISTS test_cases CASCADE;

CREATE TABLE test_cases (
    id SERIAL PRIMARY KEY,
    problem_id VARCHAR(100) REFERENCES problems(id) ON DELETE CASCADE,
    
    -- Test data (JSON format for flexibility)
    input JSONB NOT NULL,                            -- {"arr": [1,2,3], "k": 2}
    expected_output JSONB NOT NULL,                  -- {"result": [3, 5]}
    
    -- Test metadata
    test_case_number INTEGER NOT NULL,
    test_group VARCHAR(100),                         -- 'basic', 'edge-cases', 'large-inputs', 'stress'
    test_name VARCHAR(200),                          -- Descriptive name
    description TEXT,
    
    -- Visibility & difficulty
    is_hidden BOOLEAN DEFAULT false,                 -- Hidden from user
    is_sample BOOLEAN DEFAULT false,                 -- Shown in problem statement
    difficulty VARCHAR(20),                          -- 'Easy', 'Medium', 'Hard'
    
    -- Execution limits
    time_limit_ms INTEGER DEFAULT 2000,
    memory_limit_mb INTEGER DEFAULT 256,
    
    -- Scoring
    points DECIMAL(5,2) DEFAULT 1.0,                 -- Points for passing this test
    weight DECIMAL(5,2) DEFAULT 1.0,                 -- Weight in scoring
    
    -- Status
    is_active BOOLEAN DEFAULT true,
    is_validated BOOLEAN DEFAULT false,              -- Has been validated to work correctly
    
    -- Timestamps
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT unique_problem_test_number UNIQUE (problem_id, test_case_number)
);

CREATE INDEX idx_testcases_problem ON test_cases(problem_id);
CREATE INDEX idx_testcases_hidden ON test_cases(is_hidden);
CREATE INDEX idx_testcases_sample ON test_cases(is_sample);
CREATE INDEX idx_testcases_group ON test_cases(test_group);
CREATE INDEX idx_testcases_active ON test_cases(is_active);

COMMENT ON TABLE test_cases IS 'Test cases for validating problem solutions';
COMMENT ON COLUMN test_cases.test_group IS 'Logical grouping: basic, edge-cases, large-inputs, stress, corner-cases';


-- =====================================================
-- SECTION 3: QUIZZES & ASSESSMENTS
-- =====================================================

-- =====================================================
-- 3.1 QUIZZES TABLE
-- =====================================================
DROP TABLE IF EXISTS quizzes CASCADE;

CREATE TABLE quizzes (
    id SERIAL PRIMARY KEY,
    problem_id VARCHAR(100) REFERENCES problems(id) ON DELETE CASCADE,
    editorial_id INTEGER REFERENCES editorials(id) ON DELETE SET NULL,
    
    -- Quiz content
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    
    -- Answer & explanation
    correct_answer CHAR(1) NOT NULL CHECK (correct_answer IN ('A', 'B', 'C', 'D')),
    explanation TEXT NOT NULL,
    explanation_detail TEXT,                         -- Extended explanation
    
    -- Quiz classification
    difficulty VARCHAR(20) CHECK (difficulty IN ('Easy', 'Medium', 'Hard')),
    quiz_type VARCHAR(50) DEFAULT 'conceptual',      -- 'conceptual', 'complexity', 'implementation', 'edge-case', 'optimization'
    quiz_category VARCHAR(100),                      -- 'understanding', 'analysis', 'application'
    
    -- Learning objectives
    learning_objective TEXT,
    concept_tested VARCHAR(200),                     -- 'Time Complexity', 'Space Optimization', etc.
    
    -- Code-based quiz
    has_code_snippet BOOLEAN DEFAULT false,
    code_snippet TEXT,
    code_language VARCHAR(50),
    
    -- Display & ordering
    display_order INTEGER DEFAULT 0,
    display_section VARCHAR(50) DEFAULT 'post-problem', -- 'pre-problem', 'post-problem', 'editorial'
    
    -- Status & engagement
    is_active BOOLEAN DEFAULT true,
    is_premium BOOLEAN DEFAULT false,
    
    -- Statistics
    total_attempts INTEGER DEFAULT 0,
    correct_attempts INTEGER DEFAULT 0,
    success_rate DECIMAL(5,2) DEFAULT 0,
    
    -- Timestamps
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT unique_problem_quiz_order UNIQUE (problem_id, display_order)
);

CREATE INDEX idx_quizzes_problem ON quizzes(problem_id);
CREATE INDEX idx_quizzes_editorial ON quizzes(editorial_id);
CREATE INDEX idx_quizzes_type ON quizzes(quiz_type);
CREATE INDEX idx_quizzes_active ON quizzes(is_active);
CREATE INDEX idx_quizzes_section ON quizzes(display_section);

COMMENT ON TABLE quizzes IS 'Multiple choice quizzes for reinforcing problem concepts';
COMMENT ON COLUMN quizzes.quiz_type IS 'Type: conceptual, complexity, implementation, edge-case, optimization';
COMMENT ON COLUMN quizzes.display_section IS 'When to show: pre-problem, post-problem, editorial';


-- =====================================================
-- SECTION 4: TAGGING & CATEGORIZATION
-- =====================================================

-- =====================================================
-- 4.1 TAGS TABLE
-- =====================================================
DROP TABLE IF EXISTS tags CASCADE;

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    slug VARCHAR(100) UNIQUE NOT NULL,
    
    -- Categorization
    category VARCHAR(100),                           -- 'Algorithm', 'Data Structure', 'Technique', 'Concept'
    parent_tag_id INTEGER REFERENCES tags(id),       -- For hierarchical tags
    
    -- Description & help
    description TEXT,
    learning_resources TEXT,
    
    -- UI & Display
    icon VARCHAR(100),                               -- Emoji or icon class
    color VARCHAR(50),                               -- Hex color code
    display_order INTEGER DEFAULT 0,
    
    -- SEO
    meta_title VARCHAR(200),
    meta_description TEXT,
    
    -- Statistics
    problem_count INTEGER DEFAULT 0,
    view_count INTEGER DEFAULT 0,
    
    -- Status
    is_active BOOLEAN DEFAULT true,
    is_featured BOOLEAN DEFAULT false,
    
    -- Timestamps
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_tags_slug ON tags(slug);
CREATE INDEX idx_tags_category ON tags(category);
CREATE INDEX idx_tags_active ON tags(is_active);
CREATE INDEX idx_tags_featured ON tags(is_featured) WHERE is_featured = true;
CREATE INDEX idx_tags_parent ON tags(parent_tag_id);

COMMENT ON TABLE tags IS 'Tags for categorizing problems (algorithms, data structures, techniques)';


-- =====================================================
-- 4.2 PROBLEM_TAGS (Many-to-Many)
-- =====================================================
DROP TABLE IF EXISTS problem_tags CASCADE;

CREATE TABLE problem_tags (
    problem_id VARCHAR(100) REFERENCES problems(id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES tags(id) ON DELETE CASCADE,
    
    -- Relevance
    relevance_score DECIMAL(3,2) DEFAULT 1.0,        -- 0.0 to 1.0, how relevant is this tag
    is_primary BOOLEAN DEFAULT false,                -- Primary tag for the problem
    
    -- Display
    display_order INTEGER DEFAULT 0,
    
    -- Metadata
    added_by VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    PRIMARY KEY (problem_id, tag_id)
);

CREATE INDEX idx_problem_tags_problem ON problem_tags(problem_id);
CREATE INDEX idx_problem_tags_tag ON problem_tags(tag_id);
CREATE INDEX idx_problem_tags_primary ON problem_tags(is_primary) WHERE is_primary = true;

COMMENT ON TABLE problem_tags IS 'Many-to-many relationship between problems and tags';


-- =====================================================
-- 4.3 COMPANIES TABLE (For interview prep)
-- =====================================================
DROP TABLE IF EXISTS companies CASCADE;

CREATE TABLE companies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) UNIQUE NOT NULL,
    slug VARCHAR(200) UNIQUE NOT NULL,
    
    -- Company info
    logo_url VARCHAR(500),
    website_url VARCHAR(500),
    description TEXT,
    
    -- Categorization
    industry VARCHAR(100),
    company_size VARCHAR(50),                        -- 'startup', 'mid-size', 'large', 'enterprise'
    
    -- Display
    display_order INTEGER DEFAULT 0,
    color VARCHAR(50),
    
    -- Statistics
    problem_count INTEGER DEFAULT 0,
    
    -- Status
    is_active BOOLEAN DEFAULT true,
    is_featured BOOLEAN DEFAULT false,
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_companies_slug ON companies(slug);
CREATE INDEX idx_companies_active ON companies(is_active);
CREATE INDEX idx_companies_featured ON companies(is_featured) WHERE is_featured = true;

COMMENT ON TABLE companies IS 'Companies for tagging interview problems';


-- =====================================================
-- 4.4 PROBLEM_COMPANIES (Many-to-Many)
-- =====================================================
DROP TABLE IF EXISTS problem_companies CASCADE;

CREATE TABLE problem_companies (
    problem_id VARCHAR(100) REFERENCES problems(id) ON DELETE CASCADE,
    company_id INTEGER REFERENCES companies(id) ON DELETE CASCADE,
    
    -- Frequency & recency
    frequency VARCHAR(50),                           -- 'very-high', 'high', 'medium', 'low'
    last_asked_year INTEGER,
    times_asked INTEGER DEFAULT 1,
    
    -- Round information
    interview_round VARCHAR(100),                    -- 'phone-screen', 'online-assessment', 'onsite', 'final'
    
    -- Metadata
    added_by VARCHAR(100),
    verified BOOLEAN DEFAULT false,
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    PRIMARY KEY (problem_id, company_id)
);

CREATE INDEX idx_problem_companies_problem ON problem_companies(problem_id);
CREATE INDEX idx_problem_companies_company ON problem_companies(company_id);
CREATE INDEX idx_problem_companies_frequency ON problem_companies(frequency);
CREATE INDEX idx_problem_companies_year ON problem_companies(last_asked_year DESC);

COMMENT ON TABLE problem_companies IS 'Track which companies ask which problems in interviews';


-- =====================================================
-- SECTION 5: USER INTERACTIONS
-- =====================================================

-- =====================================================
-- 5.1 USER SUBMISSIONS TABLE
-- =====================================================
DROP TABLE IF EXISTS user_submissions CASCADE;

CREATE TABLE user_submissions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    
    -- User & problem
    user_id BIGINT NOT NULL,                         -- References users(id) from auth system
    problem_id VARCHAR(100) REFERENCES problems(id) ON DELETE CASCADE,
    
    -- Submission details
    language_name VARCHAR(50) NOT NULL,
    language_id INTEGER,                             -- Judge0 language ID
    source_code TEXT NOT NULL,
    
    -- Execution results
    status VARCHAR(50) NOT NULL,                     -- 'Accepted', 'Wrong Answer', 'TLE', 'MLE', 'CE', 'RE', 'Running'
    status_code INTEGER,                             -- Numeric status code
    
    -- Test case results
    passed_test_cases INTEGER DEFAULT 0,
    total_test_cases INTEGER NOT NULL,
    failed_test_case_number INTEGER,
    
    -- Performance metrics
    runtime_ms INTEGER,
    memory_mb DECIMAL(10,2),
    
    -- Error details
    error_message TEXT,
    compiler_output TEXT,
    stderr TEXT,
    stdout TEXT,
    
    -- Scoring
    score DECIMAL(5,2) DEFAULT 0,
    max_score DECIMAL(5,2),
    
    -- Submission metadata
    is_accepted BOOLEAN DEFAULT false,
    is_best_submission BOOLEAN DEFAULT false,        -- User's best submission
    submission_number INTEGER,                       -- User's nth attempt on this problem
    
    -- Judge0 integration
    judge0_token VARCHAR(150),
    judge0_batch_id VARCHAR(150),
    
    -- Code analysis
    code_length INTEGER,
    lines_of_code INTEGER,
    
    -- Tracking
    ip_address INET,
    user_agent TEXT,
    submission_source VARCHAR(50) DEFAULT 'web',     -- 'web', 'mobile', 'api', 'ide'
    
    -- Timestamps
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP,
    
    -- Indexing for partitioning (optional)
    submission_date DATE DEFAULT CURRENT_DATE
);

CREATE INDEX idx_submissions_user ON user_submissions(user_id);
CREATE INDEX idx_submissions_problem ON user_submissions(problem_id);
CREATE INDEX idx_submissions_user_problem ON user_submissions(user_id, problem_id);
CREATE INDEX idx_submissions_status ON user_submissions(status);
CREATE INDEX idx_submissions_accepted ON user_submissions(is_accepted) WHERE is_accepted = true;
CREATE INDEX idx_submissions_created_at ON user_submissions(created_at DESC);
CREATE INDEX idx_submissions_date ON user_submissions(submission_date DESC);
CREATE INDEX idx_submissions_judge0 ON user_submissions(judge0_token) WHERE judge0_token IS NOT NULL;

COMMENT ON TABLE user_submissions IS 'All user code submissions with execution results';
COMMENT ON COLUMN user_submissions.is_best_submission IS 'Flags the best submission for this user-problem pair';


-- =====================================================
-- 5.2 USER PROBLEM PROGRESS TABLE
-- =====================================================
DROP TABLE IF EXISTS user_problem_progress CASCADE;

CREATE TABLE user_problem_progress (
    user_id BIGINT NOT NULL,
    problem_id VARCHAR(100) REFERENCES problems(id) ON DELETE CASCADE,
    
    -- Status tracking
    status VARCHAR(30) NOT NULL DEFAULT 'not_started', -- 'not_started', 'attempted', 'solved'
    
    -- Attempt statistics
    total_attempts INTEGER DEFAULT 0,
    successful_attempts INTEGER DEFAULT 0,
    
    -- Important timestamps
    first_attempt_at TIMESTAMP,
    solved_at TIMESTAMP,
    last_attempted_at TIMESTAMP,
    last_viewed_at TIMESTAMP,
    
    -- Best performance
    best_runtime_ms INTEGER,
    best_memory_mb DECIMAL(10,2),
    best_submission_id UUID,
    
    -- Languages used
    languages_attempted TEXT[],
    
    -- Engagement tracking
    viewed_solution BOOLEAN DEFAULT false,
    viewed_hints BOOLEAN DEFAULT false,
    viewed_editorial BOOLEAN DEFAULT false,
    watched_video BOOLEAN DEFAULT false,
    
    -- Bookmarking & notes
    bookmarked BOOLEAN DEFAULT false,
    bookmarked_at TIMESTAMP,
    notes TEXT,
    
    -- Time tracking
    total_time_spent_seconds INTEGER DEFAULT 0,      -- Total time on problem
    
    -- Difficulty feedback
    user_difficulty_rating INTEGER,                  -- 1-5 scale
    
    -- Timestamps
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    PRIMARY KEY (user_id, problem_id)
);

CREATE INDEX idx_progress_user ON user_problem_progress(user_id);
CREATE INDEX idx_progress_problem ON user_problem_progress(problem_id);
CREATE INDEX idx_progress_status ON user_problem_progress(status);
CREATE INDEX idx_progress_solved ON user_problem_progress(solved_at DESC);
CREATE INDEX idx_progress_bookmarked ON user_problem_progress(bookmarked) WHERE bookmarked = true;
CREATE INDEX idx_progress_last_attempted ON user_problem_progress(last_attempted_at DESC);

COMMENT ON TABLE user_problem_progress IS 'Tracks user progress and engagement with each problem';


-- =====================================================
-- 5.3 USER QUIZ ATTEMPTS TABLE
-- =====================================================
DROP TABLE IF EXISTS user_quiz_attempts CASCADE;

CREATE TABLE user_quiz_attempts (
    id SERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    quiz_id INTEGER REFERENCES quizzes(id) ON DELETE CASCADE,
    problem_id VARCHAR(100) REFERENCES problems(id) ON DELETE CASCADE,
    
    -- Answer details
    selected_answer CHAR(1) NOT NULL CHECK (selected_answer IN ('A', 'B', 'C', 'D')),
    is_correct BOOLEAN NOT NULL,
    
    -- Timing
    time_taken_seconds INTEGER,
    
    -- Attempt number
    attempt_number INTEGER DEFAULT 1,
    
    -- Feedback
    marked_helpful BOOLEAN,
    
    -- Timestamps
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT unique_user_quiz_attempt UNIQUE (user_id, quiz_id, attempt_number)
);

CREATE INDEX idx_quiz_attempts_user ON user_quiz_attempts(user_id);
CREATE INDEX idx_quiz_attempts_quiz ON user_quiz_attempts(quiz_id);
CREATE INDEX idx_quiz_attempts_problem ON user_quiz_attempts(problem_id);
CREATE INDEX idx_quiz_attempts_correct ON user_quiz_attempts(is_correct);
CREATE INDEX idx_quiz_attempts_created ON user_quiz_attempts(created_at DESC);

COMMENT ON TABLE user_quiz_attempts IS 'User attempts at problem-related quizzes';


-- =====================================================
-- 5.4 USER EDITORIAL FEEDBACK TABLE
-- =====================================================
DROP TABLE IF EXISTS user_editorial_feedback CASCADE;

CREATE TABLE user_editorial_feedback (
    id SERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    editorial_id INTEGER REFERENCES editorials(id) ON DELETE CASCADE,
    problem_id VARCHAR(100) REFERENCES problems(id) ON DELETE CASCADE,
    
    -- Feedback type
    feedback_type VARCHAR(50) NOT NULL,              -- 'helpful', 'not-helpful', 'report-issue'
    
    -- Ratings (1-5 scale)
    clarity_rating INTEGER CHECK (clarity_rating BETWEEN 1 AND 5),
    completeness_rating INTEGER CHECK (completeness_rating BETWEEN 1 AND 5),
    helpfulness_rating INTEGER CHECK (helpfulness_rating BETWEEN 1 AND 5),
    
    -- Comments
    comment TEXT,
    issue_description TEXT,
    
    -- Metadata
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_editorial_feedback_user ON user_editorial_feedback(user_id);
CREATE INDEX idx_editorial_feedback_editorial ON user_editorial_feedback(editorial_id);
CREATE INDEX idx_editorial_feedback_problem ON user_editorial_feedback(problem_id);
CREATE INDEX idx_editorial_feedback_type ON user_editorial_feedback(feedback_type);

COMMENT ON TABLE user_editorial_feedback IS 'User feedback and ratings for editorials';


-- =====================================================
-- SECTION 6: ANALYTICS & AGGREGATIONS
-- =====================================================

-- =====================================================
-- 6.1 PROBLEM STATISTICS (Aggregate table)
-- =====================================================
DROP TABLE IF EXISTS problem_statistics CASCADE;

CREATE TABLE problem_statistics (
    problem_id VARCHAR(100) PRIMARY KEY REFERENCES problems(id) ON DELETE CASCADE,
    
    -- Submission stats
    total_submissions INTEGER DEFAULT 0,
    accepted_submissions INTEGER DEFAULT 0,
    acceptance_rate DECIMAL(5,2) DEFAULT 0,
    
    -- Performance stats
    avg_runtime_ms DECIMAL(10,2),
    avg_memory_mb DECIMAL(10,2),
    min_runtime_ms INTEGER,
    min_memory_mb DECIMAL(10,2),
    
    -- User engagement
    unique_users_attempted INTEGER DEFAULT 0,
    unique_users_solved INTEGER DEFAULT 0,
    avg_attempts_to_solve DECIMAL(5,2),
    
    -- Time stats
    avg_solve_time_minutes DECIMAL(10,2),
    median_solve_time_minutes DECIMAL(10,2),
    
    -- Language distribution
    language_distribution JSONB,                     -- {"Python": 45, "Java": 30, "C++": 25}
    
    -- Difficulty feedback
    user_difficulty_avg DECIMAL(3,2),                -- Average user rating of difficulty
    
    -- Last updated
    last_calculated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_problem_stats_acceptance ON problem_statistics(acceptance_rate DESC);
CREATE INDEX idx_problem_stats_updated ON problem_statistics(last_calculated_at);

COMMENT ON TABLE problem_statistics IS 'Aggregated statistics for problems (updated periodically)';


-- =====================================================
-- SECTION 7: TRIGGERS & FUNCTIONS
-- =====================================================

-- =====================================================
-- 7.1 Auto-update updated_at timestamp
-- =====================================================
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Apply to all relevant tables
CREATE TRIGGER update_problems_updated_at
    BEFORE UPDATE ON problems
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_editorials_updated_at
    BEFORE UPDATE ON editorials
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_media_assets_updated_at
    BEFORE UPDATE ON media_assets
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_function_signatures_updated_at
    BEFORE UPDATE ON function_signatures
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_quizzes_updated_at
    BEFORE UPDATE ON quizzes
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_test_cases_updated_at
    BEFORE UPDATE ON test_cases
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_tags_updated_at
    BEFORE UPDATE ON tags
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_progress_updated_at
    BEFORE UPDATE ON user_problem_progress
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_problem_companies_updated_at
    BEFORE UPDATE ON problem_companies
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_problem_stats_updated_at
    BEFORE UPDATE ON problem_statistics
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();


-- =====================================================
-- 7.2 Update tag problem count
-- =====================================================
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
-- 7.3 Update company problem count
-- =====================================================
CREATE OR REPLACE FUNCTION update_company_problem_count()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        UPDATE companies SET problem_count = problem_count + 1 WHERE id = NEW.company_id;
    ELSIF TG_OP = 'DELETE' THEN
        UPDATE companies SET problem_count = problem_count - 1 WHERE id = OLD.company_id;
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_company_count
AFTER INSERT OR DELETE ON problem_companies
FOR EACH ROW
EXECUTE FUNCTION update_company_problem_count();


-- =====================================================
-- 7.4 Update editorial flag on problems
-- =====================================================
CREATE OR REPLACE FUNCTION update_problem_editorial_flag()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        UPDATE problems 
        SET has_editorial = true, 
            editorial_premium = NEW.is_premium
        WHERE id = NEW.problem_id;
    ELSIF TG_OP = 'DELETE' THEN
        UPDATE problems 
        SET has_editorial = false, 
            editorial_premium = false
        WHERE id = OLD.problem_id;
    ELSIF TG_OP = 'UPDATE' THEN
        UPDATE problems 
        SET editorial_premium = NEW.is_premium
        WHERE id = NEW.problem_id;
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_editorial_flag
AFTER INSERT OR UPDATE OR DELETE ON editorials
FOR EACH ROW
EXECUTE FUNCTION update_problem_editorial_flag();


-- =====================================================
-- 7.5 Update quiz statistics
-- =====================================================
CREATE OR REPLACE FUNCTION update_quiz_statistics()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE quizzes
    SET 
        total_attempts = total_attempts + 1,
        correct_attempts = CASE WHEN NEW.is_correct THEN correct_attempts + 1 ELSE correct_attempts END,
        success_rate = ROUND((correct_attempts::DECIMAL / NULLIF(total_attempts, 0)) * 100, 2)
    WHERE id = NEW.quiz_id;
    
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_quiz_stats
AFTER INSERT ON user_quiz_attempts
FOR EACH ROW
EXECUTE FUNCTION update_quiz_statistics();


-- =====================================================
-- 7.6 Update editorial feedback counts
-- =====================================================
CREATE OR REPLACE FUNCTION update_editorial_feedback_counts()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.feedback_type = 'helpful' THEN
        UPDATE editorials SET helpful_count = helpful_count + 1 WHERE id = NEW.editorial_id;
    ELSIF NEW.feedback_type = 'not-helpful' THEN
        UPDATE editorials SET not_helpful_count = not_helpful_count + 1 WHERE id = NEW.editorial_id;
    END IF;
    
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_editorial_feedback
AFTER INSERT ON user_editorial_feedback
FOR EACH ROW
EXECUTE FUNCTION update_editorial_feedback_counts();


-- =====================================================
-- SECTION 8: VIEWS
-- =====================================================

-- =====================================================
-- 8.1 Complete Problem View
-- =====================================================
CREATE OR REPLACE VIEW vw_problems_complete AS
SELECT 
    p.id,
    p.display_id,
    p.title,
    p.slug,
    p.difficulty,
    p.difficulty_score,
    p.category,
    p.subcategory,
    p.is_premium,
    p.subscription_tier,
    p.acceptance_rate,
    p.total_submissions,
    p.total_views,
    p.has_editorial,
    p.editorial_premium,
    
    -- Aggregated tags
    ARRAY_AGG(DISTINCT t.name ORDER BY t.name) FILTER (WHERE t.name IS NOT NULL) as tags,
    ARRAY_AGG(DISTINCT t.slug ORDER BY t.slug) FILTER (WHERE t.slug IS NOT NULL) as tag_slugs,
    
    -- Aggregated companies
    ARRAY_AGG(DISTINCT c.name ORDER BY c.name) FILTER (WHERE c.name IS NOT NULL) as companies,
    
    -- Counts
    COUNT(DISTINCT pe.id) as example_count,
    COUNT(DISTINCT fs.id) as language_count,
    COUNT(DISTINCT tc.id) as test_case_count,
    COUNT(DISTINCT q.id) as quiz_count,
    COUNT(DISTINCT ma.id) as media_asset_count,
    
    -- Timestamps
    p.created_at,
    p.updated_at,
    p.published_at
    
FROM problems p
LEFT JOIN problem_tags pt ON p.id = pt.problem_id
LEFT JOIN tags t ON pt.tag_id = t.id AND t.is_active = true
LEFT JOIN problem_companies pc ON p.id = pc.problem_id
LEFT JOIN companies c ON pc.company_id = c.id AND c.is_active = true
LEFT JOIN problem_examples pe ON p.id = pe.problem_id
LEFT JOIN function_signatures fs ON p.id = fs.problem_id AND fs.is_active = true
LEFT JOIN test_cases tc ON p.id = tc.problem_id AND tc.is_active = true
LEFT JOIN quizzes q ON p.id = q.problem_id AND q.is_active = true
LEFT JOIN media_assets ma ON p.id = ma.problem_id AND ma.is_active = true
WHERE p.is_active = true AND p.is_deleted = false
GROUP BY p.id;


-- =====================================================
-- 8.2 Problem List View (Lightweight for listing)
-- =====================================================
CREATE OR REPLACE VIEW vw_problems_list AS
SELECT 
    p.id,
    p.display_id,
    p.title,
    p.slug,
    p.difficulty,
    p.category,
    p.is_premium,
    p.acceptance_rate,
    p.total_submissions,
    ARRAY_AGG(DISTINCT t.name ORDER BY pt.display_order) FILTER (WHERE t.name IS NOT NULL) as tags,
    p.is_featured,
    p.created_at
FROM problems p
LEFT JOIN problem_tags pt ON p.id = pt.problem_id
LEFT JOIN tags t ON pt.tag_id = t.id AND t.is_active = true
WHERE p.is_active = true AND p.is_deleted = false AND p.is_published = true
GROUP BY p.id;


-- =====================================================
-- 8.3 User Progress Dashboard View
-- =====================================================
CREATE OR REPLACE VIEW vw_user_progress_dashboard AS
SELECT 
    upp.user_id,
    COUNT(*) as total_problems_viewed,
    COUNT(*) FILTER (WHERE upp.status = 'attempted') as attempted_count,
    COUNT(*) FILTER (WHERE upp.status = 'solved') as solved_count,
    COUNT(*) FILTER (WHERE upp.bookmarked = true) as bookmarked_count,
    COUNT(*) FILTER (WHERE p.difficulty = 'Easy' AND upp.status = 'solved') as easy_solved,
    COUNT(*) FILTER (WHERE p.difficulty = 'Medium' AND upp.status = 'solved') as medium_solved,
    COUNT(*) FILTER (WHERE p.difficulty = 'Hard' AND upp.status = 'solved') as hard_solved,
    SUM(upp.total_time_spent_seconds) as total_time_spent_seconds,
    MAX(upp.last_attempted_at) as last_active_at
FROM user_problem_progress upp
JOIN problems p ON upp.problem_id = p.id
GROUP BY upp.user_id;


-- =====================================================
-- 8.4 Editorial with Media Assets View
-- =====================================================
CREATE OR REPLACE VIEW vw_editorials_with_media AS
SELECT 
    e.id,
    e.problem_id,
    e.summary,
    e.is_premium,
    e.view_count,
    e.helpful_count,
    e.not_helpful_count,
    
    -- Aggregate media assets
    jsonb_agg(
        jsonb_build_object(
            'id', ma.id,
            'type', ma.asset_type,
            'category', ma.asset_category,
            'url', ma.file_url,
            'alt_text', ma.alt_text,
            'caption', ma.caption
        ) ORDER BY ma.display_order
    ) FILTER (WHERE ma.id IS NOT NULL) as media_assets,
    
    e.created_at,
    e.updated_at
FROM editorials e
LEFT JOIN media_assets ma ON e.id = ma.editorial_id AND ma.is_active = true
WHERE e.is_active = true
GROUP BY e.id;


-- =====================================================
-- 8.5 Quiz Performance View
-- =====================================================
CREATE OR REPLACE VIEW vw_quiz_performance AS
SELECT 
    q.id as quiz_id,
    q.problem_id,
    q.quiz_type,
    q.difficulty,
    q.total_attempts,
    q.correct_attempts,
    q.success_rate,
    p.title as problem_title,
    p.difficulty as problem_difficulty
FROM quizzes q
JOIN problems p ON q.problem_id = p.id
WHERE q.is_active = true
ORDER BY q.success_rate ASC;


-- =====================================================
-- 8.6 Media Assets Status View
-- =====================================================
CREATE OR REPLACE VIEW vw_media_assets_status AS
SELECT 
    p.id as problem_id,
    p.display_id,
    p.title,
    COUNT(ma.id) as total_assets,
    COUNT(ma.id) FILTER (WHERE ma.is_placeholder = true) as placeholder_count,
    COUNT(ma.id) FILTER (WHERE ma.is_optimized = true) as optimized_count,
    COUNT(ma.id) FILTER (WHERE ma.asset_type = 'image') as image_count,
    COUNT(ma.id) FILTER (WHERE ma.asset_category = 'header') as has_header,
    COUNT(ma.id) FILTER (WHERE ma.asset_category = 'problem-illustration') as has_illustration,
    COUNT(ma.id) FILTER (WHERE ma.asset_category = 'algorithm-steps') as has_algorithm_steps,
    COUNT(ma.id) FILTER (WHERE ma.asset_category = 'visualization') as has_visualization
FROM problems p
LEFT JOIN media_assets ma ON p.id = ma.problem_id AND ma.is_active = true
WHERE p.is_active = true
GROUP BY p.id
ORDER BY placeholder_count DESC, total_assets DESC;


-- =====================================================
-- SECTION 9: UTILITY FUNCTIONS
-- =====================================================

-- =====================================================
-- 9.1 Function to calculate acceptance rate
-- =====================================================
CREATE OR REPLACE FUNCTION calculate_acceptance_rate(p_problem_id VARCHAR)
RETURNS DECIMAL AS $$
DECLARE
    v_total INTEGER;
    v_accepted INTEGER;
BEGIN
    SELECT COUNT(*), COUNT(*) FILTER (WHERE is_accepted = true)
    INTO v_total, v_accepted
    FROM user_submissions
    WHERE problem_id = p_problem_id;
    
    IF v_total = 0 THEN
        RETURN 0;
    END IF;
    
    RETURN ROUND((v_accepted::DECIMAL / v_total) * 100, 2);
END;
$$ LANGUAGE plpgsql;


-- =====================================================
-- 9.2 Function to get user's next recommended problem
-- =====================================================
CREATE OR REPLACE FUNCTION get_recommended_problems(
    p_user_id BIGINT,
    p_limit INTEGER DEFAULT 10
)
RETURNS TABLE (
    problem_id VARCHAR,
    title VARCHAR,
    difficulty VARCHAR,
    relevance_score DECIMAL
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        p.id,
        p.title,
        p.difficulty,
        CAST(0.0 AS DECIMAL) as relevance_score  -- Placeholder for ML scoring
    FROM problems p
    LEFT JOIN user_problem_progress upp ON p.id = upp.problem_id AND upp.user_id = p_user_id
    WHERE p.is_active = true 
        AND p.is_published = true
        AND upp.problem_id IS NULL  -- Not attempted yet
    ORDER BY p.acceptance_rate DESC
    LIMIT p_limit;
END;
$$ LANGUAGE plpgsql;


-- =====================================================
-- SECTION 10: SAMPLE DATA COMMENTS
-- =====================================================

COMMENT ON DATABASE postgres IS 'DSA Platform - Complete schema with problems, editorials, quizzes, images, and user tracking';

-- =====================================================
-- SECTION 11: GRANTS & PERMISSIONS (Adjust as needed)
-- =====================================================

-- Example: Grant read access to application role
-- GRANT SELECT ON ALL TABLES IN SCHEMA public TO app_role;
-- GRANT INSERT, UPDATE, DELETE ON user_submissions, user_problem_progress, user_quiz_attempts TO app_role;
-- GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO app_role;


-- =====================================================
-- END OF SCHEMA
-- =====================================================
-- 
-- USAGE NOTES:
-- 1. Run this script on a fresh PostgreSQL database
-- 2. Adjust user_id type (BIGINT) based on your auth system
-- 3. Configure CDN URLs for media_assets
-- 4. Set up scheduled jobs to update problem_statistics
-- 5. Implement caching for frequently accessed views
-- 6. Consider table partitioning for user_submissions (by date)
-- 7. Add full-text search indexes for advanced search
-- 8. Set up backup and replication strategies
-- 
-- NEXT STEPS:
-- 1. Load sample data using insert scripts
-- 2. Set up Judge0 integration for code execution
-- 3. Implement API layer to interact with this schema
-- 4. Add monitoring and alerting for database performance
-- 5. Create materialized views for heavy analytics
-- =====================================================
