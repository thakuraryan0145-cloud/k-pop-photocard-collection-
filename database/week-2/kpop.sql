
-- =====================================================
-- WEEK 2: SAMPLE DATA
-- Project: K-Pop Photocard Collection
-- Task: Insert and verify groups, idols and users
-- =====================================================


-- W2.1: Insert groups
-- Groups are added first because idols depend on them.

INSERT INTO groups (name, agency, debut_date)
VALUES
    ('BTS', 'Big Hit Music', '2013-06-13'),
    ('BLACKPINK', 'YG Entertainment', '2016-08-08'),
    ('TWICE', 'JYP Entertainment', '2015-10-20'),
    ('Stray Kids', 'JYP Entertainment', '2018-03-25'),
    ('iKON', '143 Entertainment', '2015-09-15');


-- W2.2: Insert idols
-- The group name is used to find the correct group_id.

INSERT INTO idols (stage_name, group_id)
SELECT v.stage_name, g.group_id
FROM (
    VALUES
        ('RM', 'BTS'),
        ('Jin', 'BTS'),
        ('Suga', 'BTS'),
        ('Jisoo', 'BLACKPINK'),
        ('Jennie', 'BLACKPINK'),
        ('Rosé', 'BLACKPINK'),
        ('Nayeon', 'TWICE'),
        ('Jeongyeon', 'TWICE'),
        ('Momo', 'TWICE')
) AS v(stage_name, group_name)
JOIN groups g
    ON g.name = v.group_name;


-- W2.3: Insert sample users
-- These values are for testing only, not real passwords.

INSERT INTO users (email, display_name, password_hash)
VALUES
    ('aisha@example.com', 'Aisha', 'test_hash_1'),
    ('riya@example.com', 'Riya', 'test_hash_2'),
    ('meera@example.com', 'Meera', 'test_hash_3');


-- W2.4: Verify inserted data

SELECT COUNT(*) AS total_groups
FROM groups;

SELECT COUNT(*) AS total_idols
FROM idols;

SELECT COUNT(*) AS total_users
FROM users;


-- Display idols with their group names

SELECT
    g.name AS group_name,
    i.stage_name
FROM groups g
JOIN idols i
    ON i.group_id = g.group_id
ORDER BY g.name, i.stage_name;
