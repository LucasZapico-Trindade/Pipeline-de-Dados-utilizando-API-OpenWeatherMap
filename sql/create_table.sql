CREATE TABLE weather_data (
id SERIAL PRIMARY KEY,
cidade VARCHAR(100),
pais VARCHAR(10),
temperatura DECIMAL(5,2),
umidade INT,
clima VARCHAR(100),
data_coleta TIMESTAMP
);