#!/usr/bin/python2

import requests, bs4

def makeNyaaUrl(query, page):
    return 

def nyaaSearch(query):
    rows = []
    pageRows = [None]*75
    p = 1
    while len(pageRows) == 75:
        url = makeNyaaUrl(query,p)