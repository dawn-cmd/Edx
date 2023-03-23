from datetime import date
from json.decoder import JSONDecodeError
from django.contrib.auth import authenticate, login, logout
from django.core import paginator
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import json

from .models import User, Post

item_num = 10

def index(request):
    return render(request, "network/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def profile(request, name):
    return render(request, 'network/profile.html', {
        "name": name,
    })

def following(request):
    return render(request, 'network/following.html')

@login_required
def edit(request, id):
    if request.method == "POST":
        post = Post.objects.get(id=id)
        post.content = request.POST.get("content")
        post.save()
        return HttpResponseRedirect(reverse('index'))
    if Post.objects.get(id=id).poster != request.user:
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'network/edit.html', {
        "id": id,
        "content": Post.objects.get(id=id).content,
    })

@csrf_exempt
@login_required
def post(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST method is required"}, status=400)
    data = json.loads(request.body)
    post = Post(
        content=data.get("content"),
        poster=request.user,
    )
    post.save()
    return JsonResponse({"message": "post successfully"}, status=201)

@csrf_exempt
def posts(request):
    data = json.loads(request.body)
    page_num = int(data.get("page")) 
    if data.get("poster") == "all":
        results = Post.objects.all()
    elif data.get("poster") == "following":
        results = Post.objects.filter(poster__in=request.user.followed.all())
    else:
        results = Post.objects.filter(poster=User.objects.get(username=data.get("poster")))
    results = results.order_by('-timestamp').all()
    paginator = Paginator(results, item_num) 
    if paginator.num_pages < page_num:
        return JsonResponse({"error": "extends page id"})
    page_obj = paginator.page(page_num)
    l = []
    for i in page_obj.object_list:
        l.append(i.serialize()) 
        if len(request.user.likes.filter(id=i.id)) == 0:
            l[len(l) - 1]["get_like"] = "unlike"
        else:  
            l[len(l) - 1]["get_like"] = "like"
    return JsonResponse(l, safe=False)

@csrf_exempt
def maxpage(request):
    data = json.loads(request.body)
    if data.get("poster") == "all":
        results = Post.objects.all()
    elif data.get("poster") == 'following':
        results = Post.objects.filter(poster__in=request.user.followed.all())
    else:
        results = Post.objects.filter(poster=User.objects.get(username=data.get("poster")))
    paginator = Paginator(results, item_num)
    return JsonResponse({"page_num": f"{paginator.num_pages}"})

@csrf_exempt
def get_follow(request):
    data = json.loads(request.body)
    u = User.objects.get(username=data.get("user"))
    if data.get("type") == "follower":
        return JsonResponse({"follower": f"{u.follower.count()}", "type": data.get("type"), "user": data.get("user")})
    else:
        return JsonResponse({"followed": f"{u.followed.all().count()}", "type": data.get("type"), "user": data.get("user")})

@csrf_exempt
def has_followed(request):
    data = json.loads(request.body)
    if data.get('name') == request.user.username:
        return JsonResponse({"error": "The same people."})
    l = request.user.followed.filter(username=f"{data.get('name')}")
    if len(l) == 0:
        return JsonResponse({"followed": "n"})
    else:
        return JsonResponse({"followed": "y"})

@csrf_exempt
def become_followed(request):
    data = json.loads(request.body)
    if data.get("command") == "follow":
        request.user.followed.add(User.objects.get(username=data.get("name")))
        return JsonResponse({"message": "Successfully followed"})
    elif data.get("command") == "unfollow":
        request.user.followed.remove(User.objects.get(username=data.get("name")))
        return JsonResponse({"message": "Successfully removed"})

@csrf_exempt
@login_required
def like(request):
    data = json.loads(request.body)
    id = int(data["id"])
    command = data["command"]
    if command == "like":
        request.user.likes.add(Post.objects.get(id=id))
        return JsonResponse({"message": "successfully like", "id": f"{id}"})
    else:
        request.user.likes.remove(Post.objects.get(id=id))
        return JsonResponse({"message": "successfully remove", "id": f"{id}"})

@csrf_exempt
@login_required
def get_like(request):
    data = json.loads(request.body)
    id = int(data.get("id"))
    if len(request.user.likes.filter(id=id)) == 0:
        return JsonResponse({"result": "n", "id": f"{id}"})
    else:
        return JsonResponse({"result": "y", "id": f"{id}"}) 