from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, nfactorial school!")


def add(request, first: int, second: int):
    res = first + second
    return HttpResponse(res)


def get_uppercase(request, text: str):
    return HttpResponse(text.upper())


def is_palindrome(request, text: str):
    res = False
    if text == text[::-1]:
        res = True
    return HttpResponse(res)


def calc(request, first: int, operation: str, second: int):
    res = 0
    sign = ""
    if operation == "add":
        res = first + second
        sign = "+"
    elif operation == "sub":
        res = first - second
        sign = "-"
    elif operation == "mult":
        res = first * second
        sign = "*"
    elif operation == "div":
        res = first / second
        sign = "/"
    return HttpResponse(f" {first} {sign} {second} = {res}")
