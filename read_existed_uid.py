#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 10:57:52 2021

@author: mac
"""



import csv
import os.path
import os

# initialize a set of existed rules
existed_uid = set()

# name of the keeper rules' file
keeper_rules_name = os.getcwd() + "/rules"

# load existed rules into a dict (keeper_rules_name)
rf = csv.DictReader(open(keeper_rules_name, encoding = 'utf-8'))

for i in rf:
    
    existed_uid.add(i['用户id'])
