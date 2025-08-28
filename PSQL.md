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

