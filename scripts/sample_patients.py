import sqlite3

con = sqlite3.connect('db/database.sqlite3', autocommit=False)
cur = con.cursor()

sample_patient_data = [
    {
        "name": "John",
        "age": 25,
        "gender": "Male",
        "contact_number": "07936254637",
    },
    {
        "name": "Alice",
        "age": 22,
        "gender": "Female",
        "contact_number": "07836452431",
    },
    {
        "name": "Bob",
        "age": 56,
        "gender": "Male",
        "contact_number": "07765482739",
    },
]

try:
    for patient in sample_patient_data:
        cur.execute("""
                    INSERT INTO patients (
                        name,
                        age,
                        gender,
                        contact_number
                    ) VALUES (?, ?, ?, ?);
            """,
            (
                patient["name"],
                patient["age"],
                patient["gender"],
                patient["contact_number"],
            )
        )
except:
    con.rollback()
    con.close()
    raise SystemError("An error occurred whilst writting to the database.")
else:
    con.commit()
    con.close()