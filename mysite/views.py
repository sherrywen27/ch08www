from django.shortcuts import render
from django.http import HttpResponse
from mysite import models

def index(request):
    # posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    posts = models.Post.objects.all().order_by('-pub_time')
    moods = models.Mood.objects.all()
    try:
        user_id = request.GET['user_id']
        user_pass = request.GET['user_pass']
        user_post = request.GET['user_post']
        user_mood = request.GET['mood']
    except:
        user_id = None
        message = '如果要張貼訊息，則每一個欄位都要填寫'

    if user_id is not None:
        mood = models.Mood.objects.get(status=user_mood)
        post = models.Post.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
        post.save()
        message = '成功儲存! 請記得你的編輯密碼[{}]!'.format(user_pass)

    return render(request, 'index.html', locals())