# DataBase

## Type: SQL vs NoSQL
  - most cases, both are ok
  - If require transaction, then has to be SQL
  - Performance: NoSQL is better
  - Sharding: NoSQL is better

## How to make it faster
  - build index
    * tree index (b+ tree), support range query
    * hash index 




## Design User System

### Scenario

sign up, log in, look up, modify  -> most is look up
^           ^       ^       ^
write     write     read    write

assume 100M DAU 

sign up, log in, modify : QPS = 100M * 0.1 / 86400 ~100  Peak *3 ~300
Look up QPS = 100M * 100 / 86400 ~100k  Peak (*3) ~300k

MySQL max ~1k QPS
MongoDB max ~10k QPS
Redis max ~100k - 1M QPS


### Service

AuthService: for login
  - keep login:  Session Table with session key / user id / expire at

UserService: for save and look up

FriendshipService: for freind relationship
  - Friedship type: one- way / two-way
  - SQL vs NoSQL: 
    * most cases, both are ok
    * If require transaction, then has to be SQL
    * Performance: NoSQL is better
    * Sharding: NoSQL is better
  - Sharding:
    * Vertical Sharding
    * Horizal Sharding (use Consistent Hashing)
    * Consistent Hashing (2^64): 1000 virtual nodes per node, find next large hash value -> node to use
  - Replica:
    * SQL (built-in): 1 master, 2 slaves
    * NoSQL (built-in): Save 3 copies in Consistent Hashing Ring clockwise

### Storage

System facing users: Read a lot more than Write

Cache: Key - Value
    - Memcached (not support persistance)
    - Redis (support persistance)

Optimize DB query:
cache.delete(key)  # delete first
database.set(user) # add to db second
so that if first step failed, there will be no inconsistance

