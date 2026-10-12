#from django.http import render
from django.shortcuts import render,redirect
from datetime import datetime
from mysite.models import Post

def showpost(request, slug):
	try:
		post = Post.objects.get(slug = slug)
		if post != None:
			return render(request, 'post.html', locals())
	except:
		return redirect('/')

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())

# 新聞直播頻道。直播影片 ID 可能變更；請以新聞台官方最新直播網址更新。
TV_LIST = [
{'name': '中天', 'tvcode': 'vr3XyVCR4T0',
'official_url': 'https://www.ctitv.com.tw/'},
{'name': '華視', 'tvcode': 'wM0g8EoUZ_E',
'official_url': 'https://news.cts.com.tw/live'},
{'name': '民視', 'tvcode': 'MCnk4m2CliM',
'official_url': 'https://www.ftvnews.com.tw/'},
{'name': '中視', 'tvcode': 'Z2mfmGIPh4Q',
'official_url': 'https://www.ctv.com.tw/'},
]

def news_live(request, tvno=0):
	if not 0 <= tvno < len(TV_LIST):
		return redirect('news-live-home')
	tv_list = TV_LIST
	tv = tv_list[tvno]
	now = datetime.now()
	return render(request, 'index.html', {
	'tv': tv,
	'tvno': tvno,
	'tv_list': tv_list,
	'now': now,
	})

def carlist(request, maker=0):
	car_maker = ['SAAB', 'Ford', 'Honda', 'Mazda', 'Nissan','Toyota' ]
	car_list = [ [],
	['Fiesta', 'Focus', 'Modeo', 'EcoSport', 'Kuga', 'Mustang'],
	['Fit', 'Odyssey', 'CR-V', 'City', 'NSX'],
	['Mazda3', 'Mazda5', 'Mazda6', 'CX-3', 'CX-5', 'MX-5'],
	['Tida', 'March', 'Livina', 'Sentra', 'Teana', 'X-Trail', 'Juke', 'Murano'],
	['Camry','Altis','Yaris','86','Prius','Vios', 'RAV4', 'Wish']
	]
	maker = maker
	maker_name = car_maker[maker]
	cars = car_list[maker]
	return render(request, 'carlist.html', locals())

def carprice(request, maker=0):
	car_maker = ['Ford', 'Honda', 'Mazda']
	car_list = [[ {'model':'Fiesta', 'price': 203500},
	{'model':'Focus','price': 605000},
	{ 'model':'Mustang','price': 900000}],
	[{'model':'Fit', 'price': 450000},
	{'model':'City', 'price': 150000},
	{'model':'NSX', 'price':1200000}],
	[{'model':'Mazda3', 'price': 329999},
	{'model':'Mazda5', 'price': 603000},
	{'model':'Mazda6', 'price':850000}],]
	maker = maker
	maker_name = car_maker[maker]
	cars = car_list[maker]
	return render(request, 'carprice.html', locals())