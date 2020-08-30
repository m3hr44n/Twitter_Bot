#***TWITTER BOT***#
#Required libraries
#pip3 install selenium for install selenium
#CODED BY m3hr44n
#https://github.com/m3hr44n

#ed = TwittBot('', '') ==> Replace your Twitter account ID and password


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwittBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self,hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_element_by_class_name('tweet')
            links = [elem.get_attribute('date-permalink-path')
                     for elem in tweets]
            print(links)
            
            for link in links:
                bot.get('https://twitter.com/' + links)   
                try:
                    bot.find_element_by_class_name('').click() 
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(60)

ed = TwittBot('', '')
ed.login()
ed.like_tweet('')
