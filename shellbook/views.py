from django.shortcuts import render
from shellbook.models import Book_info
from django.http import HttpResponse
# 引入我们创建的表单类
from .forms import AddUserForm
from shellbook.models import Personal_info
from shellbook.models import Book_Review
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
	if request.method == "GET":
		if len(request.GET) == 0:
			return render(request, 'home.html', {'books': Book_info.GetbooksbyNewDate(), 'hotbooks': Book_info.GetbooksbyPoint()})
		elif len(request.GET) > 0:
			a = Book_info.objects.get(bookname = request.GET['book'],classification = request.GET['class'])
			return render(request,'book.html',{'bookobject':a})
	else:
		if len(request.POST) == 0:
			return render(request, 'home.html', {'books': Book_info.GetbooksbyNewDate(), 'hotbooks': Book_info.GetbooksbyPoint()})
		elif len(request.GET) == 0:
			if request.POST['select'] == "书名":
				a = Book_info.GetbooksbyBookname(request.POST['search'])
				return render(request, 'searchresults.html', {'books': a}) 
			elif request.POST['select'] == "作者":
				a = Book_info.GetbooksbyWriter(request.POST['search'])
				return render(request, 'searchresults.html', {'books': a})
			elif request.POST['select'] == "类别":
				a = Book_info.GetbooksbyClassification(request.POST['search'])
				return render(request, 'searchresults.html', {'books': a})	
		else:
			Book_Review.StoreComment(request.GET['book'],"yuyuanhang",request.POST['comment'])
			return HttpResponse("hello")

@csrf_protect
def userregister(request):
	if request.POST:   # 当提交表单时     
		a = request.POST['username']
		b = request.POST['userpassword']
		if Personal_info.MAddUser(a,b) == 0:
			return render(request, 'user_registration.html', {'flag': 0})
		else:
			return HttpResponseRedirect("../login/")
	else:# 当正常访问时
		return render(request, 'user_registration.html')
def userlogin(request):
	if request.POST:   # 当提交表单时  
		print(request.POST)
		a = request.POST['username']
		b = request.POST['userpassword']
		if Personal_info.VerifyLogin(a,b) == 1:
			return render(request, 'home.html', {'flag': 1, 'username': a, 'books': Book_info.GetbooksbyNewDate(), 'hotbooks': Book_info.GetbooksbyPoint()})
		else:
			return render(request, 'user_login.html',{'flag': 0})
	else:# 当正常访问时
		return render(request, 'user_login.html')
def userinfo(request):
	if request.POST:   # 当提交表单时
		a = request.POST['nickname']
		b = request.POST['region']
		c = request.POST['introduce']
		d = request.POST['userinfo']
		e = request.POST['gender']
		f = request.FILES['img']
		Personal_info.Changeuserinfo(d,a,b,c,e,f)
		print(Personal_info.GetUserByName(d).gender)
		return render(request, 'personalhome.html',{'username':d,
				'nickname':Personal_info.GetUserByName(d).nickname,
				'region':Personal_info.GetUserByName(d).region,
				'introduce':Personal_info.GetUserByName(d).introduce,
				'gender':Personal_info.GetUserByName(d).gender,
				'img':Personal_info.GetUserByName(d).photo.url})
	mname = str(request.GET['username'])
	return render(request, 'personalhome.html',{'username':mname,
				'nickname':Personal_info.GetUserByName(mname).nickname,
				'region':Personal_info.GetUserByName(mname).region,
				'introduce':Personal_info.GetUserByName(mname).introduce,
				'gender':Personal_info.GetUserByName(mname).gender,
				'img':Personal_info.GetUserByName(mname).photo.url})