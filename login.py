#!/usr/bin/env python3
import os, json, cgi, cgitb
import templates, secret
print("<title>Test CGI Login</title>")

form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')

if username == secret.username and password == secret.password:
    print("Set-Cookie:username = {};".format(username))
    print("Set-Cookie:password = {};".format(password))
    print("Content-type:text/html\r\n\r\n")
    print(templates.secret_page(username, password))
else:
    print(templates.after_login_incorrect())
