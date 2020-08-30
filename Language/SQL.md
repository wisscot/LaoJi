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

-- deduplicate
SELECT DISTINCT ...

-- count
SELECT count(*) AS count
WHERE ...

-- count group
SELECT col1, count(*) AS count
WHERE ...
GROUP BY col1

-- count on condition
SELECT
SUM(CASE WHEN col1 > 50 AND col2 like "%war%" THEN 1 ELSE 0 END)

-- case
CASE 
WHEN cond1 THEN res1
WHEN cond2 THEN res2
ELSE res3
END

-- cast
CAST(col_int as float)

-- join
SELECT table1.col1, table1.col2, table2.col1
FROM table1
JOIN table2 ON table1.id=table2.id;
```

Index
```sql
create index index_name on table1 (col1)
```


CRUD
```sql
-- create database
create database db1

-- create table
CREATE TABLE table1 (
  col1 INTEGER,
  col2 TEXT,
  col3 REAL
)

-- delete table
DROP TABLE xxtable

-- insert values
INSERT INTO table1 VALUES (1, "name")

INSERT INTO table1 (id, name) VALUES (1, "name")

-- update
UPDATE xxtable
SET colume_name = 'sth'

-- delete values
DELETE FROM xxtable
```
