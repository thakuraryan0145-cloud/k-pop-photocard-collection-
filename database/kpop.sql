
-- =====================================================
-- WEEK 1: DATABASE SCHEMA V1
-- Project: K-Pop Photocard Collection
-- Task: Create groups, idols, users and verify constraints
-- =====================================================

CREATE EXTENSION IF NOT EXISTS pgcrypto;


-- W1.1: Groups table
-- Stores basic information about each K-pop group.

CREATE TABLE groups (
    group_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(90) NOT NULL UNIQUE,
    agency VARCHAR(40),
    debut_date DATE,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);


-- W1.2: Idols table
-- Each idol belongs to a group.
-- Stage names must be unique within the same group.

CREATE TABLE idols (
    idol_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    stage_name VARCHAR(90) NOT NULL,
    group_id UUID NOT NULL,
    birth_date DATE,
    position VARCHAR(50),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    CONSTRAINT fk_idol_group
        FOREIGN KEY (group_id)
        REFERENCES groups(group_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT uq_idol_group_stage_name
        UNIQUE (group_id, stage_name)
);


-- W1.3: Users table
-- Stores user details and their favorite group.
-- Only collector and admin roles are allowed.

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(100) NOT NULL UNIQUE,
    display_name VARCHAR(50) NOT NULL,
    password_hash VARCHAR(333) NOT NULL,
    favorite_group_id UUID,
    role VARCHAR(20) NOT NULL DEFAULT 'collector',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    CONSTRAINT fk_user_favorite_group
        FOREIGN KEY (favorite_group_id)
        REFERENCES groups(group_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,

    CONSTRAINT chk_user_role
        CHECK (role IN ('collector', 'admin'))
);


-- W1.4: Verify tables and constraints
-- These queries help confirm that the schema was created.

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
  AND table_name IN ('groups', 'idols', 'users')
ORDER BY table_name;

SELECT table_name, constraint_name, constraint_type
FROM information_schema.table_constraints
WHERE table_schema = 'public'
  AND table_name IN ('groups', 'idols', 'users')
ORDER BY table_name, constraint_name;
