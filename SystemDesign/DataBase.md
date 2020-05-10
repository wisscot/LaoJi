# DataBase

## Popular DB
  - MySQL / PostgreSQL -> SQL
  - Memcached (mem based, key-value -> a big hashtable, no persistance, cache aside)
  - Redis (mem based, support set / list, can be used as cache/message Queue/Database, has persistance, cache through)
  - Cassandra, HBase -> Column Family Based, row-key and column-key (column-key for simple range query)
  - MongoDB, Document based, optimized for write (log)
  - Rocksdb, key-value hard drive based

## Choose between SQL vs NoSQL
  - most cases, both are ok
  - If require transaction/relationship, then has to be SQL
  - Performance: NoSQL is better > 1k QPS
  - Sharding: NoSQL is better
  - NoSQL was design to adress loging problem (lots of log, need write)

## choose based on QPS and read/write
  - MySQL max ~1k QPS
  - MongoDB max ~10k QPS
  - Redis max ~100k - 1M QPS

## PK & FK
  - primary key: identify the row
  - foreign key: like reference

## TTL
  - basically LRU

## Index
  - if no index, have to loop all items to search
  - index can speed up equal query and range query
  - index implementation
    - tree index (b+ tree, multiple brach search tree reduce height), support range query
    - hash index 
  - index types
    - composite index (secondary index) -> combine two columes to build index
    - primary index
    - condition index

## Sharding:
  - Vertical Sharding
  - Horizal Sharding (use Consistent Hashing)
  - Consistent Hashing (2^64): 1000 virtual nodes per node, find next large hash value -> node to use

## Replica:
  - SQL (built-in): master - slave model
  - NoSQL (built-in): Save 3 copies in Consistent Hashing Ring clockwise




