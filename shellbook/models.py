# -*- coding: utf-8 -*-
from django.db import models
import xlrd
from datetime import date
import re
import datetime
import time
from operator import itemgetter, attrgetter

# Create your models here.
class Book_info(models.Model):
	bookname = models.CharField(max_length = 100)
	bookwriter = models.CharField(max_length = 100)
	bookyear = models.CharField(max_length = 100)
	bookpress = models.CharField(max_length = 100)
	classification = models.CharField(max_length = 100)
	bookcover = models.CharField(max_length = 150)
	usernumber = models.IntegerField()
	onepoint = models.IntegerField()
	twopoint = models.IntegerField()
	threepoint = models.IntegerField()
	fourpoint = models.IntegerField()
	fivepoint = models.IntegerField()
	point = models.FloatField()
	booknumber = models.CharField(max_length = 100)
	writerintroduce = models.CharField(max_length = 1000)
	bookintroduce = models.CharField(max_length = 2000)
	bookprice = models.CharField(max_length = 100)
	bookbinding = models.CharField(max_length = 100)
	booktranslater = models.CharField(max_length = 100)
	def importdata():
		workbook = xlrd.open_workbook(r'C:\Users\lenovo\Desktop\data.xlsx')
		try:
			mysheet = workbook.sheets()[0]
		except:
			print("no sheet in sheets named PC")
			return
		#total rows and cols
		print("%d rows, %d cols"%(mysheet.nrows, mysheet.ncols))
		for row in range(0,mysheet.nrows):
			mname = str(mysheet.cell(row,0))[6:len(str(mysheet.cell(row,0))) - 3]
			mwriter = str(mysheet.cell(row,3))[6:len(str(mysheet.cell(row,3))) - 3]
			myear = str(mysheet.cell(row,6))[6:len(str(mysheet.cell(row,6))) - 3]
			mpress = str(mysheet.cell(row,4))[6:len(str(mysheet.cell(row,4))) - 3]
			mcover = str(mysheet.cell(row,1))[6:len(str(mysheet.cell(row,1))) - 3]
			mclassification = str(mysheet.cell(row,11))[6:len(str(mysheet.cell(row,11))) - 3]
			musernumber = 0
			monepoint = 0
			mtwopoint = 0
			mthreepoint = 0
			mfourpoint = 0
			mfivepoint = 0
			mpoint = 0
			mbooknumber = str(mysheet.cell(row,10))[6:len(str(mysheet.cell(row,10))) - 3]
			mwriterintroduce = str(mysheet.cell(row,12))[8:len(str(mysheet.cell(row,12))) - 1]
			mbookintroduce = str(mysheet.cell(row,13))[8:len(str(mysheet.cell(row,13))) - 1]
			mbookprice = str(mysheet.cell(row,8))[6:len(str(mysheet.cell(row,8))) - 3]
			mbookbinding = str(mysheet.cell(row,9))[6:len(str(mysheet.cell(row,9))) - 3]
			mbooktranslater = str(mysheet.cell(row,5))[6:len(str(mysheet.cell(row,5))) - 3]
			a = Book_info(bookname = mname,bookwriter = mwriter,bookyear = myear,bookpress = mpress,classification = mclassification,bookcover = mcover,usernumber = musernumber,onepoint = monepoint,twopoint = mtwopoint,threepoint = mthreepoint,fourpoint = mfourpoint,fivepoint = mfivepoint,point = mpoint,
			booknumber = mbooknumber,writerintroduce = mwriterintroduce,bookintroduce = mbookintroduce,bookprice = mbookprice,bookbinding = mbookbinding,booktranslater = mbooktranslater)
			a.save()
		workbook = xlrd.open_workbook(r'C:\Users\lenovo\Desktop\编程.xlsx')
		try:
			mysheet = workbook.sheets()[0]
		except:
			print("no sheet in sheets named PC")
			return
		#total rows and cols
		print("%d rows, %d cols"%(mysheet.nrows, mysheet.ncols))
		for row in range(0,mysheet.nrows):
			mname = str(mysheet.cell(row,0))[6:len(str(mysheet.cell(row,0))) - 3]
			mwriter = str(mysheet.cell(row,3))[6:len(str(mysheet.cell(row,3))) - 3]
			myear = str(mysheet.cell(row,6))[6:len(str(mysheet.cell(row,6))) - 3]
			mpress = str(mysheet.cell(row,4))[6:len(str(mysheet.cell(row,4))) - 3]
			mcover = str(mysheet.cell(row,1))[6:len(str(mysheet.cell(row,1))) - 3]
			mclassification = str(mysheet.cell(row,11))[6:len(str(mysheet.cell(row,11))) - 3]
			musernumber = 0
			monepoint = 0
			mtwopoint = 0
			mthreepoint = 0
			mfourpoint = 0
			mfivepoint = 0
			mpoint = 0
			mbooknumber = str(mysheet.cell(row,10))[6:len(str(mysheet.cell(row,10))) - 3]
			mwriterintroduce = str(mysheet.cell(row,12))[8:len(str(mysheet.cell(row,12))) - 1]
			mbookintroduce = str(mysheet.cell(row,13))[8:len(str(mysheet.cell(row,13))) - 1]
			mbookprice = str(mysheet.cell(row,8))[6:len(str(mysheet.cell(row,8))) - 3]
			mbookbinding = str(mysheet.cell(row,9))[6:len(str(mysheet.cell(row,9))) - 3]
			mbooktranslater = str(mysheet.cell(row,5))[6:len(str(mysheet.cell(row,5))) - 3]
			a = Book_info(bookname = mname,bookwriter = mwriter,bookyear = myear,bookpress = mpress,classification = mclassification,bookcover = mcover,usernumber = musernumber,onepoint = monepoint,twopoint = mtwopoint,threepoint = mthreepoint,fourpoint = mfourpoint,fivepoint = mfivepoint,point = mpoint,
			booknumber = mbooknumber,writerintroduce = mwriterintroduce,bookintroduce = mbookintroduce,bookprice = mbookprice,bookbinding = mbookbinding,booktranslater = mbooktranslater)
			a.save()
		workbook = xlrd.open_workbook(r'C:\Users\lenovo\Desktop\绘本.xlsx')
		try:
			mysheet = workbook.sheets()[0]
		except:
			print("no sheet in sheets named PC")
			return
		#total rows and cols
		print("%d rows, %d cols"%(mysheet.nrows, mysheet.ncols))
		for row in range(0,mysheet.nrows):
			mname = str(mysheet.cell(row,0))[6:len(str(mysheet.cell(row,0))) - 3]
			mwriter = str(mysheet.cell(row,3))[6:len(str(mysheet.cell(row,3))) - 3]
			myear = str(mysheet.cell(row,6))[6:len(str(mysheet.cell(row,6))) - 3]
			mpress = str(mysheet.cell(row,4))[6:len(str(mysheet.cell(row,4))) - 3]
			mcover = str(mysheet.cell(row,1))[6:len(str(mysheet.cell(row,1))) - 3]
			mclassification = str(mysheet.cell(row,11))[6:len(str(mysheet.cell(row,11))) - 3]
			musernumber = 0
			monepoint = 0
			mtwopoint = 0
			mthreepoint = 0
			mfourpoint = 0
			mfivepoint = 0
			mpoint = 0
			mbooknumber = str(mysheet.cell(row,10))[6:len(str(mysheet.cell(row,10))) - 3]
			mwriterintroduce = str(mysheet.cell(row,12))[8:len(str(mysheet.cell(row,12))) - 1]
			mbookintroduce = str(mysheet.cell(row,13))[8:len(str(mysheet.cell(row,13))) - 1]
			mbookprice = str(mysheet.cell(row,8))[6:len(str(mysheet.cell(row,8))) - 3]
			mbookbinding = str(mysheet.cell(row,9))[6:len(str(mysheet.cell(row,9))) - 3]
			mbooktranslater = str(mysheet.cell(row,5))[6:len(str(mysheet.cell(row,5))) - 3]
			a = Book_info(bookname = mname,bookwriter = mwriter,bookyear = myear,bookpress = mpress,classification = mclassification,bookcover = mcover,usernumber = musernumber,onepoint = monepoint,twopoint = mtwopoint,threepoint = mthreepoint,fourpoint = mfourpoint,fivepoint = mfivepoint,point = mpoint,
			booknumber = mbooknumber,writerintroduce = mwriterintroduce,bookintroduce = mbookintroduce,bookprice = mbookprice,bookbinding = mbookbinding,booktranslater = mbooktranslater)
			a.save()
		workbook = xlrd.open_workbook(r'C:\Users\lenovo\Desktop\历史.xlsx')
		try:
			mysheet = workbook.sheets()[0]
		except:
			print("no sheet in sheets named PC")
			return
		#total rows and cols
		print("%d rows, %d cols"%(mysheet.nrows, mysheet.ncols))
		for row in range(0,mysheet.nrows):
			mname = str(mysheet.cell(row,0))[6:len(str(mysheet.cell(row,0))) - 3]
			mwriter = str(mysheet.cell(row,3))[6:len(str(mysheet.cell(row,3))) - 3]
			myear = str(mysheet.cell(row,6))[6:len(str(mysheet.cell(row,6))) - 3]
			mpress = str(mysheet.cell(row,4))[6:len(str(mysheet.cell(row,4))) - 3]
			mcover = str(mysheet.cell(row,1))[6:len(str(mysheet.cell(row,1))) - 3]
			mclassification = str(mysheet.cell(row,11))[6:len(str(mysheet.cell(row,11))) - 3]
			musernumber = 0
			monepoint = 0
			mtwopoint = 0
			mthreepoint = 0
			mfourpoint = 0
			mfivepoint = 0
			mpoint = 0
			mbooknumber = str(mysheet.cell(row,10))[6:len(str(mysheet.cell(row,10))) - 3]
			mwriterintroduce = str(mysheet.cell(row,12))[8:len(str(mysheet.cell(row,12))) - 1]
			mbookintroduce = str(mysheet.cell(row,13))[8:len(str(mysheet.cell(row,13))) - 1]
			mbookprice = str(mysheet.cell(row,8))[6:len(str(mysheet.cell(row,8))) - 3]
			mbookbinding = str(mysheet.cell(row,9))[6:len(str(mysheet.cell(row,9))) - 3]
			mbooktranslater = str(mysheet.cell(row,5))[6:len(str(mysheet.cell(row,5))) - 3]
			a = Book_info(bookname = mname,bookwriter = mwriter,bookyear = myear,bookpress = mpress,classification = mclassification,bookcover = mcover,usernumber = musernumber,onepoint = monepoint,twopoint = mtwopoint,threepoint = mthreepoint,fourpoint = mfourpoint,fivepoint = mfivepoint,point = mpoint,
			booknumber = mbooknumber,writerintroduce = mwriterintroduce,bookintroduce = mbookintroduce,bookprice = mbookprice,bookbinding = mbookbinding,booktranslater = mbooktranslater)
			a.save()
		workbook = xlrd.open_workbook(r'C:\Users\lenovo\Desktop\漫画.xlsx')
		try:
			mysheet = workbook.sheets()[0]
		except:
			print("no sheet in sheets named PC")
			return
		#total rows and cols
		print("%d rows, %d cols"%(mysheet.nrows, mysheet.ncols))
		for row in range(0,mysheet.nrows):
			mname = str(mysheet.cell(row,0))[6:len(str(mysheet.cell(row,0))) - 3]
			mwriter = str(mysheet.cell(row,3))[6:len(str(mysheet.cell(row,3))) - 3]
			myear = str(mysheet.cell(row,6))[6:len(str(mysheet.cell(row,6))) - 3]
			mpress = str(mysheet.cell(row,4))[6:len(str(mysheet.cell(row,4))) - 3]
			mcover = str(mysheet.cell(row,1))[6:len(str(mysheet.cell(row,1))) - 3]
			mclassification = str(mysheet.cell(row,11))[6:len(str(mysheet.cell(row,11))) - 3]
			musernumber = 0
			monepoint = 0
			mtwopoint = 0
			mthreepoint = 0
			mfourpoint = 0
			mfivepoint = 0
			mpoint = 0
			mbooknumber = str(mysheet.cell(row,10))[6:len(str(mysheet.cell(row,10))) - 3]
			mwriterintroduce = str(mysheet.cell(row,12))[8:len(str(mysheet.cell(row,12))) - 1]
			mbookintroduce = str(mysheet.cell(row,13))[8:len(str(mysheet.cell(row,13))) - 1]
			mbookprice = str(mysheet.cell(row,8))[6:len(str(mysheet.cell(row,8))) - 3]
			mbookbinding = str(mysheet.cell(row,9))[6:len(str(mysheet.cell(row,9))) - 3]
			mbooktranslater = str(mysheet.cell(row,5))[6:len(str(mysheet.cell(row,5))) - 3]
			a = Book_info(bookname = mname,bookwriter = mwriter,bookyear = myear,bookpress = mpress,classification = mclassification,bookcover = mcover,usernumber = musernumber,onepoint = monepoint,twopoint = mtwopoint,threepoint = mthreepoint,fourpoint = mfourpoint,fivepoint = mfivepoint,point = mpoint,
			booknumber = mbooknumber,writerintroduce = mwriterintroduce,bookintroduce = mbookintroduce,bookprice = mbookprice,bookbinding = mbookbinding,booktranslater = mbooktranslater)
			a.save()
		workbook = xlrd.open_workbook(r'C:\Users\lenovo\Desktop\小说.xlsx')
		try:
			mysheet = workbook.sheets()[0]
		except:
			print("no sheet in sheets named PC")
			return
		#total rows and cols
		print("%d rows, %d cols"%(mysheet.nrows, mysheet.ncols))
		for row in range(0,mysheet.nrows):
			mname = str(mysheet.cell(row,0))[6:len(str(mysheet.cell(row,0))) - 3]
			mwriter = str(mysheet.cell(row,3))[6:len(str(mysheet.cell(row,3))) - 3]
			myear = str(mysheet.cell(row,6))[6:len(str(mysheet.cell(row,6))) - 3]
			mpress = str(mysheet.cell(row,4))[6:len(str(mysheet.cell(row,4))) - 3]
			mcover = str(mysheet.cell(row,1))[6:len(str(mysheet.cell(row,1))) - 3]
			mclassification = str(mysheet.cell(row,11))[6:len(str(mysheet.cell(row,11))) - 3]
			musernumber = 0
			monepoint = 0
			mtwopoint = 0
			mthreepoint = 0
			mfourpoint = 0
			mfivepoint = 0
			mpoint = 0
			mbooknumber = str(mysheet.cell(row,10))[6:len(str(mysheet.cell(row,10))) - 3]
			mwriterintroduce = str(mysheet.cell(row,12))[8:len(str(mysheet.cell(row,12))) - 1]
			mbookintroduce = str(mysheet.cell(row,13))[8:len(str(mysheet.cell(row,13))) - 1]
			mbookprice = str(mysheet.cell(row,8))[6:len(str(mysheet.cell(row,8))) - 3]
			mbookbinding = str(mysheet.cell(row,9))[6:len(str(mysheet.cell(row,9))) - 3]
			mbooktranslater = str(mysheet.cell(row,5))[6:len(str(mysheet.cell(row,5))) - 3]
			a = Book_info(bookname = mname,bookwriter = mwriter,bookyear = myear,bookpress = mpress,classification = mclassification,bookcover = mcover,usernumber = musernumber,onepoint = monepoint,twopoint = mtwopoint,threepoint = mthreepoint,fourpoint = mfourpoint,fivepoint = mfivepoint,point = mpoint,
			booknumber = mbooknumber,writerintroduce = mwriterintroduce,bookintroduce = mbookintroduce,bookprice = mbookprice,bookbinding = mbookbinding,booktranslater = mbooktranslater)
			a.save()
		workbook = xlrd.open_workbook(r'C:\Users\lenovo\Desktop\推理.xlsx')
		try:
			mysheet = workbook.sheets()[0]
		except:
			print("no sheet in sheets named PC")
			return
		#total rows and cols
		print("%d rows, %d cols"%(mysheet.nrows, mysheet.ncols))
		for row in range(0,mysheet.nrows):
			mname = str(mysheet.cell(row,0))[6:len(str(mysheet.cell(row,0))) - 3]
			mwriter = str(mysheet.cell(row,3))[6:len(str(mysheet.cell(row,3))) - 3]
			myear = str(mysheet.cell(row,6))[6:len(str(mysheet.cell(row,6))) - 3]
			mpress = str(mysheet.cell(row,4))[6:len(str(mysheet.cell(row,4))) - 3]
			mcover = str(mysheet.cell(row,1))[6:len(str(mysheet.cell(row,1))) - 3]
			mclassification = str(mysheet.cell(row,11))[6:len(str(mysheet.cell(row,11))) - 3]
			musernumber = 0
			monepoint = 0
			mtwopoint = 0
			mthreepoint = 0
			mfourpoint = 0
			mfivepoint = 0
			mpoint = 0
			mbooknumber = str(mysheet.cell(row,10))[6:len(str(mysheet.cell(row,10))) - 3]
			mwriterintroduce = str(mysheet.cell(row,12))[8:len(str(mysheet.cell(row,12))) - 1]
			mbookintroduce = str(mysheet.cell(row,13))[8:len(str(mysheet.cell(row,13))) - 1]
			mbookprice = str(mysheet.cell(row,8))[6:len(str(mysheet.cell(row,8))) - 3]
			mbookbinding = str(mysheet.cell(row,9))[6:len(str(mysheet.cell(row,9))) - 3]
			mbooktranslater = str(mysheet.cell(row,5))[6:len(str(mysheet.cell(row,5))) - 3]
			a = Book_info(bookname = mname,bookwriter = mwriter,bookyear = myear,bookpress = mpress,classification = mclassification,bookcover = mcover,usernumber = musernumber,onepoint = monepoint,twopoint = mtwopoint,threepoint = mthreepoint,fourpoint = mfourpoint,fivepoint = mfivepoint,point = mpoint,
			booknumber = mbooknumber,writerintroduce = mwriterintroduce,bookintroduce = mbookintroduce,bookprice = mbookprice,bookbinding = mbookbinding,booktranslater = mbooktranslater)
			a.save()
		workbook = xlrd.open_workbook(r'C:\Users\lenovo\Desktop\随笔.xlsx')
		try:
			mysheet = workbook.sheets()[0]
		except:
			print("no sheet in sheets named PC")
			return
		#total rows and cols
		print("%d rows, %d cols"%(mysheet.nrows, mysheet.ncols))
		for row in range(0,mysheet.nrows):
			mname = str(mysheet.cell(row,0))[6:len(str(mysheet.cell(row,0))) - 3]
			mwriter = str(mysheet.cell(row,3))[6:len(str(mysheet.cell(row,3))) - 3]
			myear = str(mysheet.cell(row,6))[6:len(str(mysheet.cell(row,6))) - 3]
			mpress = str(mysheet.cell(row,4))[6:len(str(mysheet.cell(row,4))) - 3]
			mcover = str(mysheet.cell(row,1))[6:len(str(mysheet.cell(row,1))) - 3]
			mclassification = str(mysheet.cell(row,11))[6:len(str(mysheet.cell(row,11))) - 3]
			musernumber = 0
			monepoint = 0
			mtwopoint = 0
			mthreepoint = 0
			mfourpoint = 0
			mfivepoint = 0
			mpoint = 0
			mbooknumber = str(mysheet.cell(row,10))[6:len(str(mysheet.cell(row,10))) - 3]
			mwriterintroduce = str(mysheet.cell(row,12))[8:len(str(mysheet.cell(row,12))) - 1]
			mbookintroduce = str(mysheet.cell(row,13))[8:len(str(mysheet.cell(row,13))) - 1]
			mbookprice = str(mysheet.cell(row,8))[6:len(str(mysheet.cell(row,8))) - 3]
			mbookbinding = str(mysheet.cell(row,9))[6:len(str(mysheet.cell(row,9))) - 3]
			mbooktranslater = str(mysheet.cell(row,5))[6:len(str(mysheet.cell(row,5))) - 3]
			a = Book_info(bookname = mname,bookwriter = mwriter,bookyear = myear,bookpress = mpress,classification = mclassification,bookcover = mcover,usernumber = musernumber,onepoint = monepoint,twopoint = mtwopoint,threepoint = mthreepoint,fourpoint = mfourpoint,fivepoint = mfivepoint,point = mpoint,
			booknumber = mbooknumber,writerintroduce = mwriterintroduce,bookintroduce = mbookintroduce,bookprice = mbookprice,bookbinding = mbookbinding,booktranslater = mbooktranslater)
			a.save()
	def GetbooksbyClassification(class_name):
		results = []
		pattern = '.*'.join(class_name) # Converts 'djm' to 'd.*j.*m'
		regex = re.compile(pattern) # Compiles a regex.
		for i in Book_info.objects.all():
			match = regex.search(i.classification)
			if match:
				if Book_info.Is_Exist(results,i) == 0:
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
		number = 0
		for i in range(30):
			if Book_info.Is_Exist(results,tempc[i]) == 0:
				results.append(tempc[i])
				number = number + 1
			if number == 10:
				return results
	def Is_Exist(results,book):
		for i in results:
			if i.bookname == book.bookname:
				return 1
		return 0
	def GetbooksbyPoint():
		results = []
		tempc = Book_info.objects.order_by("point")
		number = 0
		for i in range(30):
			if Book_info.Is_Exist(results,tempc[i]) == 0:
				results.append(tempc[i])
				number = number + 1
			if number == 10:
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
				if Book_info.Is_Exist(results,i) == 0:
					results.append(i)
		return results
	def GetbooksbyWriter(writer_name):
		results = []
		pattern = '.*'.join(writer_name) # Converts 'djm' to 'd.*j.*m'
		regex = re.compile(pattern) # Compiles a regex.
		for i in Book_info.objects.all():
			match = regex.search(i.bookwriter)
			if match:
				if Book_info.Is_Exist(results,i) == 0:
					results.append(i)
		return results
		

