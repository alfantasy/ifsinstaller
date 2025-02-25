import json

translations = {
    'ru': {
        "help_message": '''Первый параметр в начальном меню "Скачивание и установка необходимых программ (онлайн):
    - Скачивает по скаченной заранее (и/или самой программой) конфигурации программы и устанавливает. 
    - Все ссылки и аргументы уже прописаны.
Второй параметр в начальном меню "Установка программ из пакета PE IFS (оффлайн)":
    - Предполагает, что скачен пакет программ PE (PostInstallation Environment) от InfoSecurity. 
    - Все аргументы и пути также будут прописаны.
    - Скачать его можно по ссылке ниже.

Описание настроек программы:
1. Изменить язык - позволяет поменять язык с русского на английский и наоборот.
2. Обновить файл конфигурации - ручное обновление файла конфигурации.
3. Включить/Отключить автоматическое обновление файла конфигурации - позволяет заведомо обновлять конфигурацию, а при отключении - не использовать параметр -noUpdate
4. Обновление файла переводчика - необходимо для корректного вывода всех текстовых значений.
5. Включить/Отключить этапы установки - позволяет отключить диалог этапов установки, сведя этапы до минимума (автоматизм).
''',
        "help_message_warning": " Внимание!",
        "help_message_warning0": "      Может быть, что программа не даст выйти при вводе 0 (редкие случаи, но все же), поэтому нажмите просто CTRL+C для принудительного завершения.",
        "help_message_title": "Help. Справка о использовании скрипта",
        "for_escape": "Для выхода, нажмите Enter",
        "online_install_programs_main": '''Выберите категорию скачиваемого ПО:
1: Браузеры
2: Архиваторы
3: Текстовые редакторы и IDE
4: Медиаплееры
5: Аудиопроигрыватели


0: Назад''',
        "types": 'Ввод...',
        "wrong_choice": "Неверный выбор. Пожалуйста, выберите снова...",
        "contenter": "Нажмите Enter, чтобы продолжить...    ",
        "select_program": "Выберите необходимую Вам программу:",
        "back": "0: Назад",
        "error_conf0": "Ошибка конфигурационного файла. Невозможно захватить никакую из существующих программ данной категории.",
        "error_conf1": "Возможно, нет установленных программ данной категории. Нажмите Enter, чтобы продолжить...",
        "menu": '''Выберите необходимый параметр:
1: Скачивание и установка необходимых программ (онлайн)   
2: Установка программ из пакета PE IFS (оффлайн)        
3: Справка
4: Настройки программы
          
0: Выйти      
''',
        "thanks_usage": "Спасибо за использование IPPE by IFS! <3",
        "help_console": '''используйте ifs -<параметр> -<второй параметр>
    -help, -h - вывод справки о параметрах и команды ifs
    -noUpdate - запуск программу без обновления файла конфигурации.
    -oInstall - авто-переход в программу онлайн-инсталляции
    -ofInstall - авто-переход в программу оффлайн-инсталляции       
        -noPacketScan - отключение сканирование пакета      
    -packetScan - сканирование на наличие оффлайн пакета программ 
              
Важно! Нельзя сочетать одинаковые параметры.\nПримеры использования команды:
    ifs -oInstall -noUpdate
    ifs -ofInstall -noUpdate
    ifs -ofInstall -noUpdate -noPacketScan
              
При переходе в режим оффлайн-инсталляции, сканирование происходит автоматически, но параметр -packetScan сканирует при запуске и в дальнейшем не будет требоваться (при переходе).              
''',
        "help_console0": 'Нажмите любую кнопку для выхода...',
        "off_update": "Вы отключили автообновление конфигурации.",
        "upload_conf": "Подгружаем конфигурацию при наличии интернет-соединения...",
        "launch_script": "Запускаем программу инсталляции...",
        "load_config": "Автозахват файла конфигурации",
        'error_load_config0': 'Внимание! Файл конфигурации "config.json" не найден!',
        'error_load_config1': 'Если Вы использовали параметр -noUpdate, и у Вас нет файла конфигурации, онлайн-инсталляция работать не будет! \nСкачайте файл конфигурации через меню, либо перезапустите приложения без параметра -noUpdate',
        "settings_title": "Настройки программы. Редактируйте внимательно!",
        "settings_text_main": '''Выберите, что нужно сделать:
1: Изменить язык
2: Обновить файл конфигурации
3: Включить/Отключить автоматическое обновление файла конфигурации
4: Обновление файла-переводчика.
5: Включить/Отключить этапы установки


0: Назад
''',
        "choice_lang": 'Выберите язык: 1. RU; 2.EN\n',
        "complete_upload_conf": "Обновление конфигурации закончено. Нажмите любую кнопку...",
        "complete_enable_conf": "Автоматическое обновление конфигурации включено. Нажмите любую кнопку...",
        "complete_disable_conf": "Автоматическое обновление конфигурации выключено. Нажмите любую кнопку...",
        "complete_update_trans": "Файл перевода обновлен. Нажмите любую кнопку...",
        "step1_to_install": "Начинаем скачивать программу: ",
        "step1.0_to_install": "Установщик загружен.",
        "step2_to_install": "Подтвердите аргументы установки: ",
        "step2.0_to_install": "Если аргументом установки является /None, значит конфигурация не предусматривает их.",
        "step2.0.1_to_install": "Если нужно запустить без аргументов установки, введите quick",
        "step2-confirm_to_install": "Введите Д (Y), чтобы подтвердить. Н (N), чтобы отклонить аргументы и ввести свои.",
        "step2.1_to_install": "Введите свои аргументы установки: ",
        "step2.1.0_to_install": "Подтвердите аргументы установки: ",
        "step2.1.1_to_install": "Если аргументы не нужны, поставьте /None или exit, чтобы выйти из установки",
        "step2.1.0-confirm_to_install": "Подтвердите введенные Вами аргументы. Выберите, Д (Y) или Н (N)?",
        "step3_to_install": "Подтвердите, точно ли нужно установить данное приложение? Введите 'да', либо 'yes' или 'нет', либо 'no'",
        "step4_cancel_install": "Установка была отклонена пользователем. Нажмите любую кнопку для возвращения...",
        "step5_to_install_complete": "Установщик запущен или установка уже была завершена... Чтобы вернуться на главную, нажмите любую кнопку...",
        "step0_error": "IPPE выдал ошибку. Пожалуйста, попробуйте ещё раз...",

        "complete_disable_steps": "Этапы установки отключены.",
        "complete_enable_steps": "Этапы установки включены.",

        "save_config": "Настройки успешно сохранены автоматически.",

        "coming_soon": "Скоро выйдет... Следите за обновлениями в Telegram канале: @ainfsy",

        "wrong_argument": "Неправильны указаны параметры. Вы ввели: ",
        "wrong_argument0": "Проверьте введенные параметры, если нужна справка введите ifs -h",
    },
    "en": {
        "help_message": '''The first option in the initial menu is "Download and install necessary programs (online):
    - Downloads according to the program configuration downloaded in advance (and/or by the program itself) and installs.               
    - All the links and arguments are already written out.
The second parameter in the initial menu, "Installing programs from the PE IFS package (offline)":
    - Suggests that the PE (Post Installation Environment) software package for information security has been downloaded. 
    - All arguments and paths will also be spelled out.
    - You can download it from the link below.

Description of the program settings:
1. Change the language - allows you to change the language from Russian to English and vice versa.
2. Update the configuration file - manually update the configuration file.
3. Enable/Disable automatic updating of the configuration file - allows you to update the configuration deliberately, and when disabled, do not use the -noUpdate parameter.
4. Updating the translator file is necessary for the correct output of all text values.
5. Enable/Disable installation steps - allows you to disable the installation steps dialog, reducing the steps to a minimum (automatism).    
''',
        "help_message_warning": " Warning!",
        "help_message_warning0": "      It may be that the program will not allow you to exit when you enter 0 (rare cases, but still), so just press CTRL+C to force termination.",
        "help_message_title": "Help. Help on using the script",
        "for_escape": "To exit the help, type Enter",
        "online_install_programs_main": '''Select the category of the downloaded software:
1: Browsers
2: Archivers
3: Text editors and IDEs
4: Media Players
5: Audio players


0: Back
''',
        "types": 'Type...',
        "wrong_choice": "Wrong choice. Please select again...",
        "contenter": "Press Enter to continue...    ",
        "select_program": "Select the program you need:",
        "back": "0: Back",
        "error_conf0": "Configuration file error. It is not possible to capture any of the existing programs in this category.",
        "error_conf1": "There may be no installed programs in this category. Press Enter to continue...",
        "menu": '''Select the required parameter:
1: Download and install necessary programs (online)   
2: Installing programs from the PE IFS package (offline)        
3: Help
4: Program Settings
          
0: Exit
''',
        "thanks_usage": "Thanks for using IPPE by IFS! <3",
        "help_console": '''usage ifs -<option> -<second option>
    -help, -h - output of the parameter help and the ifs command
    -noUpdate - running the program without updating the configuration file.
    -oInstall - auto-switch to the online installation program
    -ofInstall - auto-switch to the offline installation program    
        -noPacketScan - disable packet scanning
    -packetScan - scanning for offline software package
                  
Important! You can't combine the same parameters. Examples of using the command with options (parameters):
    ifs -oInstall -noUpdate
    ifs -ofInstall -noUpdate
    ifs -ofInstall -noUpdate -noPacketScan                  
    Usage without options: 
        ifs
                  
When switching to offline installation mode, scanning occurs automatically, but the -packetScan option scans at startup and will not be required in the future (during the transition).               
''',
        "help_console0": "Press any button to close it...",
        "off_update": "You have disabled the automatic configuration update.",
        "upload_conf": "Load the configuration if there is an Internet connection...",
        "launch_script": "Launching the installation program...",
        "load_config": "Auto-capture of the configuration file",
        "error_load_config0": "Attention! The configuration file \"config.json\" was not found!",
        "error_load_config1": "If you have used the -noUpdate option and you do not have the configuration file, the online installation will not work! \nDownload the configuration file from the menu, or restart the applications without the -noUpdate parameter.",
        "settings_title": "Program settings. Edit carefully!",
        "settings_text_main": '''Choose what you need to do:
1: Change the language
2: Update the configuration file
3: Enable/Disable automatic updating of the configuration file
4: Updating the translator file.
5: Enable/Disable the installation steps


0: Back
''',
        "choice_lang": "Select a language: 1.RU; 2. EN\n",
        "complete_upload_conf": "The configuration update is finished. Press any button...",
        "complete_enable_conf": "The configuration update is enabled. Press any button...",
        "complete_disable_conf": "The configuration update is disabled. Press any button...",
        "complete_update_trans": "The translation file has been updated. Press any button...",
        "step1_to_install": "Launching the download of the program: ",
        "step1.0_to_install": "The installer is downloaded.",
        "step2_to_install": "Confirm installation arguments: ",
        "step2-confirm_to_install": "Enter Y to confirm. N to reject the arguments and enter your own.",
        "step2.0_to_install": "If the installation argument is /None, then the configuration does not provide for them.",
        "step2.0.1_to_install": "If you want to run without installation arguments, enter quick",
        "step2.1_to_install": "Enter your installation arguments: ",
        "step2.1.0_to_install": "Confirm the installation arguments: ",
        "step2.1.0-confirm_to_install": "Confirm the arguments you entered. Type, Y or N?",
        "step2.1.1_to_install": "If arguments are not needed, set /None or exit to exit the installation",
        "step3_to_install": "Can you confirm if you need to install this application correctly? Enter 'yes' (D, d) or 'no' (N, n)",
        "step4_cancel_install": "The installation was rejected by the user. Press any button to return...",
        "step5_to_install_complete": "The installer is running or the installation has already been completed... To return to the main page, press any button...",
        "step0_error": "IPPE returned an error. Please try again...",
        "save_config": "The settings were saved successfully automatically.",
        "complete_disable_steps": "The steps installation are disabled. Press any button...",
        "complete_enable_steps": "The steps installation are enabled. Press any button...",

        "coming_soon": "It's coming out soon... Follow the updates in the Telegram channel: @ainfsy",

        "wrong_argument": "The parameters are specified incorrectly. You have entered:",
        "wrong_argument0": "Check the entered parameters, if you need help, enter ifs -h",
    }
}

with open('translation.json', 'w+', encoding='UTF-8') as f:
    f.write(json.dumps(translations, ensure_ascii=False, sort_keys=True, indent='\t', separators=(',', ': ')))
