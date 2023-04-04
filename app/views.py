import tweepy
from django.conf import settings
from django.shortcuts import render,redirect

# Create your views here.

def index(request):
    if request.method == 'POST':
        content = request.POST.get('content', '')

        if content:
            print('Content:', content)

            auth = tweepy.OAuthHandler(settings.TWITTER_API_KEY, settings.TWITTER_API_SECRET_KEY)
            auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)

            api = tweepy.API(auth)
            api.update_status(content)

            return redirect ('home')

    context = {}

    return render(request, 'post/index.html',context)