class User_Book_Info(models.Model):
	username = models.CharField(max_length = 100)
	bookname = models.CharField(max_length = 100)
	status = models.IntegerField()
	point = models.IntegerField()
	def AddBook(musername,mbookname,mstatus):
		if mstatus == "已读":
			if User_Book_Info.objects.filter(username = musername,bookname = mbookname):
				for i in User_Book_Info.objects.filter(username = musername,bookname = mbookname):
					i.delete()
			a = User_Book_Info(username = musername,bookname = mbookname,status = 0,point = 0)
		elif mstatus == "正在读":
			a = User_Book_Info(username = musername,bookname = mbookname,status = 1,point = 0)
			if User_Book_Info.objects.filter(username = musername,bookname = mbookname):
				for i in User_Book_Info.objects.filter(username = musername,bookname = mbookname):
					i.delete()
		elif mstatus == "想读":
			a = User_Book_Info(username = musername,bookname = mbookname,status = 2,point = 0)
			if User_Book_Info.objects.filter(username = musername,bookname = mbookname):
				for i in User_Book_Info.objects.filter(username = musername,bookname = mbookname):
					i.delete()
		a.save()
	def FindBooks(musername,mstatus):
		a = User_Book_Info.objects.filter(username = musername,status = mstatus)
		return a
	
