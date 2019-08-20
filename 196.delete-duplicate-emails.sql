--
-- @lc app=leetcode id=196 lang=mysql
--
-- [196] Delete Duplicate Emails
--
-- https://leetcode.com/problems/delete-duplicate-emails/description/
--
-- database
-- Easy (34.34%)
-- Likes:    293
-- Dislikes: 367
-- Total Accepted:    79.4K
-- Total Submissions: 230.8K
-- Testcase Example:  '{"headers": {"Person": ["Id", "Email"]}, "rows": {"Person": [[1, ' +
--  '"john@example.com"], [2, "bob@example.com"], [3, ' +
--  '"john@example.com"]]}}'
--
-- Write a SQL query to delete all duplicate email entries in a table named
-- Person, keeping only unique emails based on its smallest Id.
-- 
-- 
-- +----+------------------+
-- | Id | Email            |
-- +----+------------------+
-- | 1  | john@example.com |
-- | 2  | bob@example.com  |
-- | 3  | john@example.com |
-- +----+------------------+
-- Id is the primary key column for this table.
-- 
-- 
-- For example, after running your query, the above Person table should have
-- the following rows:
-- 
-- 
-- +----+------------------+
-- | Id | Email            |
-- +----+------------------+
-- | 1  | john@example.com |
-- | 2  | bob@example.com  |
-- +----+------------------+
-- 
-- 
-- Note:
-- 
-- Your output is the whole Person table after executing your sql. Use delete
-- statement.
-- 
--
# Write your MySQL query statement below
delete from Person where Id in (select Id from (select * from Person inner join (select Email mail, min(Id) m from Person where Email in (
            select Email count from Person group by Email having count(Id) > 1
    ) group by Email) as d where Person.Email = d.mail) as e where e.Id > e.m);


