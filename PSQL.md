***Postgress Basics***


**Initially** : After installing and starting the psql database, and putting username and password this is what it looks like : 
```psql 
postgres=#
```

### Basic utilies 
```psql 
postgres=# help
```
- commands start with backslah : \

- quit 
```
postgres=# \q
```

- Listing Databases : 
```psql
\l
```

### Database connection using docker 

```bash
docker exec -it db psql -U postgres
```
to connect to a docker psql image and executing commnads accordingly

### Creating Database 
```sql 
CREATE DATABASE database_name;
```


### Connecting to Database 
**remotely using docker**
- Assuming the database name : _agent_data_
```bash 
docker exec -it db psql -h localhost -p 5432 -U postgres agent_data;
```

**inside the psql user**
```bash
postgres=# \c agent_data
You are now connected to database "agent_data" as user "postgres".
agent_data=#
```


### Deteting Database 

```sql
DROP DATABASE database_name;
```
- **Dangerous**




### Connection Code with Python 

- Required libraries : `psycopg2`

**Basic Connection Code : ** 
```python
import psycopg2
try : 
    conn  = psycopg2.connect(
        host = "localhost",
        port = "5432",
        database = "agent_data",
        user = "postgres",
        password = "123456"
    )

    print("Successful Connection")
    curr = conn.cursor()

    query = """
    CREATE TABLE agent_name(
    id INT SERIAL AUTO_INCREMENT,
    name varchar(20) 
    )
    """

    curr.execute(query)
    conn.commit()
    print("Table Created")
    curr.close()
    conn.close()
    print("connection closed")
except psycopg2.Error as e : 
    print("Error : ", e )

```

### Tables 
- to see the created table 
```sql 
\d 
```
- d stands for describes 

```sql 
\d table_name
```

#### Instering into Tables   
```sql
INSERT INTO table_name(
    col_name
) VALUES ('values)
```

- Instering into tables using python  : 
```python 
query = "INSERT INTO agent_name(name)values(%s)"
value = "Execution agent"
curr.execute(query, (value,))
curr.commit()
```


#### PgVector Inside PSQL 

**Installation of Pgvector inside a existing container**

1. going inside the container : 
```bash 
docker exec -it db bash
```

2.  Install and build tools and pgvector 
```bash
apt-get update
apt-get install -y git build-essential postgresql-server-dev-17
git clone --branch v0.7.0 https://github.com/pgvector/pgvector.git
cd pgvector
make
make install
```
3. Restart Posgres container and run inside psql
```bash 
CREATE EXTENSTION vector;
```



#### Understading storing in Pgvector and very basic opertions 

- Creating a table with {embedding}

```sql 
CREATE TABLE documentts(
    id SERIAL PRIMARY KEY,
    content TEXT,
    embedding vector(3)
)
```

| Sentences | Example Embeddings | 
| :------- | :------: | 
| I love databases  | [0.1, 0.9, 0.3] | 
| Postgres is awesome | [0.2, 0.8, 0.4]  | 
| I enjoy playing football | [0.9, 0.1, 0.2]|

### **OPERATIONS in PgVECTOR**

1) **`<->`** : **Eulidean Distance : **

$x = (x_1, x_2, \dots, x_n)$ and $y = (y_1, y_2, \dots, y_n)$ is:

$$
d(x, y) = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}
$$

- Meaning: Straight-line distance between two points.

- Smaller = more similar.
```sql 
SELECT * FROM notes ORDER BY embedding <-> '[0.15, 0.85, 0.35]';
```

2) `<#>` : **Inner Product**

$x = (x_1, x_2, \dots, x_n)$ and $y = (y_1, y_2, \dots, y_n)$ is:

$$
\langle x, y \rangle = \sum_{i=1}^{n} x_i y_i
$$ 

- Larger = more similar.
- Used a lot in machine learning when vectors are normalized.
```sql 
SELECT * FROM notes ORDER BY embedding <#> '[0.15, 0.85, 0.35]';
```

3. `<=>` — **Cosine Distance**
$x = (x_1, x_2, \dots, x_n)$ and $y = (y_1, y_2, \dots, y_n)$ is:

$$
\text{cosine\_sim}(x, y) = \frac{\langle x, y \rangle}{\|x\|_2 \, \|y\|_2}
$$

The **Cosine Distance** is then defined as:

$$
\text{cosine\_dist}(x, y) = 1 - \text{cosine\_sim}(x, y)
$$

- Range: 0 (same direction, very similar) to 2 (opposite direction).

- Very common for text embeddings, because it cares about direction not magnitude.

```sql 
SELECT * FROM notes ORDER BY embedding <=> '[0.15, 0.85, 0.35]';
```
## External Notes : 


- to commit : `curr.commit(query)` directly 
- Primary key syntax : `PRIMARY KEY`
- unlike SQL, AUTO_INCREMENT is actually ; 
`id SERIAL` 
