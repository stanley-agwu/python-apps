import sqlite3

# Connect to database
conn=sqlite3.connect("y_customer.db")

# Create a cursor
c = conn.cursor()

# Create a Table
# c.execute("""CREATE TABLE customers (
# 		first_name text,
# 		last_name text,
# 		email text,
# 		age integer,
# 		city text
# 		)
# 		""")


# many_customers=[('Lionel', 'Messi', 'messi@barca.com', '33', 'Barcelona'),
# 				('Christiano', 'Ronaldo', 'CR7@juve.com', '35', 'Turin'),
# 				('Lebron', 'James', 'lebron@lakers.com', '36', 'Los Angeles'),
# 				('Serena', 'Williams', 'serena@houston.com', '34', 'Texas'),
# 				('Sadio', 'Manny', 'sadio@liverpool.com', '30', 'Liverpool')
# 				]
# c.executemany("INSERT INTO customers VALUES (?, ?, ?, ?, ?)", many_customers)

#print("Command executed successfully....")

#Query the database
c.execute("SELECT rowid, * FROM customers")
# c.execute("SELECT rowid, * FROM customers WHERE last_name='Winfrey'")

#Ordering the database
#c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")

#Update the database
# c.execute("""UPDATE customers SET first_name='CR7'
# 	WHERE last_name='Ronaldo'
# 	""")
# c.execute("""UPDATE customers SET email='lebron@la.com'
# 	WHERE rowid=6
#  	""")

# #Commit our command
# conn.commit()

#print(c.fetchone())
#print(c.fetchmany(3))
#print(c.fetchall())

items=c.fetchall()

print("S/N" + "\t" + "NAMES" + "\t\t\t" + "EMAIL" + "\t\t" + "AGE" + "\t" +"CITY")
for item in items:
	print(str(item[0]) + "\t" + item[1] + "\t" + item[2] 
		+ "\t" + item[3] + "\t\t" + str(item[4]) + "\t" + item[5])

# #Commit our command
conn.commit()

# Close our connection
c.close()


# Query the database
# c.execute("SELECT rowid, * FROM customers")
# items=c.fetchall()

# for item in items:
# 	print(item)

	


#Datatypes in sqlite3 
#1. Null
#2. integer
#3. Real(Float)
#4. text
#5. Blob(Images, music files--mp3, mp4)

