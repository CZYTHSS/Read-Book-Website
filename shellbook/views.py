from django.shortcuts import render
from shellbook.models import Book_info
from django.http import HttpResponse
# 引入我们创建的表单类
from .forms import AddUserForm
from shellbook.models import Personal_info
from shellbook.models import Book_Review
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from shellbook.models import User_Relationship
from shellbook.models import Message_Record
from shellbook.models import User_Book_Info
from shellbook.models import Notebook

# Create your views here.
def home(request):
	if request.method == "GET":
		if len(request.GET) == 0:
			return render(request, 'home.html', {'books': Book_info.GetbooksbyNewDate(), 'hotbooks': Book_info.GetbooksbyPoint()})
		elif len(request.GET) >= 2:
			a = Book_Review.GetCommentsBybookname(request.GET['book'])
			a1 = Book_info.objects.filter(bookname = request.GET['book'],classification = request.GET['class'])[0]
			return render(request,'book.html',{'bookobject':a1,'username':request.GET['username'],'comment':a})
		elif len(request.GET) == 1:
			a = request.GET['username']
			return render(request, 'home.html', {'flag': 1, 'username': a, 'books': Book_info.GetbooksbyNewDate(), 'hotbooks': Book_info.GetbooksbyPoint()})
			
	else:
		print(len(request.POST))
		if len(request.POST) == 0:
			return render(request, 'home.html', {'books': Book_info.GetbooksbyNewDate(), 'hotbooks': Book_info.GetbooksbyPoint()})
		elif len(request.GET) == 0:
			if request.POST['select'] == "书名":
				a = Book_info.GetbooksbyBookname(request.POST['search'])
				return render(request, 'searchresults.html', {'books': a,'flag':0}) 
			elif request.POST['select'] == "作者":
				a = Book_info.GetbooksbyWriter(request.POST['search'])
				return render(request, 'searchresults.html', {'books': a,'flag':0})
			elif request.POST['select'] == "类别":
				a = Book_info.GetbooksbyClassification(request.POST['search'])
				return render(request, 'searchresults.html', {'books': a,'flag':0})	
		else:
			if len(request.POST) == 2:
				User_Book_Info.AddBook(request.GET['username'],request.GET['book'],request.POST['status'])
				a = Book_Review.GetCommentsBybookname(request.GET['book'])
				a1 = Book_info.objects.get(bookname = request.GET['book'],classification = request.GET['class'])
				return render(request,'book.html',{'bookobject':a1,'username':request.GET['username'],'comment':a})
			else:
				Book_Review.StoreComment(request.GET['book'],request.GET['username'],request.POST['comment'])
				a = Book_Review.GetCommentsBybookname(request.GET['book'])
				a1 = Book_info.objects.get(bookname = request.GET['book'],classification = request.GET['class'])
				return render(request,'book.html',{'bookobject':a1,'username':request.GET['username'],'comment':a})

@csrf_protect
def userregister(request):
	if request.POST:   # 当提交表单时
		a = request.POST['username']
		b = request.POST['userpassword']
		if Personal_info.MAddUser(a,b) == 0:
			return render(request, 'user_registration.html', {'flag': 0})
		if Personal_info.MAddUser(a,b) == 2:
			return render(request, 'user_registration.html', {'flag': 2})
		if Personal_info.MAddUser(a,b) == 3:
			return render(request, 'user_registration.html', {'flag': 3})
		else:
			return HttpResponseRedirect("../login/")
	else:# 当正常访问时
		return render(request, 'user_registration.html')
		