class User_Relationship(models.Model):
	username1 = models.CharField(max_length = 100)
	username2 = models.CharField(max_length = 100)
	def AddFriend(muser1,muser2):
		if Personal_info.objects.filter(username = muser2):
			a = User_Relationship(username1 = muser1,username2 = muser2)
			a.save()
	def FindFriends(user1):
		a = User_Relationship.objects.filter(username1 = user1)
		return a
	def DeleteFriends(user1,user2):
		a = User_Relationship.objects.filter(username1 = user1,username2 = user2)
		a.delete()
	def SearchFriend(user):
		a = Personal_info.objects.filter(nickname = user)
		return a
	
class Message_Record(models.Model):
	username1 = models.CharField(max_length = 100)
	username2 = models.CharField(max_length = 100)
	message = models.CharField(max_length = 100)
	nickname1 = models.CharField(max_length = 100)
	photo1 =  models.ImageField(upload_to = 'upload')
	nickname2 = models.CharField(max_length = 100)
	photo2 =  models.ImageField(upload_to = 'upload')
	date = models.CharField(max_length = 100)
	def StoreMessage(musername1,musername2,mmessage):
		c = str(datetime.datetime.fromtimestamp(time.time()))
		d = c.split('.')[0]
		b = Personal_info.objects.filter(username = musername1)
		e = Personal_info.objects.filter(username = musername2)
		if e:
			if User_Relationship.objects.filter(username1 = b[0].username,username2 = e[0].username):
				if User_Relationship.objects.filter(username1 = e[0].username,username2 = b[0].username):
					a = Message_Record(username1 = musername1,username2 = musername2,message = mmessage,
					nickname1 = b[0].nickname,photo1 = b[0].photo,nickname2 = e[0].nickname,photo2 = e[0].photo,date = d)
					a.save()
					return 1
	def FindMessage(user):
		a = Message_Record.objects.filter(username1 = user)
		b = Message_Record.objects.filter(username2 = user)
		c = []
		for one in a:
			c.append(one)
		for one in b:
			c.append(one)
		listLength = len(c)
		while listLength > 0:
			for i in range(listLength - 1):
				if c[i].date > c[i + 1].date:
					t = c[i + 1]
					c[i + 1] = c[i]
					c[i] = t
			listLength -= 1
		return c
	
