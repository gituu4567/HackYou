lang = "Русс"
a = input("Открыть файл(Y-N): ")
if a == "Y":
    print("HackYou.(V.OTTT)")
    print("*Progi*-Проги(5)")
    print("*Options*-Настройки и как пользоваться")
    print("Пример ввода комманды: Progi")
    print("")
    komm = input("ВВедите комманду: ");
if komm == "Progi":
    print("")
    print("Weeman(Фишинг страниц)")
    print("Пример ввода комманды: Progi")
    print("");
    pr = input("ВВедите комманду: ");
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
if enter == "Releng":
    print("Engl, Русс");
    print("Выберите язык")
    rl = input("Какой язык вы выбрали: ")
if rl == "Engl":
    print("ERROR001:This language is not supported"); 
if a == "N":
    print("Exit HackYou");
