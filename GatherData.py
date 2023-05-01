import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options





def append_to_file(filename, text):
    with open(filename, 'a') as f:
        f.write(text + '\n')

def getText(driver, index, president):
    driver.get("https://millercenter.org/the-presidency/presidential-speeches")
    time.sleep(1)
    button = driver.find_element(By.CLASS_NAME, "form-checkboxes.bef-checkboxes")
    print(button.text)
    children = button.find_elements(By.CLASS_NAME, "option")
    click = children[index]
    driver.execute_script("arguments[0].click();", click)
    time.sleep(1)
    button = driver.find_element(By.CLASS_NAME, "views-infinite-scroll-content-wrapper.clearfix")
    children = button.find_elements(By.CLASS_NAME, "views-field.views-field-title")
    i =0
    for child in children:
        driver.execute_script("window.open(arguments[0], '_blank');", child.find_element(By.TAG_NAME, "a"))
        driver.switch_to.window(driver.window_handles[-1])
        try:
            click = driver.find_element(By.CLASS_NAME, "view-transcript-btn.top")
            click = click.find_element(By.TAG_NAME, "a")
            driver.execute_script("arguments[0].click();", click)
            transcript = driver.find_element(By.CLASS_NAME, "transcript-inner")
        except Exception as e:
            print(e)
            transcript = driver.find_element(By.CLASS_NAME, "view-transcript")
        text = transcript.find_elements(By.TAG_NAME, "p")
        for paragraph in text:
            print(paragraph.text)
            append_to_file("/Users/ahmedmoamen/Desktop/ahmed/work/Programming/python/NPL/USA presidential vocab/presidents/"+president+"_"+str(i)+".txt", paragraph.text)
        i = i+1
        print(i)
        print("\n\n\n\n\n")
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
def getAll(driver, friverpresidents):
    for key, value in presidents.items():
        if key > 25:
            try:
                getText(driver, key-1, value)
            except Exception as e:
                print(e)


chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
presidents = {
    1: 'George Washington',
    2: 'John Adams',
    3: 'Thomas Jefferson',
    4: 'James Madison',
    5: 'James Monroe',
    6: 'John Quincy Adams',
    7: 'Andrew Jackson',
    8: 'Martin Van Buren',
    9: 'William Harrison',
    10: 'John Tyler',
    11: 'James K. Polk',
    12: 'Zachary Taylor',
    13: 'Millard Fillmore',
    14: 'Franklin Pierce',
    15: 'James Buchanan',
    16: 'Abraham Lincoln',
    17: 'Andrew Johnson',
    18: 'Ulysses S. Grant',
    19: 'Rutherford B. Hayes',
    20: 'James A. Garfield',
    21: 'Chester A. Arthur',
    22: 'Grover Cleveland',
    23: 'Benjamin Harrison',
    24: 'William McKinley',
    25: 'Theodore Roosevelt',
    26: 'William Taft',
    27: 'Woodrow Wilson',
    28: 'Warren G. Harding',
    29: 'Calvin Coolidge',
    30: 'Herbert Hoover',
    31: 'Franklin D. Roosevelt',
    32: 'Harry S. Truman',
    33: 'Dwight D. Eisenhower',
    34: 'John F. Kennedy',
    35: 'Lyndon B. Johnson',
    36: 'Richard M. Nixon',
    37: 'Gerald Ford',
    38: 'Jimmy Carter',
    39: 'Ronald Reagan',
    40: 'George H. W. Bush',
    41: 'Bill Clinton',
    42: 'George W. Bush',
    43: 'Barack Obama',
    44: 'Donald Trump',
    45: 'Joe Biden'
}
def run():
    getAll(driver, presidents)
