import datetime
now=datetime.datetime.now()
mes=''
def MESSAGE(STATUS='Успешно',DATE='2021 года', day='13', mounth='Декабря',hour='16 часов',minute='15 минут',TEXT='Подписать служебку у начальника'):
    if mes=='Подписать служебку у начальника 13 декабря 2021 года в 16:15':
        print('Статус:',STATUS)
        print('Дата:',DATE,day,mounth,hour,minute)
        print('Напоминание:',TEXT)
    if mes!='Подписать служебку у начальника 13 декабря 2021 года в 16:15':
        print('Статус:Ошибка,неправильный ввод', )
    if mes=='':
        print('Сегодняшняя дата:',now)
MESSAGE()

