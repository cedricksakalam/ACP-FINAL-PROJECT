import sqlite3

def init_db():
    conn = sqlite3.connect("PeriodicGame.db")
    cursor = conn.cursor()

    #Create leaderboard table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leaderboard (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            score INTEGER NOT NULL
        )
    """)

    #Create feedback table (include age column)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            age INTEGER NOT NULL,  -- Add age column here
            feedback TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    #Create users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()
    
#Add a new user to the users table
def add_user(username, age):
    conn = sqlite3.connect("PeriodicGame.db")
    cursor = conn.cursor()

    # Insert user into the users table
    cursor.execute("INSERT INTO users (username, age) VALUES (?, ?)", (username, age))
    conn.commit()
    conn.close()

#Retrieve the leaderboard
def get_leaderboard():
    conn = sqlite3.connect("PeriodicGame.db")
    cursor = conn.cursor()
    # Select the appropriate fields in the right order
    cursor.execute("SELECT username, score FROM leaderboard ORDER BY score DESC LIMIT 20")
    rows = cursor.fetchall()
    conn.close()
    return rows

#Add or update a user's score in the leaderboard
def add_score(username, score):
    conn = sqlite3.connect("PeriodicGame.db")
    cursor = conn.cursor()

    #Check if the user already has a score
    cursor.execute("SELECT score FROM leaderboard WHERE username = ?", (username,))
    existing_score = cursor.fetchone()

    if existing_score:
        if score > existing_score[0]:  #Update only if the new score is higher
            cursor.execute("UPDATE leaderboard SET score = ? WHERE username = ?", (score, username))
    else:
        cursor.execute("INSERT INTO leaderboard (username, score) VALUES (?, ?)", (username, score))

    conn.commit()
    conn.close()

#Reset the leaderboard by clearing the leaderboard table
def reset_leaderboard_db():
    conn = sqlite3.connect("PeriodicGame.db")
    cursor = conn.cursor()

    #Delete all entries in the leaderboard table
    cursor.execute("DELETE FROM leaderboard")  # Fixed query

    conn.commit()
    conn.close()

#Add feedback to the feedback table
def add_feedback(username, age, feedback):
    conn = sqlite3.connect("PeriodicGame.db")
    cursor = conn.cursor()

    #Insert feedback into the database
    cursor.execute("INSERT INTO feedback (username, age, feedback) VALUES (?, ?, ?)", (username, age, feedback))
    conn.commit()
    conn.close()

#Retrieve all feedback from users
def get_feedback():
    conn = sqlite3.connect("PeriodicGame.db")
    cursor = conn.cursor()
    
    # Retrieve all feedback with age and timestamp
    cursor.execute("SELECT username, age, feedback, timestamp FROM feedback ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows
