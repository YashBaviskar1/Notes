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

## External Notes : 


- to commit : `curr.commit(query)` directly 
- Primary key syntax : `PRIMARY KEY`
- unlike SQL, AUTO_INCREMENT is actually ; 
`id SERIAL` 
