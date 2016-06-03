from splinter import Browser

browser = Browser()
browser.visit('http://127.0.0.1:8000/admin/')
browser.fill('username', 'teste_1234')
browser.fill('password', '1234')
browser.find_by_value('Log in').click()

if browser.is_text_present('My Actions'):
    print "Logged"
else:
    print "Could not access"

browser.quit()