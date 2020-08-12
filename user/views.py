from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework.decorators import api_view
import json
from util import *
# Create your views here.

@api_view(['POST'])
def hello(request):
	print(request.body)
	try:
		data = json.loads(request.body)
		print(data)
	except:
		return render(request, template_name='error.html', context={'msg': '入参json格式错误'})
	a = data.get('a')
	b = data.get('b')
	if a is not None and b is not None:
		return render(request, template_name='user.html', context={'name': 'json'})
	else:
		return render(request, template_name='error.html', context={'msg': 'json缺少必要参数'})

@api_view(['GET'])
def login(request):
	return render(request, template_name='login.html')


def home(request):
	username = request.COOKIES.get('username')
	print(username)
	try:
		password = request.get_signed_cookie('password')
	except:
		password = None
	if is_login(username, password) is not None:
		return render(request, template_name='home.html', context={"name": username})
	else:
		res = HttpResponseRedirect('/user/login', content={'msg': '请先登录'})
		return res


@api_view(['POST'])
def api_login(request):
	data = request.POST

	username = data.get('username')
	password = data.get('password')
	is_cookie = data.get('is_login')
	if username is not None and password is not None:
		is_av = is_login(username, password)
		if is_av is not None:
			res = HttpResponseRedirect('/user/home/')
			if is_cookie == 'on':
				res.set_cookie("uid", is_av, max_age=3600)
				res.set_cookie("username", username, max_age=3600)
				res.set_signed_cookie("password", password, max_age=3600)
			else:
				res.set_cookie("uid", is_av)
				res.set_cookie("username", username)
				res.set_signed_cookie("password", password)
				print(res.cookies)
			return res
		else:
			return render(request, template_name='error.html', context={'msg': '用户名或密码都错误'})
	else:
		return render(request, template_name='error.html', context={'msg': '用户名、密码必填'})


@api_view(['POST', 'GET'])
def api_logout(request):
	res = HttpResponseRedirect('/user/login/')
	res.delete_cookie('uid')
	res.delete_cookie('username')
	res.delete_cookie('password')
	return res