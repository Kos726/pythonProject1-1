list_check_end = [".com", "ru", ".net"]                 # доменов может быть больше, поэтому создаем список,
                                                        # которым потенциально можно управлять отдельно.
email_default = 'university.help@gmail.com'             # заведем адрес по умолчанию как переменную.

# в задании (п.2) сказано "Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net".
# Таким образом нужно проверить на наличие ошибок оба адреса.
# Поэтому создаем отдельную функцию, в которой будет проверяться один или два разных адреса.
def check_email_(email_):
    check_a = email_.find('@')                          # проверяем на наличие "@", функция возращяет "-1",
                                                        # если значение не найдено, т.е. будет "<0"
    i = 0                                               # вспомогательная переменная
    len_list = len(list_check_end)                      # считаем количество доменов в списке проверки
    check_end = 0                                       # вспомогательная переменная для пробегания по списку доменов
    for i in range(len_list):                           # перебор на совпадение домена и наличия "@"

        check_end = check_end + email_.endswith(list_check_end[i])  # количество сопадений доменов:
                                                                    # т.к. всегда один из множества
                                                                    # доменов должен совпасть, то всегда будет "1"
    if check_a < 0 or int(check_end) < 1:               # условие совпадения "@" и домена
        error_ = True                                   # возврат True, если есть ошибки
    else:
        error_ = False                                  # возврат False, если ошибок нет
    return error_

# создаем функцию проверки условий
def send_email(message, recipient, *, sender = email_default):
    if check_email_(sender) == True or check_email_(recipient) == True:     # условие совпадения "@" и домена адресов
        print(f'Невозможно отправить письмо с адреса <{recipient}> на адрес <{sender}>')
    elif recipient == sender:                                               # проверка совпадения адресов
        print(f'Нельзя отправить письмо самому себе!')
    elif sender == email_default:                                           # проверка на соответсвие почты по умолчанию
        print(f'Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>.')

send_email('Это сообщение для проверки связи',
           'vasyok1337@gmail.com')
print()
send_email('Вы видите это сообщение как лучший студент курса!',
           'urban.fan@mail.ru',
           sender ='urban.info@gmail.com')
print()
send_email('Пожалуйста, исправьте задание',
           'urban.student@mail.ru',
           sender ='urban.teacher@mail.uk')
print()
send_email('Напоминаю самому себе о вебинаре',
           'urban.teacher@mail.ru',
           sender ='urban.teacher@mail.ru')
