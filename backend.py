import sqlite3
import random
import smtplib
from email.mime.text import MIMEText

class words_dic:

	def __init__(self,db):
		global conn,cur
		conn = sqlite3.connect(db)
		cur = conn.cursor()
		cur.execute("CREATE TABLE IF NOT EXISTS dicch (id INTEGER PRIMARY KEY, word text, defination text, example text)")
		conn.commit()
	

	def insert(self,word,defination,example):
		cur.execute("INSERT INTO dicch VALUES (NULL,?,?,?)",(word,defination,example))
		conn.commit()


	def view(self):
		cur.execute("SELECT * FROM dicch")
		rows = cur.fetchall()

		return rows

	def delete(self,n):
		cur.execute("DELETE FROM dicch WHERE id =?",(n,))
		conn.commit()


	def search(self,word):
		cur.execute("SELECT * FROM dicch WHERE word = ? or word LIKE  ?",(word,'%'+word+'%'))
		rows = cur.fetchall()
		return rows

	def update(self,n,word,defination,example):
		cur.execute("UPDATE dicch SET word=?,defination=?,example=? WHERE id=?",(word,defination,example,n))
		conn.commit()

	def random_word(self):
		cur.execute("SELECT * FROM dicch")
		rows = cur.fetchall()
		# num_words = len(rows)
		chosen_word = random.choice(rows)
		word = chosen_word[1]
		cur.execute("SELECT * FROM dicch WHERE word = ? ",(word,))
		random_row = cur.fetchall()
		# word = random_row[0][1]
		# dif = random_row[0][2]
		# exa = random_row[0][3]
		# set email content
		# message = 'Hello Mr. Abdullah \n\nI hope you are doing great, and let\'s take a look at today word.\n\n Word:%s\nDifension:%s\nExample:%s'%(word,dif,exa)
		# msg=MIMEText(message, 'html')
		# msg['Subject']='Today WORD'
		# msg['To']='abdullah.alashafi@gmail.com'
		# msg['From']="wwr2012@gmail.com"
		# gmail.send_message(msg)
		# set email connection
		##### ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ######## 
		#THE above code is working good, i just want to use that in down here
		#because the speaces. thanks
		# try:
		# 	gmail = smtplib.SMTP('smtp.gmail.com', 587)
		# 	# self.gmail = gmail
		# 	gmail.ehlo()
		# 	gmail.starttls()
		# 	gmail.login('wwr2012@gmail.com','Iwanther1back2me')
		# 	gmail.sendmail('wwr2012@gmail.com','abdullah.alashafi@gmail.com','Subject:Today WORD .... \n\nHello Mr. Abdullah \n\nI hope you are doing great, and let\'s take a look at today word.\n\n Word:%s\nDifension:%s\nExample:%s'%(word,dif,exa))
		# 	gmail.quit()
		# 	message = 'Email has been send successfully'
		# except:
		# 	message = 'There is a problem with send the email.'
		
		return random_row




	def __del__(self):
		conn.close()
		

# word = words_dic('abdullah.db')

# print (word.random_word())

#create_database('abdullah.db')
#insert(1,'permit','allow','My mother didn\'t permit me to play out the house')
#delete(1)
#print (search('colony')[0][3])
#update(2,'Resign','giave up or leave the work','I resigned my old company and going to apply to better job')
#print (view())
# def d():
# 	for i in range(6,-1,-1):
# 		print(i) 



# import turtle  
# skk = turtle.Turtle() 
  
# for i in range(4): 
#     skk.forward(50) 
#     skk.right(90) 
      
# turtle.done() 