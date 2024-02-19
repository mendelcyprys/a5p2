import sqlite3

con = sqlite3.connect('db/database.sqlite3')
cur = con.cursor()

sample_patient_data = [
    {
        "name": "Maria Johnson",
        "age": 36,
        "gender": "Female",
        "contact_number": "07856921734",
    },
    {
        "name": "David Smith",
        "age": 45,
        "gender": "Male",
        "contact_number": "07548032917",
    },
    {
        "name": "Emily Brown",
        "age": 19,
        "gender": "Female",
        "contact_number": "07567491823",
    },
    {
        "name": "Daniel Wilson",
        "age": 28,
        "gender": "Male",
        "contact_number": "07931254876",
    },
    {
        "name": "Sophia Taylor",
        "age": 52,
        "gender": "Female",
        "contact_number": "07846290315",
    },
    {
        "name": "Ethan Martinez",
        "age": 37,
        "gender": "Male",
        "contact_number": "07418632957",
    },
    {
        "name": "Olivia Garcia",
        "age": 64,
        "gender": "Female",
        "contact_number": "07956324187",
    },
    {
        "name": "Liam Anderson",
        "age": 31,
        "gender": "Male",
        "contact_number": "07389645217",
    },
    {
        "name": "Ava Hernandez",
        "age": 22,
        "gender": "Female",
        "contact_number": "07123456789",
    },
    {
        "name": "Noah Thomas",
        "age": 49,
        "gender": "Male",
        "contact_number": "07978563412",
    }
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