from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Categories, Comment, User, Auction_listing


def index(request):
    return render(request, "auctions/index.html",{
        "listings": Auction_listing.objects.all() 
    })


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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@ login_required
def create_listing(request):
    if request.method == "POST":
        listing = Auction_listing(
            title=request.POST["title"],
            description=request.POST["description"],
            cover_url=request.POST["cover"],
            provider=request.user,
            bidder = request.user,
            category=Categories.objects.get(pk=int(request.POST["category"])),
            bid=request.POST["bid"],
            active=True
        )
        listing.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/create_listing.html", {
            "categories": Categories.objects.all()
        })

def categories_list(request):
    return render(request, "auctions/categories_list.html", {
        "categories": Categories.objects.all()
    })

@login_required
def auction_display(request, auction_id):
    auction = Auction_listing.objects.get(pk=auction_id) 
    if request.method == "POST":
        if request.POST.get("in_watchlist") != None:
            if request.POST["in_watchlist"] == "True":
                request.user.watchlist.add(auction)
            elif request.POST["in_watchlist"] == "False":
                request.user.watchlist.remove(auction)
        elif request.POST.get("active") != None:
            if request.POST["active"] == "True":
                auction.bid = request.POST["bid"]
                auction.bidder = request.user
            else:
                auction.active = False
        elif request.POST.get("comment") != None:
            Comment.objects.create(
                commenter=request.user,
                content=request.POST["comment"],
                item=auction
            )
        auction.save()
        request.user.save()
    return render(request, "auctions/auction_display.html", {
        "auction": auction,
        "watchlist": request.user.watchlist.all(),
        "comments": Comment.objects.filter(item=auction),
    })

@login_required
def watchlist(request):
    return render(request, "auctions/watchlist.html", {
        "watchlist": request.user.watchlist.all()
    })

def category_display(request, category_id):
    category = Categories.objects.get(pk=category_id)
    return render(request, "auctions/category_display.html", {
        "list": Auction_listing.objects.filter(category=category),
        "category": category
    })