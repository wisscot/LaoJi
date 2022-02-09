# Design User System

## Scenario

Functionalities:
    sign up, log in, look up, modify  -> most is look up
    ^           ^       ^       ^
    write     write     read    write

DAU: assume 100M 

Write QPS (sign up, log in, modify) = 100M * 0.1 / 86400 ~100  Peak *3 ~300
Read QPS = 100M * 100 / 86400 ~100k  Peak (*3) ~300k

User (human) oriented service: Read a lot more than Write

## Service

AuthService: for login and keep login
  - login: create a session obj, return session_key as cookie to client, save it to Session Table
  - logout: delete from Session Table

UserService: for user info storage and look up

FriendshipService: for freind relationship
  - Friedship type: one- way / two-way

## Storage

AuthService -> User Table / Session Table (keep login with session key / user id / expire at)

UserService -> User Table

FiendshipService -> Friendship Table

Schema:
 - Session Table
    - session_key: string
    - user_id: fk
    - expire_at: timestamp

 - User Table
    - id: integer
    - username: varchar
    - email: varchar
    - password: varchar (hash, salted)
    
 - Friendship Table
    - from_user_id: fk
    - to_user_id: fk
    - created_at: timestamp


## Scale

Optimize DB query:
cache.delete(key)  # delete first
database.set(user) # add to db second
so that if first step failed, there will be no inconsistance