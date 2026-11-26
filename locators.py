from selenium.webdriver.common.by import By


class RegistrationLocators:

    REG_NAME_FIELD = (By.XPATH, "//div[normalize-space(label)='Имя']/input")  #Поле ввода имени на странице регистрации
    REG_EMAIL_FIELD = (By.XPATH, "//div[normalize-space(label)='Email']/input")  #Поле ввода email на странице регистрации
    REG_PASSWORD_FIELD = (By.XPATH, "//div[normalize-space(label)='Пароль']/input")  #Поле ввода пароля на странице регистрации
    REG_BUTTON = (By.XPATH, "//button[normalize-space()='Зарегистрироваться']")  #Кнопка "Зарегистрироваться" на странице регистрации
    PASSWORD_ERROR_MESSAGE = (By.CSS_SELECTOR, "p.input__error.text_type_main-default")  #Сообщение о неверном пароле на странице регистрации
    REG_LOGIN_BUTTON = (By.CSS_SELECTOR, "a[href='/login']")  #Кнопка "Войти" на странице регистрации

class AuthorizationLocators:
    AUTH_FORM = (By.XPATH, "//main//h2[normalize-space()='Вход']")  #Название формы авторизации
    AUTH_EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/../input")  #Поле ввода email на странице авторизации
    AUTH_PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/../input")  #Поле ввода пароля на странице авторизации
    AUTH_BUTTON = (By.XPATH, "//main//button[normalize-space()='Войти']")  #Кнопка "Войти" на странице авторизации

class MainPageLocators:
    AUTH_ACC_BUTTON = (By.XPATH, "//main//button[normalize-space()='Войти в аккаунт']")  #Кнопка "Войти в аккаунт" на главной странице
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[normalize-space(text())='Оформить заказ']")  #Кнопка "Оформить заказ" на главной странице для авторизованного пользователя
    ACCOUNT_BUTTON = (By.CSS_SELECTOR, "a[href='/account']")  #Кнопка "Личный кабинет" на главной странице
    CONSTRUCT_BURGER = (By.XPATH, "//h1[normalize-space()='Соберите бургер']")  #Название формы конструктора бургера "Соберите бургер" на главной странице
    BUNS_BUTTON = (By.XPATH, "//span[normalize-space()='Булки']/..")  #Кнопка переключения на раздел "Булки" в конструкторе бургеров на главной странице
    SAUCE_BUTTON = (By.XPATH, "//span[normalize-space()='Соусы']/..")  #Кнопка переключения на раздел "Соусы" в конструкторе бургеров на главной странице
    FILLINGS_BUTTON = (By.XPATH, "//span[normalize-space()='Начинки']/..")  #Кнопка переключения на раздел "Начинки" в конструкторе бургеров на главной странице

class ForgotPasswordPageLocators:
    FORGOT_PASS_LOGIN_BUTTON = (By.CSS_SELECTOR, "a[href='/login']")  #Кнопка "Войти" на странице восстановления пароля

class AccountProfilePageLocators:
    PROFILE_BUTTON = (By.CSS_SELECTOR, "a[href='/account/profile']")  #Кнопка раздела "Профиль" на странице личного кабинета
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[normalize-space()='Конструктор']")  #Кнопка верхнего меню "Конструктор" на странице личного кабинета
    LOGO_SVG = (By.CSS_SELECTOR, 'svg[viewBox="0 0 290 50"]')  #Логотип-ссылка на странице личного кабинета
    EXIT_BUTTON = (By.XPATH, "//main//button[normalize-space()='Выход']")  #Кнопка "Выход" на странице личного кабинета
