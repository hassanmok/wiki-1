from django.shortcuts import render
from markdown2 import Markdown
from . import util
import random

def convert_md_to_html(title):
    content = util.get_entry(title)
    markdown = Markdown()
    if content == None:
        return None
    else:
        return markdown.convert(content)
    

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    html_content = convert_md_to_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html",{
            "message":"This page not found"
        })
    else:
        return render(request, "encyclopedia/entry.html",{
            "title":title,
            "content":html_content
        })
def search(request):
    if request.method == "POST":
        entry_search = request.POST["q"]
        html_content = convert_md_to_html(entry_search)
        if html_content is not None:
            return render(request, "encyclopedia/entry.html",{
            "title":entry_search,
            "content":html_content
        })
        else:
            allentries = util.list_entries()
            new_list = []
            for entry in allentries:
                if entry_search.lower() in entry.lower():
                    new_list.append(entry)
            count = 0
            for n in new_list:
                if n is not None:
                    count +=1
            if count > 0:
                return render(request, "encyclopedia/search.html",{
                    "title":"Entries",
                    "new_list":new_list
            })
            else:
                return render(request, "encyclopedia/search.html",{
                    "title":"Error",
                    "message":"not found"
            })
            

def Create_New_Page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/Create_New_Page.html")
    else:
        new_title = request.POST['new_title']
        new_content = request.POST['new_content']
        title_exsit = util.get_entry(new_title)
        if title_exsit is not None:
            return render(request, "encyclopedia/error.html",{
                "message": "the entry already exists"
            })
        else:
            util.save_entry(new_title, new_content)
            html_content = convert_md_to_html(new_title)
            return render(request, "encyclopedia/entry.html",{
                "title": new_title,
                "content": new_content 
            })
        
def edit(request):
    if request.method == "POST":
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html",{
            "title": title,
            "content": content
        })
    

def new_edit(request):
    if request.method == "POST":
        title = request.POST['new_title']
        content = request.POST['new_content']
        util.save_entry(title, content)
        html_content = convert_md_to_html(title)
        return render(request, "encyclopedia/entry.html",{
                "title": title,
                "content": html_content 
            })
    
def random_entry(request):
    entry = util.list_entries()
    ran_en = random.choice(entry)
    html_content = convert_md_to_html(ran_en)
    return render(request, "encyclopedia/entry.html",{
                "title": ran_en,
                "content": html_content 
            })






