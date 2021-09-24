#!/usr/bin/env python3
import os, json, cgi, cgitb
import secret
from templates import login_page, secret_page
print("Content-type:text/html\r\n\r\n")
print("<title>Test CGI</title>")
print("<p>Hello World!</p>")

cookie = os.environ["HTTP_COOKIE"]
if cookie:
    cookie = dict(x.split("=") for x in cookie.split("; "))
    username = cookie["username"]
    password = cookie["password"]
    if username == secret.username and password == secret.password:
        print(secret_page(username, password))
else:
    print(login_page())
