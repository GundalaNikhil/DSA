
-- =====================================================
-- DSA PLATFORM — V1 CANONICAL SCHEMA
-- File: platform.sql
-- PostgreSQL 14+
-- Git → CI → DB architecture
-- =====================================================

CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- -----------------------------
-- PROBLEMS
-- -----------------------------
CREATE TABLE problems (
  problem_id TEXT PRIMARY KEY,
  display_id TEXT NOT NULL UNIQUE,
  slug TEXT NOT NULL UNIQUE,

  title TEXT NOT NULL,
  difficulty TEXT CHECK (difficulty IN ('Easy','Medium','Hard')),
  category TEXT,

  problem_html TEXT NOT NULL,

  time_limit_ms INT,
  memory_limit_mb INT,

  is_premium BOOLEAN DEFAULT false,
  subscription_tier TEXT,

  version INT NOT NULL DEFAULT 1,
  is_published BOOLEAN DEFAULT false,

  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);


-- -----------------------------
-- EDITORIALS
-- -----------------------------
CREATE TABLE editorials (
  problem_id TEXT PRIMARY KEY
    REFERENCES problems(problem_id) ON DELETE CASCADE,

  editorial_html TEXT NOT NULL,
  version INT NOT NULL DEFAULT 1,

  is_premium BOOLEAN DEFAULT false,
  is_published BOOLEAN DEFAULT true,

  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- -----------------------------
-- IMAGES / MEDIA
-- -----------------------------
CREATE TABLE problem_images (
  image_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  problem_id TEXT REFERENCES problems(problem_id) ON DELETE CASCADE,
  image_key TEXT NOT NULL,
  image_url TEXT NOT NULL,
  image_type TEXT CHECK (image_type IN ('problem','editorial','example','diagram')),
  created_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(problem_id, image_key)
);

-- -----------------------------
-- FUNCTION SIGNATURES
-- -----------------------------
CREATE TABLE function_signatures (
  signature_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  problem_id TEXT REFERENCES problems(problem_id) ON DELETE CASCADE,
  language_name TEXT NOT NULL,
  language_id INT,
  function_name TEXT NOT NULL,
  return_type TEXT,
  parameters JSONB,
  starter_code TEXT NOT NULL,
  runner_code TEXT NOT NULL,
  version INT DEFAULT 1,
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(problem_id, language_name)
);

-- -----------------------------
-- TEST CASES
-- -----------------------------
CREATE TABLE test_cases (
  test_case_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  problem_id TEXT REFERENCES problems(problem_id) ON DELETE CASCADE,
  input JSONB NOT NULL,
  expected_output JSONB NOT NULL,
  is_hidden BOOLEAN DEFAULT false,
  is_sample BOOLEAN DEFAULT false,
  time_limit_ms INT,
  memory_limit_mb INT,
  created_at TIMESTAMP DEFAULT NOW()
);

-- -----------------------------
-- QUIZZES
-- -----------------------------
CREATE TABLE quizzes (
  quiz_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  problem_id TEXT REFERENCES problems(problem_id) ON DELETE CASCADE,
  title TEXT NOT NULL,
  passing_score INT NOT NULL,
  version INT DEFAULT 1,
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE quiz_questions (
  question_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  quiz_id UUID REFERENCES quizzes(quiz_id) ON DELETE CASCADE,
  category TEXT CHECK (category IN ('problem','editorial','code','complexity')),
  type TEXT CHECK (type IN ('single_choice','multiple_choice','true_false')),
  question_text TEXT NOT NULL,
  code_snippet TEXT,
  language TEXT,
  points INT NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE quiz_options (
  option_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  question_id UUID REFERENCES quiz_questions(question_id) ON DELETE CASCADE,
  option_key TEXT,
  option_text TEXT NOT NULL,
  is_correct BOOLEAN DEFAULT false
);

-- -----------------------------
-- USER SUBMISSIONS
-- -----------------------------
CREATE TABLE user_submissions (
  submission_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id BIGINT NOT NULL,
  problem_id TEXT REFERENCES problems(problem_id),
  language_name TEXT,
  language_id INT,
  source_code TEXT NOT NULL,
  verdict TEXT,
  runtime_ms INT,
  memory_mb DECIMAL(10,2),
  judge0_token TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);

-- -----------------------------
-- USER PROGRESS
-- -----------------------------
CREATE TABLE user_problem_progress (
  user_id BIGINT NOT NULL,
  problem_id TEXT REFERENCES problems(problem_id),
  status TEXT CHECK (status IN ('not_started','attempted','solved')) DEFAULT 'not_started',
  solved_at TIMESTAMP,
  total_attempts INT DEFAULT 0,
  PRIMARY KEY (user_id, problem_id)
);

-- -----------------------------
-- USER QUIZ ATTEMPTS
-- -----------------------------
CREATE TABLE user_quiz_attempts (
  attempt_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id BIGINT NOT NULL,
  quiz_id UUID REFERENCES quizzes(quiz_id),
  score INT NOT NULL,
  passed BOOLEAN DEFAULT false,
  created_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(user_id, quiz_id)
);
