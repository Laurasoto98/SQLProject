import cx_Oracle
import pandas as pd

"""
Some quick start guides:
* cx_Oracle 8: https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html
* pandas: https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html
"""
# TODO change path of Oracle Instant Client to yours
cx_Oracle.init_oracle_client(lib_dir = "./instantclient_19_8")

# TODO change credentials
# Connect as user "user" with password "mypass" to the "CSC423" service
# running on lawtech.law.miami.edu
connection = cx_Oracle.connect("lasocsc423", "c03719", "lawtech.law.miami.edu/CSC_423")
cursor = connection.cursor()
cursor.execute("""
    SELECT name, COUNT(*) AS num_Of_Offered_Sessions
    FROM course c, course_offering m
    WHERE c.courseID = m.courseID 
    GROUP BY c.courseID, name
    """)

print("\n1. Count the number of offered session for each course\n\n")
# get column names from cursor
columns = [c[0] for c in cursor.description]
# fetch data
data = cursor.fetchall()
# bring data into a pandas dataframe for easy data transformation
df = pd.DataFrame(data, columns = columns)
print(df) # examine
print(df.columns)
# print(df['FIRST_NAME']) # example to extract a column

cursor = connection.cursor()
cursor.execute("""
    SELECT a.firstName, a.LastName, EXTRACT(MONTH FROM a.registrationDate) AS registrationMonth, l.name, c.startMonth 
    FROM student a, course_offering c, course l
    WHERE a.courseOfferingID = c.courseOfferingID AND c.courseID = l.courseID AND EXTRACT(MONTH FROM registrationDate) >= startMonth
    """)

print("\n2. Return the name, the course, the start month and the registration date of the student that did not register on time for the class \n\n")
# get column names from cursor
columns = [c[0] for c in cursor.description]
# fetch data
data = cursor.fetchall()
# bring data into a pandas dataframe for easy data transformation
df = pd.DataFrame(data, columns = columns)
print(df) # examine
print(df.columns)
# print(df['FIRST_NAME']) # example to extract a column

cursor.execute("""
    SELECT name AS courseName, firstName, LastName
    FROM course_offering c, course a, tutor t
    WHERE c.courseID = a.courseID AND c.tutorID = t.tutorID AND optFieldWeek = 1
    """)

print("\n3. List all the course name and tutor name of the offered courses that have an optional field trip  \n\n")
# get column names from cursor
columns = [c[0] for c in cursor.description]
# fetch data
data = cursor.fetchall()
# bring data into a pandas dataframe for easy data transformation
df = pd.DataFrame(data, columns = columns)
print(df) # examine
print(df.columns)
# print(df['FIRST_NAME']) # example to extract a column

cursor.execute("""
    SELECT name, firstName, lastName
    FROM course c, student s, course_offering l
    WHERE s.courseOfferingID = l.courseOfferingID AND c.courseID = l.courseID AND name LIKE 'Italian%'
    """)

print("\n4. List all the students registered in an italian course\n\n")
# get column names from cursor
columns = [c[0] for c in cursor.description]
# fetch data
data = cursor.fetchall()
# bring data into a pandas dataframe for easy data transformation
df = pd.DataFrame(data, columns = columns)
print(df) # examine
print(df.columns)
# print(df['FIRST_NAME']) # example to extract a column

cursor.execute("""
    SELECT name, firstName, lastName, maxnumofstudents, startMonth, endMonth
    FROM course c, course_offering l, tutor t
    WHERE  c.courseID = l.courseID AND l.tutorID = t.tutorID AND startMonth < 6   
    """)

print("\n5. List all courses offered in the spring semester, therefore that the start month is before May. Display the course name, the instructure name, the maximum number of students, the start and the end month\n\n")
# get column names from cursor
columns = [c[0] for c in cursor.description]
# fetch data
data = cursor.fetchall()
# bring data into a pandas dataframe for easy data transformation
df = pd.DataFrame(data, columns = columns)
print(df) # examine
print(df.columns)
# print(df['FIRST_NAME']) # example to extract a column