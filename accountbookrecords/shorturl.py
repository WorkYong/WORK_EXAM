# import pyshorteners as ps
# import time
# from selenium   import webdriver


# # https://sites.google.com/a/chromium.org/chromedriver/downloads 
# # 크롬최신버전은 지원되지 않습니다. 버전 확인 유의 부탁드립니다.
# def shortUrl():
#     options = webdriver.ChromeOptions()
#     driver_path = '/' #현재 chromedriver Path 적어주세요.
#     driver = webdriver.Chrome(driver_path, options=options)
#     link = driver.current_url
    
#     sh = ps.Shortener()
#     short_url = (sh.tinyurl.short(link))
    
#     return print(short_url)

# shortUrl()