# -*- coding:utf-8 -*-
import re
def person(name, age, sex, job):
    def walk():
        print("ok")

    data = {
        'name': name,
        'age': age,
        'sex': sex,
        'job': job,
        'walk': walk()
    }

    return data

a =person("hq",15,"男","程序员")
a["walk"]

