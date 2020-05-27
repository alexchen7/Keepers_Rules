# -*- coding: utf-8 -*-
"""
Created on Mon May 11 16:54:58 2020

@author: asus
"""

import pandas as pd
import csv

# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 06:05:15 2020

@author: asus
"""
import pandas as pd

def convert_float(val):
    try:
        return float(val)
    except ValueError:
        print ('非数字输入，将保留文本格式')
        

def edit_rules(uid, para, val):
        
    uid = int(uid)    
    try:
        val =float(val)
    except ValueError:
        print ('非数字输入，将保留文本格式')
    
    df = pd.read_csv('rules')
    
    df.set_value(df.set_index('用户id').index.get_loc(uid), para, val)
    
    df.to_csv('rules', index=False)
    
    print ('已成功更改',uid,'的认领信息')

filename = 'rules'
with open(filename, 'a', newline = '', encoding = 'utf-8') as f:
    fieldnames = ['用户id', '最小单种体积', '最少总认领体积', \
		'最少总认领数', '最少做种时间', \
		'认领名次合格种子数比例', '认领名次合格种子数体积比例', \
		'认领名次魔力比例', '合格认领小组', '不合格认领分类', \
		'工资比例', '工资体积系数',	'工资种子寿命系数', \
		'工资做种时间系数', '工资做种人数系数', '最多允许同伴数', \
		'最少第一认领占体积比', '备注']
	
    thewriter = csv.DictWriter(f, fieldnames = fieldnames)
    existed_uid = set()
    # get all the existed uid in a set to aovid dup rules
    rf = csv.DictReader(open(filename, encoding = 'utf-8'))
    for i in rf:
        existed_uid.add(i['用户id'])