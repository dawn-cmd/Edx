from django.forms.forms import Form
from django.forms.widgets import Textarea
from django.shortcuts import render
from . import util
from django import forms
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from markdown2 import Markdown
from django.contrib import messages
import random

class NewEntryForm(forms.Form):

    title = forms.CharField(label="Title", required=True)
    text = forms.CharField(widget=forms.Textarea)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def creat(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid() and util.get_entry(form.cleaned_data["title"]) == None:
            util.save_entry(
                form.cleaned_data["title"], form.cleaned_data["text"])
            return HttpResponseRedirect(reverse("entry", args=[form.cleaned_data["title"]]))
        else:
            messages.error(request, 'The entry has already existed.')
            return render(request, "encyclopedia/creat.html", {
                "form": form
            })
    return render(request, "encyclopedia/creat.html", {
        "form": NewEntryForm()
    })


def entry(request, title):
    if util.get_entry(title) == None:
        return render(request, "encyclopedia/404.html")
    else:
        text = util.get_entry(title)
        markdowner = Markdown()
        text = markdowner.convert(text)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "text": text
        })

def randpage(request):
    l = util.list_entries()
    id = random.randint(0, len(l) - 1)
    return HttpResponseRedirect(reverse("entry", args=[l[id]]))

class EditEntry(forms.Form):

    text = forms.CharField(widget=forms.Textarea)

def edit(request, title):
    if request.method == "POST":
        form = EditEntry(request.POST)
        if form.is_valid():
            util.save_entry(title, form.cleaned_data["text"])
            return HttpResponseRedirect(reverse("entry", args=[title]))
    area = EditEntry(initial={'text': util.get_entry(title)})
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "area": area
    })

def search(request):
    info = request.GET.get("q")
    for title in util.list_entries():
        if info == title:
            return HttpResponseRedirect(reverse("entry", args=[title]))
    results = [x for i, x in enumerate(util.list_entries()) if x.find(info) != -1] 
    l = len(results)
    return render(request, "encyclopedia/search result.html", locals())
