# -*- coding: utf-8 -*-
from django.db import models
import xlrd
from datetime import date
import re
import datetime
import time

# Create your models here.
class Book_info(models.Model):
	bookname = models.CharField(max_length = 100)
	bookwriter = models.CharField(max_length = 100)
	bookyear = models.DateField(default = date.today)
	bookpress = models.CharField(max_length = 100)
	classification = models.CharField(max_length = 100)
	bookcover = models.CharField(max_length = 100)
	usernumber = models.IntegerField()
	onepoint = models.IntegerField()
	twopoint = models.IntegerField()
	threepoint = models.IntegerField()
	fourpoint = models.IntegerField()
	fivepoint = models.IntegerField()
	point = models.IntegerField()
	def importdata():
		workbook = xlrd.open_workbook(r'C:\Users\lenovo\Desktop\经管.xlsx')
		try:
			mysheet = workbook.sheets()[0]
		except:
			print("no sheet in sheets named PC")
			return
		#total rows and cols
		print("%d rows, %d cols"%(mysheet.nrows, mysheet.ncols))
		for row in range(1,mysheet.nrows):
			mname = str(mysheet.cell(row,0))[6:len(str(mysheet.cell(row,0))) - 1]
			mwriter = str(mysheet.cell(row,2))[6:len(str(mysheet.cell(row,2))) - 1]
			myear = xlrd.xldate.xldate_as_datetime(mysheet.cell(row,4).value, 0)
			mpress = str(mysheet.cell(row,3))[6:len(str(mysheet.cell(row,3))) - 1]
			mcover = str(mysheet.cell(row,1))[6:len(str(mysheet.cell(row,1))) - 1]
			mclassification = "经管" + str(mysheet.cell(row,5))[6:len(str(mysheet.cell(row,5))) - 1]
			musernumber = 0
			monepoint = 0
			mtwopoint = 0
			mthreepoint = 0
			mfourpoint = 0
			mfivepoint = 0
			mpoint = 0
			a = Book_info(bookname = mname,bookwriter = mwriter,bookyear = myear,bookpress = mpress,classification = mclassification,bookcover = mcover,usernumber = musernumber,onepoint = monepoint,twopoint = mtwopoint,threepoint = mthreepoint,fourpoint = mfourpoint,fivepoint = mfivepoint,point = mpoint)
			a.save()
		workbook = xlrd.open_workbook(r'C:\Users\lenovo\Desktop\科技.xlsx')
		try:
			mysheet = workbook.sheets()[0]
		except:
			print("no sheet in sheets named PC")
			return
		#total rows and cols
		print("%d rows, %d cols"%(mysheet.nrows, mysheet.ncols))
		for row in range(1,mysheet.nrows):
			mname = str(mysheet.cell(row,0))[6:len(str(mysheet.cell(row,0))) - 1]
			mwriter = str(mysheet.cell(row,2))[6:len(str(mysheet.cell(row,2))) - 1]
			myear = xlrd.xldate.xldate_as_datetime(mysheet.cell(row,4).value, 0)
			mpress = str(mysheet.cell(row,3))[6:len(str(mysheet.cell(row,3))) - 1]
			mcover = str(mysheet.cell(row,1))[6:len(str(mysheet.cell(row,1))) - 1]
			mclassification = "科技" + str(mysheet.cell(row,5))[6:len(str(mysheet.cell(row,5))) - 1]
			musernumber = 0
			monepoint = 0
			mtwopoint = 0
			mthreepoint = 0
			mfourpoint = 0
			mfivepoint = 0
			mpoint = 0
			a = Book_info(bookname = mname,bookwriter = mwriter,bookyear = myear,bookpress = mpress,classification = mclassification,bookcover = mcover,usernumber = musernumber,onepoint = monepoint,twopoint = mtwopoint,threepoint = mthreepoint,fourpoint = mfourpoint,fivepoint = mfivepoint,point = mpoint)
			a.save()
		workbook = xlrd.open_workbook(r'C:\Users\lenovo\Desktop\流行.xlsx')
		try:
			mysheet = workbook.sheets()[0]
		except:
			print("no sheet in sheets named PC")
			return
		#total rows and cols
		print("%d rows, %d cols"%(mysheet.nrows, mysheet.ncols))
		for row in range(1,mysheet.nrows):
			mname = str(mysheet.cell(row,0))[6:len(str(mysheet.cell(row,0))) - 1]
			mwriter = str(mysheet.cell(row,2))[6:len(str(mysheet.cell(row,2))) - 1]
			myear = xlrd.xldate.xldate_as_datetime(mysheet.cell(row,4).value, 0)
			mpress = str(mysheet.cell(row,3))[6:len(str(mysheet.cell(row,3))) - 1]
			mcover = str(mysheet.cell(row,1))[6:len(str(mysheet.cell(row,1))) - 1]
			mclassification = "流行" + str(mysheet.cell(row,5))[6:len(str(mysheet.cell(row,5))) - 1]
			musernumber = 0
			monepoint = 0
			mtwopoint = 0
			mthreepoint = 0
			mfourpoint = 0
			mfivepoint = 0
			mpoint = 0
			a = Book_info(bookname = mname,bookwriter = mwriter,bookyear = myear,bookpress = mpress,classification = mclassification,bookcover = mcover,usernumber = musernumber,onepoint = monepoint,twopoint = mtwopoint,threepoint = mthreepoint,fourpoint = mfourpoint,fivepoint = mfivepoint,point = mpoint)
			a.save()
		workbook = xlrd.open_workbook(r'C:\Users\lenovo\Desktop\文学.xlsx')
		try:
			mysheet = workbook.sheets()[0]
		except:
			print("no sheet in sheets named PC")
			return
		#total rows and cols
		print("%d rows, %d cols"%(mysheet.nrows, mysheet.ncols))
		for row in range(1,mysheet.nrows):
			mname = str(mysheet.cell(row,0))[6:len(str(mysheet.cell(row,0))) - 1]
			mwriter = str(mysheet.cell(row,2))[6:len(str(mysheet.cell(row,2))) - 1]
			myear = xlrd.xldate.xldate_as_datetime(mysheet.cell(row,4).value, 0)
			mpress = str(mysheet.cell(row,3))[6:len(str(mysheet.cell(row,3))) - 1]
			mcover = str(mysheet.cell(row,1))[6:len(str(mysheet.cell(row,1))) - 1]
			mclassification = "文学" + str(mysheet.cell(row,5))[6:len(str(mysheet.cell(row,5))) - 1]
			musernumber = 0
			monepoint = 0
			mtwopoint = 0
			mthreepoint = 0
			mfourpoint = 0
			mfivepoint = 0
			mpoint = 0
			a = Book_info(bookname = mname,bookwriter = mwriter,bookyear = myear,bookpress = mpress,classification = mclassification,bookcover = mcover,usernumber = musernumber,onepoint = monepoint,twopoint = mtwopoint,threepoint = mthreepoint,fourpoint = mfourpoint,fivepoint = mfivepoint,point = mpoint)
			a.save()
		workbook = xlrd.open_workbook(r'C:\Users\lenovo\Desktop\生活.xlsx')
		try:
			mysheet = workbook.sheets()[0]
		except:
			print("no sheet in sheets named PC")
			return
		#total rows and cols
		print("%d rows, %d cols"%(mysheet.nrows, mysheet.ncols))
		for row in range(1,mysheet.nrows):
			mname = str(mysheet.cell(row,0))[6:len(str(mysheet.cell(row,0))) - 1]
			mwriter = str(mysheet.cell(row,2))[6:len(str(mysheet.cell(row,2))) - 1]
			myear = xlrd.xldate.xldate_as_datetime(mysheet.cell(row,4).value, 0)
			mpress = str(mysheet.cell(row,3))[6:len(str(mysheet.cell(row,3))) - 1]
			mcover = str(mysheet.cell(row,1))[6:len(str(mysheet.cell(row,1))) - 1]
			mclassification = "生活" + str(mysheet.cell(row,5))[6:len(str(mysheet.cell(row,5))) - 1]
			musernumber = 0
			monepoint = 0
			mtwopoint = 0
			mthreepoint = 0
			mfourpoint = 0
			mfivepoint = 0
			mpoint = 0
			a = Book_info(bookname = mname,bookwriter = mwriter,bookyear = myear,bookpress = mpress,classification = mclassification,bookcover = mcover,usernumber = musernumber,onepoint = monepoint,twopoint = mtwopoint,threepoint = mthreepoint,fourpoint = mfourpoint,fivepoint = mfivepoint,point = mpoint)
			a.save()
		workbook = xlrd.open_workbook(r'C:\Users\lenovo\Desktop\文化.xlsx')
		try:
			mysheet = workbook.sheets()[0]
		except:
			print("no sheet in sheets named PC")
			return
		#total rows and cols
		print("%d rows, %d cols"%(mysheet.nrows, mysheet.ncols))
		for row in range(1,mysheet.nrows):
			mname = str(mysheet.cell(row,0))[6:len(str(mysheet.cell(row,0))) - 1]
			mwriter = str(mysheet.cell(row,2))[6:len(str(mysheet.cell(row,2))) - 1]
			myear = xlrd.xldate.xldate_as_datetime(mysheet.cell(row,4).value, 0)
			mpress = str(mysheet.cell(row,3))[6:len(str(mysheet.cell(row,3))) - 1]
			mcover = str(mysheet.cell(row,1))[6:len(str(mysheet.cell(row,1))) - 1]
			mclassification = "文化" + str(mysheet.cell(row,5))[6:len(str(mysheet.cell(row,5))) - 1]
			musernumber = 0
			monepoint = 0
			mtwopoint = 0
			mthreepoint = 0
			mfourpoint = 0
			mfivepoint = 0
			mpoint = 0
			a = Book_info(bookname = mname,bookwriter = mwriter,bookyear = myear,bookpress = mpress,classification = mclassification,bookcover = mcover,usernumber = musernumber,onepoint = monepoint,twopoint = mtwopoint,threepoint = mthreepoint,fourpoint = mfourpoint,fivepoint = mfivepoint,point = mpoint)
			a.save()
	def GetbooksbyClassification(class_name):
		results = []
		pattern = '.*'.join(class_name) # Converts 'djm' to 'd.*j.*m'
		regex = re.compile(pattern) # Compiles a regex.
		for i in Book_info.objects.all():
			match = regex.search(i.classification)
			if match:
				results.append(i)
		return results
	def GetbooksbyDate(year_name):
		results = []
		for i in Book_info.objects.all():
			if year_name == i.bookyear.strftime('%Y%m%d'):
				results.append(i)
		return results
	def GetbooksbyNewDate():
		results = []
		tempc = Book_info.objects.order_by("-bookyear")
		for i in range(10):
			results.append(tempc[i])
		return results
	def GetbooksbyPoint():
		results = []
		tempc = Book_info.objects.order_by("point")
		for i in range(10):
			results.append(tempc[i])
		return results
	def GetbookbyId(id_name):
		return Book_info.objects.get(id = id_name)
	def Sortbypoint(objects_name):
		listLength = len(objects_name)
		while listLength > 0:
			for i in range(listLength - 1):
				if objects_name[i].point < objects_name[i + 1].point:
					objects_name[i].point = objects_name[i].point + objects_name[i + 1].point
					objects_name[i + 1].point = objects_name[i].point - objects_name[i + 1].point
					objects_name[i].point = objects_name[i].point - objects_name[i + 1].point
			listLength -= 1
		return objects_name
	def GetbooksbyBookname(book_name):
		results = []
		pattern = '.*'.join(book_name) # Converts 'djm' to 'd.*j.*m'
		regex = re.compile(pattern) # Compiles a regex.
		for i in Book_info.objects.all():
			match = regex.search(i.bookname)
			if match:
				results.append(i)
		return results
	def GetbooksbyWriter(writer_name):
		results = []
		pattern = '.*'.join(writer_name) # Converts 'djm' to 'd.*j.*m'
		regex = re.compile(pattern) # Compiles a regex.
		for i in Book_info.objects.all():
			match = regex.search(i.bookwriter)
			if match:
				results.append(i)
		return results
		