def userlogin(request):
	if request.POST:   # 当提交表单时
		if len(request.POST) == 5:
			if request.POST['select'] == "书名":
				a = Book_info.GetbooksbyBookname(request.POST['search'])
				return render(request, 'searchresults.html', {'books': a,'flag':1,'username':request.POST['username']}) 
			elif request.POST['select'] == "作者":
				a = Book_info.GetbooksbyWriter(request.POST['search'])
				return render(request, 'searchresults.html', {'books': a,'flag':1,'username':request.POST['username']})
			elif request.POST['select'] == "类别":
				a = Book_info.GetbooksbyClassification(request.POST['search'])
				return render(request, 'searchresults.html', {'books': a,'flag':1,'username':request.POST['username']})
		elif len(request.POST) == 4:
			if request.POST['select'] == "书名":
				a = Book_info.GetbooksbyBookname(request.POST['search'])
				return render(request, 'searchresults.html', {'books': a,'flag':1,'username':request.POST['username']}) 
			elif request.POST['select'] == "作者":
				a = Book_info.GetbooksbyWriter(request.POST['search'])
				return render(request, 'searchresults.html', {'books': a,'flag':1,'username':request.POST['username']})
			elif request.POST['select'] == "类别":
				a = Book_info.GetbooksbyClassification(request.POST['search'])
				return render(request, 'searchresults.html', {'books': a,'flag':1,'username':request.POST['username']})
		elif len(request.POST) == 3:
			a = request.POST['username']
			b = request.POST['userpassword']
			if Personal_info.VerifyLogin(a,b) == 1:
				return render(request, 'home.html', {'flag': 1, 'username': a, 'books': Book_info.GetbooksbyNewDate(), 'hotbooks': Book_info.GetbooksbyPoint()})
			else:
				return render(request, 'user_login.html',{'flag': 0})
		else:
			return HttpResponse("hello")
	else:# 当正常访问时
		return render(request, 'user_login.html')
		
