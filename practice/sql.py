import sqlite3

connection = sqlite3.connect("sounds_like_a_gym.db")
cursor = connection.cursor()
cursor.execute("""DROP TABLE Members;""")
cursor.execute("""DROP TABLE Organization;""")

sql_command = """
CREATE TABLE Members ( 
ID INTEGER PRIMARY KEY, 
FIRST_NAME VARCHAR(30), 
LAST_NAME VARCHAR(40),
STREET_ADDRESS VARCHAR(100), 
APARTMENT_NUMBER VARCHAR(20) DEFAULT NULL,
CITY VARCHAR(50),
STATE VARCHAR(25),
ZIPCODE VARCHAR(10),
PHONE_NUMBER VARCHAR(20),
AGE INT(10));"""

cursor.execute(sql_command)


sql_command = """
CREATE TABLE Organization ( 
ID INTEGER PRIMARY KEY, 
MEMBER_ID VARCHAR(20), 
LOCATION VARCHAR(30), 
DUES DECIMAL(19,4));"""

cursor.execute(sql_command)


members_data = [ ("William", "Shakespeare", "1000 Innovation Way", "Apt 400","Fake London", "Georgia","33009","123-456-789","105"),]
               
for member in members_data:
    members_format_str = """INSERT INTO members (ID, FIRST_NAME, LAST_NAME, STREET_ADDRESS, APARTMENT_NUMBER, CITY, STATE, ZIPCODE, PHONE_NUMBER, AGE)
    VALUES (NULL, "{first}", "{last}", "{street_address}", "{apartment_number}", "{city}", "{state}","{zipcode}","{phone_number}","{age}");"""

    sql_command = members_format_str.format(first=member[0], last=member[1], street_address=member[2], apartment_number = member[3], city = member[4],state = member[5],zipcode = member[6],phone_number = member[7],age=member[8])
    cursor.execute(sql_command)


cursor.execute("SELECT * FROM Members") 
print("fetchall:")
result = cursor.fetchall() 
for r in result:
    print(r)


cursor.execute("SELECT * FROM Members") 
print("\nfetch one:")
res = cursor.fetchone() 
print(res)

