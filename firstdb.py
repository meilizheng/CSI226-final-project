# # Importing the MySQL Connector module
import mysql.connector
# Establishing a connection to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Wellschiro1!",
    database="testdb"
)

# Creating a cursor object to interact with the MySQL database
mycursor = mydb.cursor()


# Creating a new database named 'firstdb'
mycursor.execute("CREATE DATABASE firstdb")



# Showing all databases
mycursor.execute("SHOW DATABASES")
for testdb in mycursor:
    print(testdb)

# Creating a new table named 'students' with columns: name, enrolledcourse, and grade
mycursor.execute("CREATE TABLE students (name VARCHAR(255), enrolledcourse VARCHAR(255), grade INTEGER(10))")


# Showing all tables in the current database
mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print (tb)


# Defining an SQL formula for inserting data into the 'students' table
sqlFormula = "INSERT INTO students (name, enrolledcourse, grade) VALUES (%s, %s, %s)"

# Data to be inserted
students = [("John Doe", "Mathematics", 85),
            ("Jane Smith", "History", 92),
            ("Bob Johnson", "Computer Science", 78),
            ("Alice Williams", "Physics", 88),
            ("Charlie Brown", "English", 95),
            ("Emma Davis", "Chemistry", 79),
            ("Michael Miller", "Biology", 91),
            ("Olivia Taylor", "Economics", 87),
            ("David Wilson", "Psychology", 84),
            ("Sophia White", "Geography", 89),]
# Executing the SQL formula to insert data into the 'students' table
mycursor.executemany(sqlFormula, students)
# Committing the changes to the database
mydb.commit()



# Retrieving and printing all records from the 'students' table
mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)


# Retrieving and printing only the 'name' column from the 'students' table
mycursor.execute("SELECT name FROM students")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)


# Retrieving and printing only the 'enrolledcourse' column from the 'students' table
mycursor.execute("SELECT enrolledcourse FROM students")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)


# Retrieving and printing only the first row of the 'enrolledcourse' column from the 'students' table
mycursor.execute("SELECT enrolledcourse FROM students")
myresult = mycursor.fetchone()
for row in myresult:
    print(row)


# Executing a SELECT query with a WHERE clause to retrieve records where 'grade' is 88
sql = "SELECT * FROM students WHERE grade = 88"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for result in myresult:
    print(result)


# Executing a SELECT query with a WHERE clause using the LIKE operator to retrieve records with 'vi' in the 'name'
sql = "SELECT * FROM students WHERE name LIKE '%vi%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for result in myresult:
    print(result)



# Executing a SELECT query with a WHERE clause and parameterized values to retrieve records for a specific 'name'
sql = "SELECT * FROM students WHERE name = %s"
mycursor.execute(sql, ("Emma Davis",))
myresult = mycursor.fetchall()
for result in myresult:
    print(result)



# Executing an UPDATE query to set the 'grade' to 80 where 'name' is 'Emma Davis'
sql = "UPDATE students SET grade = 80 WHERE name = 'Emma Davis'"
mycursor.execute(sql)
mydb.commit()


# Executing a SELECT query with a LIMIT clause to retrieve the first 5 records from the 'students' table
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM students LIMIT 5")
myresult = mycursor.fetchall()
for result in myresult:
    print(result)


# Executing a SELECT query with a LIMIT and OFFSET clause to retrieve 5 records starting from the third record
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM students LIMIT 5 OFFSET 2")
myresult = mycursor.fetchall()
for result in myresult:
    print(result)



# Executing a SELECT query with an ORDER BY clause to retrieve all records ordered by 'name' in ascending order
sql = "SELECT * FROM students ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for r in myresult:
    print(r)


# Executing a SELECT query with an ORDER BY clause to retrieve all records ordered by 'grade' in ascending order
sql = "SELECT * FROM students ORDER BY grade"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for r in myresult:
    print(r)


# Executing a SELECT query with an ORDER BY clause to retrieve all records ordered by 'grade' in descending order
sql = "SELECT * FROM students ORDER BY grade DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for r in myresult:
    print(r)


# Executing a SELECT query with an ORDER BY clause to retrieve all records ordered by 'name' in descending order
sql = "SELECT * FROM students ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for r in myresult:
    print(r)


# Executing a DELETE query to delete the record where 'name' is 'Sophia White'
sql = "DELETE FROM students WHERE name = 'Sophia White'"
mycursor.execute(sql)
mydb.commit()


# Executing a DROP TABLE query to delete the 'students' table
sql = "DROP TABLE IF EXISTS students"
mycursor.execute(sql)
mydb.commit()


