from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
# Create your views here.

# @api_view(['POST'])
def hello(request):
	if request.method == 'POST':
		return render(request, template_name='mall.html', context={'name': '李四'})
		print(request.GET.get('a'))
		a = request.GET.get('a')
		b = request.GET.get('b')
		if a is not None and b is not None:
			return render(request, template_name='mall.html', context={'name': '李四'})
		else:
			return render(request, template_name='error.html', context={'msg': '缺少必要参数'})
	else:
		# return HttpResponse(status=405, reason='aaa method not allowed')
		return JsonResponse(data={'a':123, 'b':456})
	
@api_view(['POST'])
def hello2(request):
	source = {
		"business_autoFans_J": [14, 15, 9],
		"autoAX": [7, 32, 0],
		"autoAX_admin": [5, 13, 2],
	}
	pname = request.POST.get('pname')
	if pname is not None:
		if pname in source.keys():
			return JsonResponse({'total': sum(source[pname]), 'name': pname})
		else:
			return JsonResponse({'total': -1, 'name': None})
	else:
		total = 0
		for k, v in source.items():
			total += sum(source[k])
		return JsonResponse({'total': total, 'name': 'all'})
	