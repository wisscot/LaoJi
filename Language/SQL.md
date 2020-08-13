# SQL

```sql

-- create database
create database xxxdb;

-- create table
CREATE TABLE xxtable (
  id INTEGER,
  name varchar(255)
);

-- delete table
DROP TABLE xxtable

-- insert values
INSERT INTO xxtable VALUES (1, "name")

INSERT INTO xxtable (id, name) VALUES (1, "name")

--query
SELECT * FROM xxtable

-- query w/ conditions
SELECT * FROM xxtable
WHERE name = 'thename'
AND/OR other_conditions;

-- query + sort
SELECT * FROM xxtable
WHERE name = 'thename'
ORDER BY age DESC/ASC;

-- query + sort on two keys
SELECT * FROM xxtable
WHERE name = 'thename'
ORDER BY age, name;

-- update
UPDATE xxtable
SET colume_name = 'sth'

-- delete values
DELETE FROM xxtable


```
