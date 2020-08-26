# SQL

Query

```sql

--query
SELECT * FROM xxtable

-- query w/ conditions + sort
SELECT * FROM xxtable
WHERE col1 = 'value'
AND/OR other_conditions
ORDER BY age DESC/ASC;
;

-- query + sort on two keys
ORDER BY age, name;

-- update
UPDATE xxtable
SET colume_name = 'sth'

-- delete values
DELETE FROM xxtable
```

Create Delete
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

```
