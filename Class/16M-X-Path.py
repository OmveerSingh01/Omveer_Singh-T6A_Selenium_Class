'''
X-Path
Traversing :-
 1. Forward -> //div[] - when accessing from parent to child ; ex:- // or /
 2. Backward -> //input/.. when accessing from child to parent ; ex:- /..

 Steps:-
 1. Identify static element
 2. Move to common parent element for both static and dynamic element
 3. Fetch dynamic element

'''
from selenium.webdriver.common.by import By
from selenium.webdriver import Edge,EdgeOptions
o = EdgeOptions()
o.add_experimental_option('detach',True)
o.add_argument('--headless')
driver=Edge(options=o)

# driver.get('https://demoqa.com/webtables')
# salary = driver.find_element(By.XPATH,'//td[text()="Cantrell"]/../td[5]').text
# print(f'Salary is {salary}')

# driver.get('https://the-internet.herokuapp.com/tables')
# due = driver.find_element(By.XPATH,'//td[text()="Frank"]/../td[4]').text
# print(f'Due amount is {due}')

'''
Siblings :-
1. Following sibling
2. preceding sibling

//td['Dhurandhr']// following-sibling::td[2]
//td['Dhurandhr']// preceding-sibling::td[1]

'''
due_am = driver.find_element(By.XPATH,'//td[text()="Tim"]//following-sibling::td[2]')
print(f'Due amount is {due_am.text}')

