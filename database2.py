'''
Created on Jan 10, 2017

@author: hanif
'''

import pymysql
import datetime

class Database:
        
	def connect(self):
		return pymysql.connect("localhost","root","","signup" )
    
	def insert(self,data):
		con = Database.connect(self)
		cursor = con.cursor()
		try:
			cursor.execute("INSERT INTO signup_info(name,username,email,password) VALUES(%s, %s, %s, %s)", (data['name'],data['username'],data['email'],data['password'],))
			con.commit()
			return True
		except:
			con.rollback()
			return False
		finally:
			con.close()
	def match(self,data):
                try:
                        con = Database.connect(self)
                        cursor = con.cursor()
                        sql1="select * from signup_info"
                        cursor.execute(sql1)
                        results=cursor.fetchall()
                        for row in results:
                                
                                name=row[0]
                                username=row[1]
                                email=row[2]
                                password=row[3]
                                print('hello')
                                if password == data['password'] and username == data['username'] or password == data['password'] and email == data['username']:
                                        return True
                                
                        return False
                                        
                         
                except Exception as e:
                        print(e)
                        print("hi")

