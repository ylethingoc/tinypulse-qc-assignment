from datetime import datetime

get_token = "//button[contains(text(), 'Get Token')]"
request_token = "//input[@type='submit']"
login = "//button[@id='login-button']"
accept = "//button[@id='auth-accept']"

accept_page_text = "//h1[contains(text(), 'Spotify for Developers')]"

user = "//input[@name='username']"
password = "//input[@name='password']"

token_box = "//input[@id='oauth-input']"


user_textbox = "//input[@data-cucumber='input-login-email']"
passwd_textbox = "//input[@data-cucumber='input-login-password']"
continue_button = "//div[@data-cucumber='button-continue']"
signin_button = "//span[contains(text(), 'Sign in')]"

avatar_img = "//img[@alt='QC Automation']"
setting_icon = "//span[contains(text(), 'Settings')]/ancestor::div"
add_people_textbox = "//span[contains(text(), 'Add People')]"

first_name_textbox = "//input[@field='firstName' and @value='']"
last_name_textbox = "//input[@field='lastName' and @value='']"
email_textbox = "//input[@field='email' and @value = '']"
now = datetime.now()
dt_string = now.strftime("%Y-%m-%d")
start_day_textbox = "//input[@field='startDate' and @value='']"
date_picker = "//div[@data-value='{}']".format(dt_string)

add_people_button = "//div[@role='button']/span[contains(text(), 'Add People')]"
congratulations_text = "//div[contains(text(), 'Congratulations')]"

manager_dropdown_menu = "//span[contains(text(), 'Select')]/ancestor::div[@role='button']"
email_item = "//div[@class='select-email-item']"

error_text = "//div[contains(text(), \"can't be blank\")]"

