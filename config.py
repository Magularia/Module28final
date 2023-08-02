from faker import Faker

# Основной URL тестируемого сайта
URL = 'https://b2c.passport.rt.ru'

# Путь к вебдрайверу
# PATH = './chromedriver.exe'
PATH = "/Applications/chromedriver_mac64/chromedriver"

# Валидные данные для авторизации
valid_email = 'magularia@mail.ru'
valid_phone = '+79636321975'
valid_password = 'Magularia2!'

# Невалидные данные для авторизации
fake = Faker()
fake_password = fake.password()