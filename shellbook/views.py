from django.shortcuts import render
from shellbook.models import Book_info
from django.http import HttpResponse
# 引入我们创建的表单类
from .forms import AddUserForm
from shellbook.models import Personal_info
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def home(request):
	class book:
		def __init__(self):
			book.name = ""
			book.author = ""
			book.date = ""
	book1 = book()
	book1.name = "三重门"
	book1.author = "韩寒"
	book1.date = "2003-09"
	book2 = book()
	book2.name = "三重门"
	book2.author = "韩寒"
	book2.date = "2003-09"
	book3 = book()
	book3.name = "三重门"
	book3.author = "韩寒"
	book3.date = "2003-09"
	book4 = book()
	book4.name = "三重门"
	book4.author = "韩寒"
	book4.date = "2003-09"
	book5 = book()
	book5.name = "三重门"
	book5.author = "韩寒"
	book5.date = "2003-09"
	books = [book1,book2,book3,book4,book5]
	return render(request, 'home.html', {'books': books}) 

@csrf_protect
def userregister(request):
	if request.POST:   # 当提交表单时     
		a = request.POST['username']
		b = request.POST['userpassword']
		Personal_info.MAddUser(a,b)
		return HttpResponse('hello')
	else:# 当正常访问时
		return render(request, 'user_registration.html')