def userinfo(request):
	if request.POST:
		if len(request.POST) >= 6:# 当提交表单时
			a = request.POST['nickname']
			b = request.POST['region']
			c = request.POST['introduce']
			d = request.POST['userinfo']
			e = request.POST['gender']
			friends = User_Relationship.FindFriends(d)
			results = []
			for friend in friends:
				results.append(Personal_info.objects.get(username = friend.username2))
			message = []
			message = Message_Record.FindMessage(d)
			books = User_Book_Info.FindBooks(d,0)
			results2 = []
			for book in books:
				results2.append(Book_info.objects.filter(bookname = book.bookname)[0])
			books = User_Book_Info.FindBooks(d,1)
			results3 = []
			for book in books:
				results3.append(Book_info.objects.filter(bookname = book.bookname)[0])
			books = User_Book_Info.FindBooks(d,2)
			results4 = []
			for book in books:
				results4.append(Book_info.objects.filter(bookname = book.bookname)[0])
			if len(request.FILES) == 1:
				f = request.FILES['img']
				Personal_info.Changeuserinfo(d,a,b,c,e,f)
				return render(request, 'personalhome.html',{'username':d,
					'nickname':Personal_info.GetUserByName(d).nickname,
					'region':Personal_info.GetUserByName(d).region,
					'introduce':Personal_info.GetUserByName(d).introduce,
					'gender':Personal_info.GetUserByName(d).gender,
					'img':Personal_info.GetUserByName(d).photo.url,
					'friends':results,
					'message':message,
					'books_isreading':results3,
					'books_read':results2,
					'bookswanted':results4})
			else:
				f = ""
				Personal_info.Changeuserinfo(d,a,b,c,e,f)
				if Personal_info.GetUserByName(d).photo.url:
					return render(request, 'personalhome.html',{'username':d,
					'nickname':Personal_info.GetUserByName(d).nickname,
					'region':Personal_info.GetUserByName(d).region,
					'introduce':Personal_info.GetUserByName(d).introduce,
					'gender':Personal_info.GetUserByName(d).gender,
					'img':Personal_info.GetUserByName(d).photo.url,
					'friends':results,
					'message':message,
					'books_isreading':results3,
					'books_read':results2,
					'bookswanted':results4})
				else:
					return render(request, 'personalhome.html',{'username':d,
						'nickname':Personal_info.GetUserByName(d).nickname,
						'region':Personal_info.GetUserByName(d).region,
						'introduce':Personal_info.GetUserByName(d).introduce,
						'gender':Personal_info.GetUserByName(d).gender,
						'img':"http://127.0.0.1:8000/media/upload/desert.jpg",
						'friends':results,
						'message':message,
						'books_isreading':results3,
						'books_read':results2,
						'bookswanted':results4})
		elif len(request.POST) == 4:
			if request.POST['add'] == "添加好友":
				a = request.POST['friends']
				b = request.POST['username']
				User_Relationship.AddFriend(b,a)
				friends = User_Relationship.FindFriends(b)
				results = []
				for friend in friends:
					results.append(Personal_info.objects.get(username = friend.username2))
				message = []
				message = Message_Record.FindMessage(b)
				books = User_Book_Info.FindBooks(b,0)
				results2 = []
				for book in books:
					results2.append(Book_info.objects.filter(bookname = book.bookname)[0])
				books = User_Book_Info.FindBooks(b,1)
				results3 = []
				for book in books:
					results3.append(Book_info.objects.filter(bookname = book.bookname)[0])
				books = User_Book_Info.FindBooks(b,2)
				results4 = []
				for book in books:
					results4.append(Book_info.objects.filter(bookname = book.bookname)[0])
				if Personal_info.objects.get(username = b).photo == "":
					return render(request, 'personalhome.html',{'username':b,
						'nickname':Personal_info.GetUserByName(b).nickname,
						'region':Personal_info.GetUserByName(b).region,
						'introduce':Personal_info.GetUserByName(b).introduce,
						'gender':Personal_info.GetUserByName(b).gender,
						'img':"http://127.0.0.1:8000/media/upload/desert.jpg",
						'friends':results,
						'message':message,
						'books_isreading':results3,
						'books_read':results2,
						'bookswanted':results4})
				else:
					return render(request, 'personalhome.html',{'username':b,
						'nickname':Personal_info.GetUserByName(b).nickname,
						'region':Personal_info.GetUserByName(b).region,
						'introduce':Personal_info.GetUserByName(b).introduce,
						'gender':Personal_info.GetUserByName(b).gender,
						'img':Personal_info.GetUserByName(b).photo.url,
						'friends':results,
						'message':message,
						'books_isreading':results3,
						'books_read':results2,
						'bookswanted':results4})
		elif len(request.POST) == 5:
			a = request.POST['friend']
			b = request.POST['username']
			c = request.POST['context']
			Message_Record.StoreMessage(b,a,c)
			friends = User_Relationship.FindFriends(b)
			results = []
			for friend in friends:
				results.append(Personal_info.objects.get(username = friend.username2))
			message = []
			message = Message_Record.FindMessage(b)
			books = User_Book_Info.FindBooks(b,0)
			results2 = []
			for book in books:
				results2.append(Book_info.objects.filter(bookname = book.bookname)[0])
			books = User_Book_Info.FindBooks(b,1)
			results3 = []
			for book in books:
				results3.append(Book_info.objects.filter(bookname = book.bookname)[0])
			books = User_Book_Info.FindBooks(b,2)
			results4 = []
			for book in books:
				results4.append(Book_info.objects.filter(bookname = book.bookname)[0])
			if Personal_info.objects.get(username = b).photo == "":
				return render(request, 'personalhome.html',{'username':b,
					'nickname':Personal_info.GetUserByName(b).nickname,
					'region':Personal_info.GetUserByName(b).region,
					'introduce':Personal_info.GetUserByName(b).introduce,
					'gender':Personal_info.GetUserByName(b).gender,
					'img':"http://127.0.0.1:8000/media/upload/desert.jpg",
					'friends':results,
					'message':message,
					'books_isreading':results3,
					'books_read':results2,
					'bookswanted':results4})
			else:
				return render(request, 'personalhome.html',{'username':b,
					'nickname':Personal_info.GetUserByName(b).nickname,
					'region':Personal_info.GetUserByName(b).region,
					'introduce':Personal_info.GetUserByName(b).introduce,
					'gender':Personal_info.GetUserByName(b).gender,
					'img':Personal_info.GetUserByName(b).photo.url,
					'friends':results,
					'message':message,
					'books_isreading':results3,
					'books_read':results2,
					'bookswanted':results4})	
			
	mname = str(request.GET['username'])
	friends = User_Relationship.FindFriends(mname)
	results = []
	for friend in friends:
		results.append(Personal_info.objects.get(username = friend.username2))
	message = []
	message = Message_Record.FindMessage(mname)
	books = User_Book_Info.FindBooks(mname,0)
	results2 = []
	for book in books:
		results2.append(Book_info.objects.filter(bookname = book.bookname)[0])
	books = User_Book_Info.FindBooks(mname,1)
	results3 = []
	for book in books:
		results3.append(Book_info.objects.filter(bookname = book.bookname)[0])
	books = User_Book_Info.FindBooks(mname,2)
	results4 = []
	for book in books:
		results4.append(Book_info.objects.filter(bookname = book.bookname)[0])
	if Personal_info.GetUserByName(mname).photo == "":
		return render(request, 'personalhome.html',{'username':mname,
				'nickname':Personal_info.GetUserByName(mname).nickname,
				'region':Personal_info.GetUserByName(mname).region,
				'introduce':Personal_info.GetUserByName(mname).introduce,
				'gender':Personal_info.GetUserByName(mname).gender,
				'img':"http://127.0.0.1:8000/media/upload/desert.jpg",
				'friends':results,
				'message':message,
				'books_isreading':results3,
				'books_read':results2,
				'bookswanted':results4})
	else:
		return render(request, 'personalhome.html',{'username':mname,
				'nickname':Personal_info.GetUserByName(mname).nickname,
				'region':Personal_info.GetUserByName(mname).region,
				'introduce':Personal_info.GetUserByName(mname).introduce,
				'gender':Personal_info.GetUserByName(mname).gender,
				'img':Personal_info.GetUserByName(mname).photo.url,
				'friends':results,
				'message':message,
				'books_isreading':results3,
				'books_read':results2,
				'bookswanted':results4})
				
