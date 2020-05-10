Tweet Table
id: int
user_id: fk
content: text
created_at: timestamp
num_of_likes: int (denomalize, save an extra copy)

Like Table
id: int
user_id: fk
tweet_id: fk
created_at: timestamp