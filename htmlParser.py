from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


URL_ = 'file:///C:/Users/hp/Desktop/XAT21040273_2076O206S1D1112E1.html'
# https://cdn3.digialm.com//per/g21/pub/2076/touchstone/AssessmentQPHTMLMode1/2076O206/2076O206S1D1206/16100187639716741/XAT21038155_2076O206S1D1206E1.html
#URL = 'https://cdn3.digialm.com//per/g21/pub/2076/touchstone/AssessmentQPHTMLMode1/2076O206/2076O206S1D1112/16100186601443132/XAT21040273_2076O206S1D1112E1.html'
print('Enter Sheet URL')
URL = input()
page = requests.Session()
soup = bs(page.get(URL).text,'html.parser')
#print (soup)
questions = soup.find_all('td',{'style':'height: 25px;text-align: left;'})
#print(len(questions))
correct_ans = []
marked_ans = []
result = []
for question in questions :
    #print (type(question),type(questions))
    correct_ans.append(question.get('class')[0])
#print(correct_ans)
answers = soup.find_all('table',{'style':'float: right;margin-bottom: 5px;margin-top: 5px;width: 29%'})
#print(answers)
for ans in answers :
    temp = ans.findChildren('td',{'class':'bold'})
    marked_ans.append(temp[2].text)
#print(marked_ans)
count_correct = 0
count_wrong = 0
count_unattempted = 0
for i in range(len(marked_ans)-25) :
    if marked_ans[i] == ' -- ' :
        count_unattempted += 1
    elif correct_ans[i*5+int(marked_ans[i])-1] == 'rightAns':
        count_correct += 1
    else :
        count_wrong += 1
#print(count_correct,count_wrong,count_unattempted)
gk_correct = 0
gk_wrong = 0
gk_unattempted = 0
for i in range(len(marked_ans)-25,len(marked_ans)) :
    if marked_ans[i] == ' -- ' :
        gk_unattempted += 1
    elif correct_ans[i*5+int(marked_ans[i])-1] == 'rightAns':
        gk_correct += 1
    else :
        gk_wrong += 1
#print(gk_correct,gk_wrong,gk_unattempted)
creds = soup.find_all('table',{'style':'width:500px;'})[0]
dets = creds.findChildren('td')
name = dets[3].text

print('Candidate Name : '+ name)ca
print('Part I : :{:.2f}'.format(count_correct-count_wrong/4-(count_unattempted-8)/10))
print('Part II : {:.2f}'.format(gk_correct))