def notebook(request):
	if request.POST:
		print(request.POST)
		if request.POST['score'] == "提交":
			musername = request.GET['username']
			mbookname = request.GET['book']
			mnotebook = request.POST['notebook']
			Notebook.StoreNotebook(musername,mbookname,mnotebook)
			notebooks = Notebook.objects.filter(username = musername)
			return render(request, 'notebook.html',{'notebooks':notebooks})
		else:
			musername = request.GET['username']
			mbookname = request.GET['book']
			temp = User_Book_Info.objects.get(username = musername,bookname = mbookname)
			notebooks = Notebook.objects.filter(username = musername)
			if temp.point == 0:
				temp.point = int(request.POST['score'][0])
				books = Book_info.objects.filter(bookname = mbookname)
				for book in books:
					if temp.point == 1:
						book.onepoint = book.onepoint + 1
					elif temp.point == 2:
						book.twopoint = book.twopoint + 1
					elif temp.point == 3:
						book.threepoint = book.threepoint + 1
					elif temp.point == 4:
						book.fourpoint = book.fourpoint + 1
					elif temp.point == 5:
						book.fivepoint = book.fivepoint + 1
					book.usernumber = book.usernumber + 1
					book.point = (book.onepoint + book.twopoint * 2 + book.threepoint * 3 + book.fourpoint * 4 + book.fivepoint * 5) / book.usernumber
					book.save()
				temp.save()
			else:
				books = Book_info.objects.filter(bookname = mbookname)
				for book in books:
					if temp.point == 1:
						book.onepoint = book.onepoint - 1
					elif temp.point == 2:
						book.twopoint = book.twopoint - 1
					elif temp.point == 3:
						book.threepoint = book.threepoint - 1
					elif temp.point == 4:
						book.fourpoint = book.fourpoint - 1
					elif temp.point == 5:
						book.fivepoint = book.fivepoint - 1
				temp.point = int(request.POST['score'][0])
				books = Book_info.objects.filter(bookname = mbookname)
				for book in books:
					if temp.point == 1:
						book.onepoint = book.onepoint + 1
					elif temp.point == 2:
						book.twopoint = book.twopoint + 1
					elif temp.point == 3:
						book.threepoint = book.threepoint + 1
					elif temp.point == 4:
						book.fourpoint = book.fourpoint + 1
					elif temp.point == 5:
						book.fivepoint = book.fivepoint + 1
					book.point = (book.onepoint + book.twopoint * 2 + book.threepoint * 3 + book.fourpoint * 4 + book.fivepoint * 5) / book.usernumber
					book.save()
				temp.save()
			return render(request, 'notebook.html',{'notebooks':notebooks})
	musername = request.GET['username']
	notebooks = Notebook.objects.filter(username = musername)
	return render(request, 'notebook.html',{'notebooks':notebooks})