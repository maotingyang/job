#a) 請用 Python 寫出一個可以爬 ptt /reddit 任意看板（https://www.ptt.cc ）的爬蟲
# 程式，可以使用任意 Python 套件
# 以下欄位為必要
# • 日期
# • 作者
# • 標題
# • 內文
# • 看板名稱

# 我沒有PTT帳號，所以爬reddit
# 時間關係，我這題做不完，附上之前爬tripadviser的正負評給你參考

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()   #我用selenium，所以麻煩要下載chrome driver
driver.get(r"https://www.reddit.com/")

def crawler(target):  # 輸入哪一個領域，就抓下前十則資訊，我用Gaming版測試
    input = driver.find_element_by_id('header-search-bar')
    input.send_keys(target)
    input.send_keys(Keys.RETURN)
    time.sleep(3)   #睡眠，避免網頁還在載入就進入下一步
    driver.find_element_by_xpath(r'//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div[1]/div/a/div[1]/div/div[1]').click()   #進入gaming版，這裡用xpath
    time.sleep(3)
    the_list = driver.find_elements_by_class_name('SQnoC3ObvgnGjWt90zD9Z')   #每篇文章的標題
    data_dict = {'日期':"","作者":"","內文":"","標題":"","看板名稱":target}
    data_list = []
    for i in range(5):  #爬前五個
        print(i)
        the_list[i].click()
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        title = soup.select('h2')[0]        
        print(title.get_text())

        
        
crawler('Gaming')    