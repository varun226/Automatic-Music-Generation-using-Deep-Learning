from django.shortcuts import render
from django.http import HttpResponse
import requests
from subprocess import run,PIPE
import sys

def index_page(request):
    return render(request, 'index.html')

def amg(request):
    return render(request, 'AMG.html')

def script(request):
    inp = request.POST.get('instrument')
    print(inp)
    out = run([sys.executable, 'D://Study Related//SEM 6//Mini Project//Code//AMGnew.py',inp],shell=False,stdout=PIPE)
    return render(request, 'AMG.html', {'generated':True})

def signup(request):
    import sqlite3
    con=sqlite3.connect('D://Study Related//SEM 6//Mini Project//AMG//amg.db')
    cursorobj=con.cursor()

    #creating table if not exists
    cursorobj.execute('CREATE TABLE IF NOT EXISTS members (Name varchar(50), email varchar(200) PRIMARY KEY, pass varchar(100))')

    name = request.POST.get('name')
    emailid = request.POST.get('emailid')
    pwd = request.POST.get('pwd')
    #print(name, emailid, pwd)
    
    data = cursorobj.execute('SELECT name FROM members WHERE email = ?',(emailid,))
    result = data.fetchall()
    if len(result) == 0:
        cursorobj.execute('INSERT INTO members VALUES (?, ?, ?)',(name, emailid, pwd))
        con.commit()
        return render(request, 'index.html',{'notredundant':True})
    else:
        return render(request, 'index.html', {'redundant':True})

def login(request):
    import sqlite3
    con=sqlite3.connect('D://Study Related//SEM 6//Mini Project//AMG//amg.db')
    cursorobj=con.cursor()

    emailid = request.POST.get('emailid')
    pwd = request.POST.get('pwd')

    data = cursorobj.execute('SELECT name FROM members WHERE email = ? AND pass = ?',(emailid, pwd))
    result = data.fetchall()
    if len(result) == 0:
        return render(request, 'index.html',{'invalid':True})
    else:
        return render(request, 'index2.html', {'valid':True, 'user':result[0][0]})