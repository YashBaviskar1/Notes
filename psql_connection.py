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
    CREATE TABLE IF NOT EXISTS agent_name(
    id SERIAL PRIMARY KEY,
    name varchar(20) 
    )
    """

    curr.execute(query)
    query2 = f"""
    INSERT INTO agent_name(
    name)
    VALUES (%s)
    """
    value = "Execution_agent"
    curr.execute(query2, (value,))
    conn.commit()
    print("Table Created!")
    curr.close()
    conn.close()
    print("connection closed")
except psycopg2.Error as e : 
    print("Error : ", e )


