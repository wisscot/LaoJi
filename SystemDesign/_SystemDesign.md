# System Design

## What to Design

   ### Design A Huge System
    - Twitter
    - Facebook
    - Uber
    - Whatsapp
    - TinyURL

   ### Design A Function
    - Rate Limiter
    - Monitor System
    - Delete a tweet
    - mark email as read

## Scenario (clarification)

 - Functionalities:
    - sign up, sign in, sign out
 - DAU: 100M or 0.5 * MAU
    - read QPS ave.: 100M * 10 / 86400 = ~1k
    - write QPS ave.: 100M * 0.1 / 86400 = ~10
    - read QPS peak: ~3k
    - write QPS peak: ~30
 - API:
    - short_to_long(short_url)

## Services (Split the System into small services)

 - User Service
 - Tweet Service
 - Media Service
 - Friendship Service (or included in User Service)

## Storage (Database, File System, Cache)
 
 - Corresponde to Services
 
 - User Service -> SQL DB
 - Friendship Service -> SQL/NoSQL DB
 - Tweets Service -> NoSQL DB

 Schema:
  - Tweet Table
    - id: integer
    - user_id: fk (Foreign Key)
    - content: text
    - created_at: timestamp

 - Media Service (picture, videos) -> File System

 - no need persistency -> Cache

 - draw to explain the flow

## Scale

 - get a working model by following last three steps (Scenario, Services, Storage)
 - this step is mainly to solver issues 

 - Solve potential issues:
    - Special Cases
    - Single Point Failure
    - Number of users scaled up
    - Slow: Database Index / Sharding
    

## Trade Off



## Message Queue
  - Software: RabbitMQ, Redis, AWS SQS
  - Producer-Consumer model uses this 
  - Reason to use: producer consumer rate difference
  - Used for some operation needs take long time, or need retry
  - Web Server <-> MQ <-> workers <-> DB
  - Applications: user follow, send registration email, book tickets
  - High availablility: Mirroed / double Master

## Pull Model vs Push Model

  - Pull Model: get all friends 100 first tweets, then merge k sorted list
  - Time Complexity: 
    - Get News Feed: O(number of followers) DB read took most of the time, merge can be ignored
    - Post a tweet: O(1)
  - Cons: slow when get

  - Push Model: when a user send a tweet, push it to every subscriber's News Feed (Fanout)
  - add a new News Feed Table
  - id, owner_id, tweed_id, created_at (denomalize)
  - Time Complexity: 
    - Get News Feed: O(1) DB Read
    - Post a tweet: O(number of followers) but can use asycronize
  - Cons: number of followers might be too large
