import pandas as pd
import openpyxl
plan=pd.read_excel('effectivecopy.xlsx')

def importer():
        #print(plan)
        title_array=plan['Title'].tolist()
        #content_array=plan['Content'].tolist()
        #ID=plan['ID'].tolist()

        #for drive in range (limit):
        
         #       print (f"Title Prompt= {title_array[drive]}")          
        return title_array

def exporter(response):
        response_df=pd.DataFrame(
                data=response,
                columns=['response'])
        print (response_df)
        with pd.ExcelWriter('plan.xlsx', mode='a') as writer:
                response_df.to_excel(writer,sheet_name='Response',index=False)


#print (plan)
