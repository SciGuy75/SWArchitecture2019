def queryDatabase(query):
    # Connect to the database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Save changes made and close the database
    conn.commit()
    conn.close()

    return