class User_Book_Info(models.Model):
	userid = models.IntegerField()
	bookid = models.IntegerField()
	status = models.IntegerField()
	point = models.DateField(default = date.today)
	
class User_Relationship(models.Model):
	user1_id = models.IntegerField()
	user2_id = models.IntegerField()
	
class Message_Record(models.Model):
	user1_id = models.IntegerField()
	user2_id = models.IntegerField()
	message = models.CharField(max_length = 100)
	date = models.DateField(default = date.today)
	
class Book_Review(models.Model):
	bookid = models.IntegerField()
	userid = models.IntegerField()
	comment = models.CharField(max_length = 100)
	time = models.DateField(default = date.today)

class Personal_info(models.Model):
	username = models.CharField(max_length = 100)
	password = models.CharField(max_length = 100)
	nickname = models.CharField(max_length = 100)
	gender = models.IntegerField()
	photo = models.CharField(max_length = 100)
	region = models.CharField(max_length = 100)
	introduce = models.CharField(max_length = 100)
	def MAddUser(musername,muserpassword):
		a = Personal_info(username = musername,password = muserpassword,nickname = "",gender = 0,photo = "",region = "",introduce = "")
		a.save()
	#0登陆失败,1登陆成功
	def VerifyLogin(musername,muserpassword):
		b = Personal_info.objects.filter(username = musername)
		if len(b) != 0:
			if b[0].password == muserpassword:
				return 1
			else:
				return 0
		else:
			return 0
		
			
		
		
