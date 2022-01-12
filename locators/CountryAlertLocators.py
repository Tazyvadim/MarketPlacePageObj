class CountryAlertLocators:
    #Может быть два вида title -> получать текст для дальнейшеней работы
    title_country = {'css': 'h1.modal-title'}
    #При определении страны
    access = {'css': '#amredirect-popup > div.buttons > button.action.action-primary.accept.choose-detected-country'}
    #При выпадании списка стран
    choise_country = {'css':'#amredirect-popup > div > h4'}
