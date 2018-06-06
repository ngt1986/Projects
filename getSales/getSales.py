#! python3
import bs4, requests, sys, webbrowser, pyperclip, time, pyexcel, openpyxl, os

from datetime import datetime
starttime=datetime.now()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.chdir('c:\\users\\nthomas3\\appdata\\local\\programs\\python\\python36-32\\work')

sys.argv #['getSales.py','Part Number','Range Start','Range End']
##if len(sys.argv)==1:
##    partNumber=pyperclip.paste()
if len(sys.argv)==2:
    partNumber=sys.argv[1]
elif len(sys.argv)==3:
    rangeStart=sys.argv[2]
elif len(sys.argv)==4:
    rangeStart=sys.argv[2]
    rangeEnd=sys.argv[3]
elif len(sys.argv)>4:
    print('Invalid Entry')
partNumber=str(partNumber)
#partNumber=100401409

#options added to change directory to download files to working directory (./work)
options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'C:/users/nthomas3/appdata/local/programs/python/python36-32/work'}
options.add_experimental_option('prefs', prefs)

def getSales(partNumber):
    browser=webdriver.Chrome(chrome_options=options)
    browser.get('http://onecat.oilfield.slb.com/saleshistory/main.aspx')
    elem=WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#dxgvQueries_DXDataRow9 > td:nth-child(1)')))
    elem.click()
    elem=WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID,'filter_@partnumber')))
    elem.send_keys(partNumber)
    elem=WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID,"linkSubmit")))
    elem.click()
    elem=WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID,"lbtnExport_xls")))
    elem.click()

getSales(partNumber)


filepath='C:/users/nthomas3/appdata/local/programs/python/python36-32/work/dxgvResults.xls'

#convert to xlsx and delete xls
def xls2xlsx(filepath):
    while not os.path.exists(filepath):
        time.sleep(1)
        if os.path.isfile(filepath):                  
            sheet=pyexcel.get_sheet(file_name=filepath, name_columns_by_row=0)
            xlsarray=sheet.to_array()
            sheet1=pyexcel.Sheet(xlsarray)
            sheet1.save_as("dxgvResults.xlsx") #saves workbook with sheet name as pyexcel sheet
            #delete the old (.xls) version
            os.unlink('dxgvResults.xls')
            #change filepath to new .xlsx version
            filepath='C:/users/nthomas3/appdata/local/programs/python/python36-32/work/dxgvResults.xlsx'
        else:
            raise ValueError("%s isn't a file!" %file_path)
    return filepath
    
filepath=xls2xlsx(filepath)

#extract Qty from column 8 of sheet
def getQty(filepath):
    Qty=0
    wb=openpyxl.load_workbook(filepath)
    sheet=wb['pyexcel sheet'] #from sheet1.save_as above (no longer called Sheet1)
    for i in range(2,sheet.max_row+1):
        Qty+=sheet.cell(i,8).value
    #delete file as now Qty has been obtained
    os.unlink(filepath)
    return Qty

Qty=getQty(filepath)
print(Qty)

print(datetime.now()-starttime)
input("press enter to continue: ")
