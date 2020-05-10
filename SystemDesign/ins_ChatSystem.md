# Chat System
 
## Scenario

Basic functionalities:
    User login / logout / Signup
    Contacts (Friendships)
    Send message (1 to 1) 
    Send message (group chat)
    online status

Others:
    Chat history
    Multi Devices

DAU -> 100M (10^8)

QPS ave. -> 100M * 20 / 86400 = ~20k
QPS peak -> *5 = ~100k
most are write op. ->  distributed db / sharding

Storage:
10 message / user / day * 30 B / message -> 300 B / user / day
300 * 100 MB = 30 GB / day


## Service

Message Service

Real-time Service


## Storage

Message Table Schema
id: int
from_user_id: int
thread_id: fk
content: text
created_at: timestamp

Thread Table Schema
thread_id: int
owner_id: int
participant_ids: text  e.g. [1,2]
nickname: text
created_at: timestamp
updated_at: timestamp  index
is_muted: bool

Message Table, a lot, does not need modify -> NoSQL
Tread Table, index by ower_id + thread_id, secondary index by updatedtime -> SQL


## Scale

Message Table Sharding - row key: thread_id

Thread Table Sharding - row key: owner_id

Speed UP: Socket (Push Service)

Large group chat: Channel Service

 