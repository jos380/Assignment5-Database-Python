# Program Name: Assignment5.py
# Course: IT3883/Section XXX
# Student Name: 
# Assignment Number: Lab 5
# Due Date: XX/XX/2026
# Purpose:
# This program reads temperature data from a file, stores it in a SQLite database,
# and calculates the average temperature for Sunday and Thursday.
# Resources:
# - Python sqlite3 documentation

import sqlite3

def main():
    # Connect to database
    conn = sqlite3.connect("temperature_data.db")
    cursor = conn.cursor()

    # Create table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS temperatures (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Day_Of_Week TEXT,
        Temperature_Value REAL
    )
    """)

    # Clear existing data to avoid duplicates on re-run
    cursor.execute("DELETE FROM temperatures")

    file_name = "Assignment5input.txt"

    # Read file and insert data
    with open(file_name, "r") as file:
        for line in file:
            data = line.strip().split()

            if len(data) == 2:
                day = data[0]
                try:
                    temp_value = float(data[1])
                except ValueError:
                    continue

                cursor.execute("""
                INSERT INTO temperatures (Day_Of_Week, Temperature_Value)
                VALUES (?, ?)
                """, (day, temp_value))

    conn.commit()

    # Query averages
    cursor.execute("""
    SELECT AVG(Temperature_Value)
    FROM temperatures
    WHERE Day_Of_Week = 'Sunday'
    """)
    sunday_avg = cursor.fetchone()[0]

    cursor.execute("""
    SELECT AVG(Temperature_Value)
    FROM temperatures
    WHERE Day_Of_Week = 'Thursday'
    """)
    thursday_avg = cursor.fetchone()[0]

    # Output
    print("Average Temperature for Sunday:", sunday_avg)
    print("Average Temperature for Thursday:", thursday_avg)

    conn.close()

if __name__ == "__main__":
    main()
