# Clash royale clan manager
# pull CSV from pixelcrux.com
# update excel file
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import time
from openpyxl import load_workbook
from openpyxl.styles import colors
from openpyxl.styles import Font, Color
from datetime import datetime


clan_tag = '22UQV98'
xpath_xlsx = "/html/body/div[1]/article/main/div[4]/section[1]/div/div[2]/div[3]/button[1]"
xpath_csv = "/html/body/div[1]/article/main/div[4]/section[1]/div/div[2]/div[3]/button[2]"
master_file = 'clash_nasty.xlsx'
date = datetime.today().strftime('%Y-%m-%d')
csv_file = clan_tag + '_' + date + '.csv'

king_levels_xpath = "/html/body/div[1]/article/main/div[4]/section[1]/div/div[2]/div[1]/section[1]/label[2]/div"
last_seen_xpath = "/html/body/div[1]/article/main/div[4]/section[1]/div/div[2]/div[1]/section[1]/label[3]/div"

king_levels_css = "#content > main > div:nth-child(4) > section.col-7.col-m-7 > div > div.module-body > div.row.checkbox-set > section:nth-child(1) > label(2)"
last_seen_css = "#content > main > div:nth-child(4) > section.col-7.col-m-7 > div > div.module-body > div.row.checkbox-set > section:nth-child(1) > label(3)"

checkbox_set_css = "#content > main > div:nth-child(4) > section.col-7.col-m-7 > div > div.module-body > div.row.checkbox-set > section:nth-child(1)"

print('configuring web driver...')
op = webdriver.ChromeOptions()
op.add_argument('headless')
op.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=op)
params = {'behavior': 'allow', 'downloadPath': r'C:\Users\nthomas3\Python\Projects\Clash Royale Clan Manager'}
driver.execute_cdp_cmd('Page.setDownloadBehavior', params)
driver.get("http://pixelcrux.com/Clash_Royale/Clan_Manager/App?tag="+clan_tag)

time.sleep(3)

print('checking that all data checkboxes are checked...')

checkboxes_span = driver.find_elements_by_class_name("checkbox-text")
checkboxes_input = driver.find_elements_by_css_selector("input[type='checkbox']")
#there is a mismatch in the number of checkboxes found by "checkbox-text", which is 6, and input[type='checkbox'], which is 9
for box in checkboxes_input[3::]:
    #print(box.is_selected())
    if box.is_selected():
        print('checkbox ' + str(checkboxes_input.index(box) - 3) + ' is checked')
    else:
        print('checkbox ' + str(checkboxes_input.index(box) - 3) + ' is not checked, checking box ' + str(checkboxes_input.index(box) - 3))
        checkboxes_span[checkboxes_input.index(box)-3].click()

    

print('attempting to download ' + csv_file + '...')
element = driver.find_element_by_xpath(xpath_csv)
# below isn't working for some reason...
# try:
#     element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, xpath_csv)))
# finally:
#     driver.quit()

element.click()

# wait for download complete
time.sleep(5)
print('closing web driver...')
driver.quit()

print('writing to ' + master_file + ' as new sheet: ' + date)
fontStyle = Font(name="Calibri", size=12, color=colors.BLACK)
book = load_workbook(master_file)
writer = pd.ExcelWriter(master_file, engine = 'openpyxl')
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
pd.read_csv(csv_file).to_excel(writer, sheet_name = date)

book.font = fontStyle
book.save(master_file)
writer.close()
print('done!')
