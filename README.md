
# SnitchDB – A Simple Redis Clone (Using Redis Protocol)

SnitchDB is a lightweight, Redis-compatible in-memory database built in Python.  
It supports core Redis commands such as `PING`, `ECHO`, `SET`, `GET`, and expiry options like `EX` and `PX`.

---

dev_repo : https://github.com/thushan-123/redis_server.git

## ✅ Features

| Command | Description |
|---------|------------|
| `PING` | Check connection to the server |
| `ECHO <message>` | Returns the same message |
| `SET key value` | Store a key-value pair |
| `SET key value PX <ms>` | Store key with expiration in milliseconds |
| `SET key value EX <sec>` | Store key with expiration in seconds |
| `GET key` | Retrieve stored value |
| Auto-expiry | Keys expire automatically when TTL is over |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/snitchdb.git
cd snitchdb
````


> ⚠ Make sure you have **pipenv** installed
> Install it using:
>
> ```bash
> pip install pipenv
> ```

### 3️⃣ Start the Server

```
./snitch.sh
```

You should see:

```
----- SNITCH_DB ----- (redis protocol)
Server Listen Port: 6379
```

---

## 🖥 Connect Using redis-cli

Open a new terminal and run:

```bash
redis-cli -p 6379
```

---

## 📌 Usage Examples

### 🔹 PING Command

```
127.0.0.1:6379> ping
PONG

127.0.0.1:6379> ping hello
"hello"
```

---

### 🔹 ECHO Command

```
127.0.0.1:6379> echo "hii i am redis clone"
"hii i am redis clone"
```

---

### 🔹 SET & GET

```
127.0.0.1:6379> SET user1 kamal
OK

127.0.0.1:6379> GET user1
"kamal"
```

---

### ⏳ SET With Expiration (Milliseconds)

```
127.0.0.1:6379> SET otp1 1212 PX 20000
OK

127.0.0.1:6379> GET otp1
"1212"

# After 20 seconds:
127.0.0.1:6379> GET otp1
(nil)
```

---

### ⏳ SET With Expiration (Seconds)

```
127.0.0.1:6379> SET sess abc123 EX 20
OK

127.0.0.1:6379> GET sess
"abc123"

# After 20 seconds:
127.0.0.1:6379> GET sess
(nil)
```

---

## 📁 Project Structure

```
SnitchDB/
│── app/
│   ├── main.py
│   ├── command.py
│   ├── DataStore/
│   ├── DarkWizardEncodeDecode/
│   ├── RDBFileConfig/
│── snitch.sh
│── Pipfile
│── Pipfile.lock
│── README.md 
```

<!-- 
SnitchDB (Redis protocol)


run the server

```
./snitch.sh
----- SNITCH_DB ----- (redis protocol) 

Server Listen Port: 6379

```

client application is redis-cli

PING command
127.0.0.1:6379> ping
PONG

127.0.0.1:6379> ping hii
"hii"


127.0.0.1:6379> ping hello world
"hello world"


ECHO command

127.0.0.1:6379> echo "hii i am redis clone"
"hii i am redis clone"

SET command

127.0.0.1:6379> SET user1 kamal
OK

GET command

127.0.0.1:6379> GET user1
"kamal"

SET command with expiration time miliseconds

127.0.0.1:6379> SET otp1 1212 PX 20000
OK

127.0.0.1:6379> GET otp1
"1212"

127.0.0.1:6379> GET otp1
(nil)

SET command with expiration time seconds

127.0.0.1:6379> SET sess abc123 EX 20
OK

127.0.0.1:6379> GET sess
"abc123"

127.0.0.1:6379> GET sess
(nil)





 -->
