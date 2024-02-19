import sqlite3

con = sqlite3.connect('db/database.sqlite3')
cur = con.cursor()

sample_doctor_data = [
    {
        "name": "Dr. Brian Hernandez",
        "age": 37,
        "gender": "Male",
        "contact_number": "07926678374",
    },
    {
        "name": "Dr. Samantha Kim",
        "age": 58,
        "gender": "Female",
        "contact_number": "07846378714",
    },
    {
        "name": "Dr. Jason Nguyen",
        "age": 45,
        "gender": "Male",
        "contact_number": "07748378924",
    },
    {
        "name": "Dr. Karen Thompson",
        "age": 61,
        "gender": "Female",
        "contact_number": "07453657628",
    },
    {
        "name": "Dr. Rachel Rodriguez",
        "age": 26,
        "gender": "Female",
        "contact_number": "07809128376",
    },
    {
        "name": "Dr. Christopher Brown",
        "age": 66,
        "gender": "Male",
        "contact_number": "07273879809",
    },
]


try:
    for doctor in sample_doctor_data:
        cur.execute("""
                    INSERT INTO doctors (
                        name,
                        age,
                        gender,
                        contact_number
                    ) VALUES (?, ?, ?, ?);
            """,
            (
                doctor["name"],
                doctor["age"],
                doctor["gender"],
                doctor["contact_number"],
            )
        )
except:
    con.rollback()
    con.close()
    raise SystemError("An error occurred whilst writting to the database.")
else:
    con.commit()
    con.close()