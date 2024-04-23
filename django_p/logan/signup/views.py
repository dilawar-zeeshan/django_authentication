from django.shortcuts import render
import mysql.connector as sql

s1=''
s2=''
s3=''
s4=''
s5=''
# Create your views here.
def signact (request):
    global s1,s2,s3,s4,s5
    if request.method=="POST":
        m=sql.connect(host = "localhost", user='root', passwd='1101', database = 'logan')
        cursor = m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=='first_name':
                s1=value
            if key=='last_name':
                s2=value
            if key=='sex':
                s3=value
            if key=='email':
                s4=value
            if key=='password':
                s5=value
        c="insert into users values('{}','{}','{}','{}','{}')".format(s1,s2,s3,s4,s5)
        cursor.execute(c)
        m.commit()

    return render(request, 'signup_p.html')