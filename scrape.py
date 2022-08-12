from selenium import webdriver
import time
import pandas as pd

driver = webdriver.Chrome('chromedriver.exe')

ques = dict()
ques['Questions'] = []
link = '/html/body/div[1]/div/div/div[4]/div/div/div[2]/div/div/div[2]/div[{}]/div/div/div/span/a/div/div/div'

print('waiting...')
driver.get(r'https://www.quora.com/search?q=learning%20path')
time.sleep(10)
# file = open('Questions.txt','w')
count = 0

reset = 0
for i in range(1,1000):
    print(i)
    a = '/html/body/div[1]/div/div/div[4]/div/div/div[2]/div/div/div[2]/div[{}]/div/div/div/span/a/div/div/div'.format(str(i))
    try:
        f = driver.find_element_by_xpath(a).text
        # file.write(f)
        # file.write('/n')
        ques['Questions'].append(f)
        count+=1
        reset = 0
    except:
        reset+=1
        pass

    if reset==10:
        break
    
    if count%7==0:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(20)

df = pd.DataFrame(ques)
df.to_csv('Questions.csv',index=None)
print(count)