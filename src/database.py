import psycopg2

def salvar_no_postgres(cidade, pais, temperatura, umidade, clima, data_coleta):
    conn = psycopg2.connect(
        host="localhost",
        database="weather_db",
        user="postgres",
        password="SUA_SENHA"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO weather_data (cidade, pais, temperatura, umidade, clima, data_coleta)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (cidade, pais, temperatura, umidade, clima, data_coleta)
    )

    conn.commit()
    cursor.close()
    conn.close()