class Book_Review(models.Model):
	bookname = models.CharField(max_length = 100)
	username = models.CharField(max_length = 100)
	nickname = models.CharField(max_length = 100)
	comment = models.CharField(max_length = 100)
	time = models.CharField(max_length = 100)
	photo =  models.ImageField(upload_to = 'upload')
	def StoreComment(mbookname,musername,mcomment):
		b = Personal_info.objects.filter(username = musername)
		c = str(datetime.datetime.fromtimestamp(time.time()))
		d = c.split('.')[0]
		if b[0].photo == "":
			a = Book_Review(bookname = mbookname,username = musername,nickname = b[0].nickname,comment = mcomment,time = d,photo = "")
		else:
			a = Book_Review(bookname = mbookname,username = musername,nickname = b[0].nickname,comment = mcomment,time = d,photo = b[0].photo)
		a.save()
	def FindBookReview(mbookname):
		a = Book_Review.objects.filter(bookname = mbookname)
		return a
	def GetCommentsBybookname(mbookname):
		a = Book_Review.objects.filter(bookname = mbookname)
		return a

class Personal_info(models.Model):
	username = models.CharField(max_length = 100)
	password = models.CharField(max_length = 100)
	nickname = models.CharField(max_length = 100)
	gender = models.IntegerField()
	photo =  models.ImageField(upload_to = 'upload')
	region = models.CharField(max_length = 100)
	introduce = models.CharField(max_length = 100)
	#用户名存在的时候返回0,否则返回1
	def MAddUser(musername,muserpassword):
		b = Personal_info.objects.filter(username = musername)
		if len(b) == 0:
			if len(musername) < 8:
				return 2
			elif len(musername) > 20:
				return 2
			elif Personal_info.Is_Simple(muserpassword):
				return 3
			else:
				a = Personal_info(username = musername,password = muserpassword,nickname = "",gender = 0,photo = "",region = "",introduce = "")
				a.save()
				return 1
		else:
			return 0
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
	def Changeuserinfo(musername,mnickname,mregion,mintroduce,mgender,mimg):
		print(1)
		print(mimg)
		a = Personal_info.objects.get(username = musername)
		a.nickname = mnickname
		a.region = mregion
		a.introduce = mintroduce
		if mgender == '男':
			a.gender = 0
		else:
			a.gender = 1
		if a.photo == "":
			a.photo = mimg
		else:
			if mimg == "":
				i = 1
			else:
				print(2)
				a.photo = mimg
		a.save()
		b = Book_Review.objects.filter(username = musername)
		for i in b:
			i.photo = a.photo
			i.nickname = mnickname
			i.save()
		c = Message_Record.objects.filter(username1 = musername)
		for i in c:
			i.photo1 = a.photo
			i.nickname1 = mnickname
			i.save()
		d = Message_Record.objects.filter(username2 = musername)
		for i in d:
			i.photo2 = a.photo
			i.nickname2 = mnickname
			i.save()
	def GetUserByName(musername):
		return Personal_info.objects.get(username = musername)
	def GetUsersByName(nick):
		return Personal_info.objects.filter(username = nick)
	def Is_Simple(password):
		if re.match(r'^(?=.*[A-Za-z])(?=.*[0-9])\w{6,}$',password):
			return 0
		else:
			return 1
		
class Notebook(models.Model):
	username = models.CharField(max_length = 100)
	bookname = models.CharField(max_length = 100)
	notebook = models.CharField(max_length = 500)
	def StoreNotebook(musername,mbookname,mnotebook):
		item = Notebook(username = musername,bookname = mbookname,notebook = mnotebook)
		item.save()
		
	
	
		
		
	
		
			
		
		
