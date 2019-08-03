# -*- coding: utf8 -*-
import sys
import const

todos = []
links = []

# Parse todo file
with open(const.PATH, 'r', encoding = 'utf-8') as f:
    lines = f.readlines()
    for i in lines:
        if len(todos) >= const.SET_MAX or len(links) >= const.SET_MAX: break
        if i.startswith(const.HEADER_TODO):
            todos.append(i.replace(const.HEADER_TODO, ''))
        if i.startswith(const.HEADER_LINK):
            links.append(i.replace(const.HEADER_LINK, ''))

def getTodos():
    return todos

def getLinks():
    return links