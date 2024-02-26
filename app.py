from flask import Flask, render_template, g, request
import sqlite3
from db.schema import initialise

app = Flask(__name__)

DATABASE = 'db/database.sqlite3'

# the following three functions are helper functions for database queries
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

# this will create the database and tables if they don't exist
# when the server is started
with app.app_context():
    cur = get_db().cursor()
    initialise(cur)

@app.route("/")
def home():
    cur = get_db().cursor()
    return render_template(
        'home.html',
    )

@app.route("/doctors")
def doctors():
    return render_template(
        'doctors.html',
        doctor_data=query_db('select * from doctors'),
        active="doctors",
    )

@app.route("/patients")
def patients():
    return render_template(
        'patients.html',
        patient_data=query_db('select * from patients'),
        active="patients",
    )

@app.route("/appointments")
def appointments():
    cur = get_db().cursor()
    return render_template(
        'appointments.html',
        active="appointments",
    )


@app.post("/clicked")
def clicked():
    return "<span>I come from the server!</span>"




@app.get("/new_doctor_form")
def new_doctor_form():
    return render_template(
        'components/doctors/new.html',
        form_data={
            'name': '',
            'age': '',
            'gender': 'Choose',
            'number': '',
        }
    )

@app.post("/submit_doctor_form")
def submit_doctor_form():
    form_data = request.form.to_dict()
    
    # some data validation
    if not form_data["age"].isdigit() or int(form_data["age"]) < 0:
        return render_template(
            'components/doctors/new.html',
            form_data=form_data,
            age_error=True,
        )
    if form_data["gender"] not in ["Male", "Female", "Other"]:
        return render_template(
            'components/doctors/new.html',
            form_data=form_data,
            gender_error=True,
        )
    
    # add to database
    cur = get_db().cursor()
    cur.execute("""
            INSERT INTO doctors (
                name,
                age,
                gender,
                contact_number
            ) VALUES (?, ?, ?, ?);
    """,
    (
        form_data["name"],
        form_data["age"],
        form_data["gender"],
        form_data["number"],
    ))
    # not sure if this is the best way to do this
    getattr(g, '_database', None).commit()

    return render_template(
        'components/doctors/data.html',
        doctor_data=query_db('select * from doctors'),
    )




@app.post("/delete_doctor")
def delete_doctor():
    form_data = request.form.to_dict()
    print(form_data)
    
    # add to database
    cur = get_db().cursor()
    print(form_data["doctor_id"])
    cur.execute("""
            DELETE FROM doctors
            WHERE doctor_id = ?;
        """,
        (str(int(form_data["doctor_id"])), ),
    )
    # not sure if this is the best way to do this
    getattr(g, '_database', None).commit()

    return render_template(
        'components/doctors/data.html',
        doctor_data=query_db('select * from doctors'),
    )