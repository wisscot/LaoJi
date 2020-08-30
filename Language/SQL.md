# SQL

Query

```sql
-- query w/ conditions + sort
SELECT * 
FROM table1
WHERE col1 = 'value'
AND/OR col2 > DATE('2017-01-01')
ORDER BY col3 DESC/ASC

-- query + sort on two keys
ORDER BY age, name

-- count
SELECT count(*) AS count
WHERE ...

-- count group
SELECT col1, count(*) AS count
WHERE ...
GROUP BY col1
```

CRUD
```sql
-- create database
create database xxxdb

-- create table
CREATE TABLE xxtable (
  id INTEGER,
  name varchar(255)
)

-- delete table
DROP TABLE xxtable

-- insert values
INSERT INTO xxtable VALUES (1, "name")

INSERT INTO xxtable (id, name) VALUES (1, "name")

-- update
UPDATE xxtable
SET colume_name = 'sth'

-- delete values
DELETE FROM xxtable
```
