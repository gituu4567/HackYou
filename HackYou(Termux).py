lang = "Русс"
#open file?
#открыть файл?
a = input("Открыть файл(Y-N): ")
#Menu HackYou
#Меню HackYou
if a == "Y":
    print("HackYou.(V.OTTT)")
    print("*Progi*-Проги(5)")
    print("*Options*-Настройки и как пользоваться")
    print("Пример ввода комманды: Progi")
    print("")
    komm = input("ВВедите комманду: ");
if komm == "Progi":
    print("")
    print("Zphisher(Фишинг страниц)")
    print("NGROK(Нужен для фишинга)")
    print("Instashell(Брутфуст страниц инстаграмма)")
    print("Пример ввода комманды: Progi")
    print("");
    pr = input("ВВедите комманду: ");
#all programs
#все программы
if pr == "Zphisher":
    print("git clone https://github.com/htr-tech/zphisher")
if pr == "Instashell":
    print("Git clone https://github.com/maxrooted/instashell")
#Menu options
#Меню настроек
if komm == "Options":
    print("Скрипт-программа `HackYou` для `Termux`");
    print("Язык(Language): " + lang);
    releng = print("(Releng)Изменить язык")
    enter = input("Напишите `Exit` для того что-бы вернуться: ");
if enter == "Exit":
    print("HackYou.(V.OTTT")
    print("*Progi*-Проги(5)")
    print("*Options*-Настройки и как пользоваться")
    print("Пример ввода комманды: Progi")
    print("")
#edit language
#изменить язык
if enter == "Releng":
    print("Engl, Русс");
    print("Выберите язык")
    rl = input("Какой язык вы выбрали: ")
if rl == "Engl":
    print("ERROR001:This language is not supported");
#exit to programms
#выход из программы
if a == "N":
    print("Exit HackYou");
