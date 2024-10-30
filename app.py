from flask import Flask, render_template, url_for, redirect, request, flash
from sqlalchemy import create_engine, text

app = Flask(__name__)
app.secret_key = 'una_chiave_segreta_molto_lunga'

engine = create_engine("mysql+pymysql://root@127.0.0.1/corsosql?charset=utf8mb4")

def get_partecipante_by_id(id_partecipante):
    with engine.connect() as conn:
        sqlSelect = text("SELECT * FROM partecipanti WHERE id = :id")
        result = conn.execute(sqlSelect, {"id": id_partecipante})
        partecipante = result.fetchone()
        
        if partecipante is None:
            return "Partecipante non trovato", 404
            
        return render_template("singoloPartecipante.html", partecipante=partecipante)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/partecipanti")
def about():
    try:
        with engine.connect() as conn:
            sqlSelect = text("SELECT * FROM partecipanti")
            result = conn.execute(sqlSelect)
            partecipanti = result.fetchall()
            return render_template("partecipanti.html", partecipanti=partecipanti)
    except Exception as e:
        print(f"Errore durante il recupero dei partecipanti: {e}")
        flash("Errore durante il recupero dei partecipanti", "error")
        return render_template("partecipanti.html", partecipanti=[])

@app.route("/partecipanti/<int:id_partecipante>")
def visualizza_partecipante(id_partecipante):
    print("viasualizza",id_partecipante)
    return get_partecipante_by_id(id_partecipante)
    
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            nome = request.form["nome"]
            cognome = request.form["cognome"]
            numero_maglia = request.form["numero_maglia"]
            email = request.form["email"]

            with engine.connect() as conn:
                sqlInsert = text("""
                INSERT INTO partecipanti (nome, cognome, numero_maglia, email) 
                VALUES (:nome, :cognome, :numero_maglia, :email)
                """)
                conn.execute(sqlInsert, {
                    "nome": nome,
                    "cognome": cognome,
                    "numero_maglia": numero_maglia,
                    "email": email
                })
                conn.commit()
            
            flash("Registrazione completata con successo!", "success")
            return redirect(url_for("about"))
        except Exception as e:
            print(f"Errore durante la registrazione: {e}")
            flash("Errore durante la registrazione", "danger")
            return redirect(url_for("register"))

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)