from django.shortcuts import render
import mysql.connector as sql


s4=''
s5=''
# Create your views here.
def logact (request):
    global s4,s5
    if request.method=="POST":
        m=sql.connect(host = "localhost", user='root', passwd='1101', database = 'logan')
        cursor = m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=='email':
                s4=value
            if key=='password':
                s5=value
        c="SELECT * from users where email='{}' and pswd ='{}'".format(s4,s5)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render (request, 'error.html')
        else:
            return render (request, 'welcome.html')

    return render(request, 'login_p.html')