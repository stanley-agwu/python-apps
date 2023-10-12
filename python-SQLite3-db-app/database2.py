import sqlite3

#Query the database and return all records
def show_all():
	# Connect to database
	conn=sqlite3.connect("y_customer.db")

	# Create a cursor
	c = conn.cursor()

	#Query the database
	c.execute("SELECT rowid, * FROM customers")
	items=c.fetchall()

	print("S/N" + "\t" + "NAMES" + "\t\t" + "EMAIL" + "\t\t\t" + "AGE" + "\t" +"CITY")
	for item in items:
		print(str(item[0]) + "\t" + item[1] + "\t" + item[2] 
		+ "\t" + item[3] + "\t\t" + str(item[4]) + "\t" + item[5])

	#Commit our command
	conn.commit()

	# Close our connection
	conn.close()

#Add a new record to our database table
def add_one(first_name, last_name, email, age, city):
	# Connect to database
	conn=sqlite3.connect("y_customer.db")

	# Create a cursor
	c = conn.cursor()

	#Add a record
	c.execute("INSERT INTO customers VALUES (?, ?, ?, ?, ?)", (first_name, last_name, email, age, city))

	#Commit our command
	conn.commit()

	# Close our connection
	conn.close()

#Delete record from our database table
def delete_one(id):
	# Connect to database
	conn=sqlite3.connect("y_customer.db")

	# Create a cursor
	c = conn.cursor()

	#Add a record
	c.execute("DELETE FROM customers WHERE rowid=(?)", id)

	#Commit our command
	conn.commit()

	# Close our connection
	conn.close()

#Add many records to database
def add_many(list):
	# Connect to database
	conn=sqlite3.connect("y_customer.db")

	# Create a cursor
	c = conn.cursor()

	#Add a record
	c.executemany("INSERT INTO customers VALUES (?, ?, ?, ?, ?)", (list))

	#Commit our command
	conn.commit()

	# Close our connection
	conn.close()

#Look up with Where
def email_lookup(email):
	# Connect to database
	conn=sqlite3.connect("y_customer.db")

	# Create a cursor
	c = conn.cursor()

	#Add a record
	c.execute("SELECT rowid, * from customers WHERE email=(?)", (email,))

	items=c.fetchall()

	print("S/N" + "\t" + "NAMES" + "\t\t" + "EMAIL" + "\t\t\t" + "AGE" + "\t" +"CITY")
	for item in items:
		print(str(item[0]) + "\t" + item[1] + "\t" + item[2] 
		+ "\t" + item[3] + "\t\t" + str(item[4]) + "\t" + item[5])
	
	#Commit our command
	#conn.commit()

	# Close our connection
	conn.close()















#Datatypes in sqlite3 
#1. Null
#2. integer
#3. Real(Float)
#4. text
#5. Blob(Images, music files--mp3, mp4)




