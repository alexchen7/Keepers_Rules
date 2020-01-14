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
        

def edit_rules():
    
    go_on = 1
    
    while go_on == 1:
    
    
        uid = int(input('请输入需要更改的uid:'))
        
        para = str(input('请输入需要更改的参数:'))
        
        val = input('请输入数值/文字')
        try:
            val =float(val)
        except ValueError:
            print ('非数字输入，将保留文本格式')
        
        df = pd.read_csv('rules')
        
        df.set_value(df.set_index('用户id').index.get_loc(uid), para, val)
        
        df.to_csv('rules', index=False)
        
        go_on = input('继续更改？输入1回车继续，否则任意输入...')
        if go_on.isdigit():
            go_on = int(go_on)
    