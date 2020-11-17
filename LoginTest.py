from selenium import webdriver

def file(data_file):
    try:
        data=[]
        file = open(data_file, 'r')
        for line in file:
            tmp = line.split(';')
            tmp=[tmp[0],tmp[1]]
            data.append(tmp)
        file.close()
        return data

    except FileExistsError:
        print("Hiányzó fájl.")

def login(browser, link):
    try:
        browser.get(link)
        browser.implicitly_wait(10)
        browser.maximize_window()
    except Exception:
        print("Hiba a böngésző betőltése során. -> login()")

def success_login(browser, email_target, password_target, file_1):

    try:
        for i in range(len(file(file_1))):
            browser.find_element_by_name(email_target).send_keys(file(file_1)[i][0])
            browser.find_element_by_name(password_target).send_keys(file(file_1)[i][1])
            browser.find_element_by_name("login").click()
            browser.find_element_by_link_text('Kijelentkezés').click()
        print("1: eset: Érvényes email és jelszó, a bejelentkezés sikeres.")

    except Exception:
        print("1. eset: Hiba a sikeres bejelentkezés során. -> success_login()")

def login_with_wrong_password(browser, email_target, password_target, file_2):

    try:
        for i in range(len(file(file_2))):
            browser.find_element_by_name(email_target).send_keys(file(file_2)[i][0])
            browser.find_element_by_name(password_target).send_keys(file(file_2)[i][1])
            browser.find_element_by_name("login").click()
        print("2. eset: Érénytelen jelszó, sikertelen bejelentkezés.")
    except Exception:
        print("2. eset: Hiba az étvénytelen jelszó tesztelése során. -> login_with_wrong_password")

def login_with_wrong_email_and_wrong_password(browser, email_target, password_target, file_3):
    try:
        for i in range(len(file(file_3))):
            browser.find_element_by_name(email_target).send_keys(file(file_3)[i][0])
            browser.find_element_by_name(password_target).send_keys(file(file_3)[i][1])
        browser.find_element_by_name("login").click()
        print("3. eset: A felhasználó nem szerepel az adatbázisban, sikertelen bejelentkezés.")
    except Exception:
        print ("3. eset: Hiba az érvénytelen email és jelszó tesztelése során. -> login_with_wrong_email_and_w_password()")

def login_with_wrong_email(browser, email_target, password_target, file_4):
    try:
        for i in range(len(file(file_4))):
            browser.find_element_by_name(email_target).send_keys(file(file_4)[i][0])
            browser.find_element_by_name(password_target).send_keys(file(file_4)[i][1])
            browser.find_element_by_name("login").click()
        print ("4. eset: Érvénytelen email cím, sikertelen bejelentkezés.")
        browser.close()

    except Exception:
        print("4. eset: Hiba az érvénytelen jelszó tesztelése során. -> login_with_wrong_email()")

def main():
    browser=webdriver.Firefox()

    #a teszt adatok változói
    link="http://127.0.0.1:8000"
    email_target="email"
    password_target="password"
    file_1="eset_1.csv"
    file_2="eset_2.csv"
    file_3="eset_3.csv"
    file_4="eset_4.csv"


    login(browser, link) #böngésző megnyitása

    #teszt esetek futtatása
    success_login(browser, email_target, password_target, file_1)
    login_with_wrong_password(browser, email_target, password_target, file_2)
    login_with_wrong_email_and_wrong_password(browser, email_target, password_target, file_3)
    login_with_wrong_email(browser, email_target, password_target, file_4 )


main()
