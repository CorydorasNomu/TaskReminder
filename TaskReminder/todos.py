# -*- coding: utf8 -*-
import sys
import const

todos = []
links = []

# Parse todo file
with open(const.PATH) as f:
    lines = f.readlines()
    for i in lines:
        if i.startswith(const.HEADER_TODO):
            todos.append(i.replace(const.HEADER_TODO, ''))
        if i.startswith(const.HEADER_TODO):
            links.append(i.replace(const.HEADER_LINK, ''))

def getTodos():
    return todos

def getLinks():
    return links