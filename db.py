from sqlalchemy import create_engine,text

# dialect + DBapi:///:location db:
engine = create_engine("mysql+pymysql://root@127.0.0.1/corsosql?charset=utf8mb4")
with engine.connect() as conn:

    # Esempio di query per selezionare dati dalla tabella partecipanti (ad esempio, per controllare se è vuota)
    sqlSelect = text("SELECT * FROM partecipanti")
    res = conn.execute(sqlSelect)
    print(res.all())  # Stampa i risultati della query di selezione