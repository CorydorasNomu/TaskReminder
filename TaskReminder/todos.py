# -*- coding: utf8 -*-
import sys
import const

todos = []
links = []

# TODOファイルの解析
with open(const.PATH, 'r', encoding = const.UTF_8) as f:
    lines = f.readlines()
    for i in lines:
        if len(todos) >= const.SET_MAX or len(links) >= const.SET_MAX: break
        if i.startswith(const.HEADER_TODO):
            contents = i.replace(const.HEADER_TODO, const.EMPTY)
            if contents != const.NEW_LINE:
                todos.append(contents)
        if i.startswith(const.HEADER_LINK):
            links.append(i.replace(const.HEADER_LINK, const.EMPTY))

def getTodos():
    return todos

def getLinks():
    return links