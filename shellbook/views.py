from django.shortcuts import render
from shellbook.models import Book_info
from django.http import HttpResponse
# 引入我们创建的表单类
from .forms import AddUserForm
from shellbook.models import Personal_info
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def home(request):
	books = Book_info.GetbooksbyNewDate()
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
def userlogin(request):
	if request.POST:   # 当提交表单时     
		a = request.POST['username']
		b = request.POST['userpassword']
		if Personal_info.VerifyLogin(a,b) == 1:
			return HttpResponse('login succeeded')
		else:
			return render(request, 'user_login.html')
	else:# 当正常访问时
		return render(request, 'user_login.html')