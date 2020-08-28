import database2

#Add a record
#database2.add_one("Novak", "Djokovi", "novak@tennis.sr", 29, "Serbia")

#Delete record using rowid
#database2.delete_one('9')

#Add many records
# stuff=[
# 	('Kelvin', 'Debryne', 'kelvin@uk.com', 26, 'Belgium'),
# 	('David', 'Silva', 'david@sp.uk', 37, 'Malaga'),
#  	('Serge', 'Gnabry', 'Serge@mls.com', 23, 'Bayern Munich'),
	
#  ]


#database2.add_many(stuff)


#Search records in database table using email
#database2.email_lookup("kelvin@uk.com")

#Display full database table
database2.show_all()

