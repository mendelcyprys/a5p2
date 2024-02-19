def initialise(cur):

    # initialise table patients
    cur.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            patient_id INTEGER PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            contact_number TEXT NOT NULL
        )
    """)

    # initialise table doctors
    cur.execute("""
        CREATE TABLE IF NOT EXISTS doctors (
            doctor_id INTEGER PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            contact_number TEXT NOT NULL
        )
    """)

    # initialise table appointments
    cur.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            appointment_id INTEGER PRIMARY KEY NOT NULL,
            description TEXT NOT NULL,
            date TEXT NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT NOT NULL,
            doctor_id INTEGER NOT NULL,
            patient_id INTEGER NOT NULL
        )
    """)