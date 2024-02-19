import sqlite3

con = sqlite3.connect('db/database.sqlite3', autocommit=False)
cur = con.cursor()

sample_doctor_data = [
    {
        "name": "Dr. Brian Hernandez",
        "age": 37,
        "gender": "Male",
        "contact_number": "07645364253",
    },
    {
        "name": "Dr. Samantha Kim",
        "age": 58,
        "gender": "Female",
        "contact_number": "07645364253",
    },
    {
        "name": "Dr. Jason Nguyen",
        "age": 45,
        "gender": "Male",
        "contact_number": "07645364253",
    },
    {
        "name": "Dr. Karen Thompson",
        "age": 61,
        "gender": "Female",
        "contact_number": "0764536425",
    },
    {
        "name": "Dr. Rachel Rodriguez",
        "age": 26,
        "gender": "Female",
        "contact_number": "07645364253",
    },
    {
        "name": "Dr. Christopher Brown",
        "age": 66,
        "gender": "Male",
        "contact_number": "07645364253",
    },
    {
        "name": "Dr. Jessica Davis",
        "age": 47,
        "gender": "Female",
        "contact_number": "07645364253",
    },
    {
        "name": "Dr. Kevin Lee",
        "age": 33,
        "gender": "Male",
        "contact_number": "07645364253",
    },
    {
        "name": "Dr. Jennifer Martinez",
        "age": 63,
        "gender": "Female",
        "contact_number": "07645364253",
    },
    {
        "name": "Dr. Michael Johnson",
        "age": 29,
        "gender": "Male",
        "contact_number": "07645364253",
    }
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