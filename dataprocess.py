# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 20:42:50 2021

@author: DADA1998
"""

import os
import pandas as pd
nstd_dir = r'C:\Users\DADA1998\Desktop\论文1\niot_nov16'
files = os.listdir(nstd_dir)
for file in files:
    if not os.path.isdir(file):
        path = os.path.join(nstd_dir, file)
        df = pd.read_excel(path, sheet_name='National IO-tables')
        need_code = ['C10-C12','C13-C15','C16','C17','C18','C19','C20','C21','C22','C23','C24','C25','C26','C27','C28','C29','C30','C31_C32','C33','II_fob','TXSP','EXP_adj','PURR','PURNR','VA','IntTTM','GO']
        need_cols = ['Year','Code','Description','Origin','C10-C12','C13-C15','C16','C17','C18','C19','C20','C21','C22','C23','C24','C25','C26','C27','C28','C29','C30','C31_C32','C33','CONS_h','CONS_np','CONS_g','GFCF','INVEN','EXP','GO'] 
        list_to_df = df[df['Code'].isin(need_code)]
        list_to_df = list_to_df[(need_cols)]
        list_to_df = list_to_df.groupby(by=['Year','Code'])['C10-C12','C13-C15','C16','C17','C18','C19','C20','C21','C22','C23','C24','C25','C26','C27','C28','C29','C30','C31_C32','C33','CONS_h','CONS_np','CONS_g','GFCF','INVEN','EXP','GO'].sum()
        list_to_df.to_csv(file.strip('.xlsx')+'_new.csv',index = 'Year')






# df=pd.read_excel(r'C:\Users\DADA1998\Desktop\论文1\niot_nov16\AUS_NIOT_nov16.xlsx',sheet_name='National IO-tables')#可以通过sheet_name来指定读取的表单

# need_code = ['C10-C12','C13-C15','C16','C17','C19','C20','C21','C22','C23','C24','C25','C26','C27','C28','C29','C30','C31_C32','C33','II_fob','TXSP','EXP_adj','PURR','PURNR','VA','IntTTM','GO']
# need_cols = ['Year','Code','Description','Origin','C10-C12','C13-C15','C16','C17','C19','C20','C21','C22','C23','C24','C25','C26','C27','C28','C29','C30','C31_C32','C33','CONS_h','CONS_np','CONS_g','GFCF','INVEN','EXP','GO'] 

# list_to_df = df[df['Code'].isin(need_code)]

# list_to_df = list_to_df[(need_cols)]
# # list_to_df.to_csv(file.strip('.xlsx')+'new',sep=',',columns = need_cols)

# list_to_df.to_csv(file.strip('.xlsx')+'new.csv',index = None)

# list_to_df = list_to_df.groupby(by=['Year','Code'])['C10-C12','C13-C15','C16','C17','C19','C20','C21','C22','C23','C24','C25','C26','C27','C28','C29','C30','C31_C32','C33','CONS_h','CONS_np','CONS_g','GFCF','INVEN','EXP','GO'].sum()
# list_to_df.to_csv(file.strip('.xlsx')+'new.csv',index = 'Year')