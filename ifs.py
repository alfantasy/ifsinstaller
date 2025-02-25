import sys
import wget
import time
import json
import os
from colorama import init
from loguru import logger
import subprocess
import asyncio
logger.remove()
logger.add('file.log', format='{time:DD-MM-YYYY HH:mm:ss} {level} {message}', retention='2 days', rotation='2 MB', colorize=True)

tags = {'info': '[IPPE-INFO]', 'debug': '[IPPE-DEBUG]', 'error': '[IPPE-ERROR]', 'warning': '[IPPE-WARNING]'}

os.system('title Installer PE')

if os.path.exists("translation.json"):
    with open("translation.json", "r", encoding='UTF-8') as f:
        content_translate = f.read()
        data_translation = json.loads(content_translate)
else:
    wget.download("https://raw.githubusercontent.com/alfantasy/ifsinstaller/refs/heads/main/translation.json", "translation.json")
    with open("translation.json", "r", encoding='UTF-8') as f:
        content_translate = f.read()
        data_translation = json.loads(content_translate)    

os.system("cls")

def t(key):
    lang = settings['language']
    return data_translation.get(lang, {}).get(key, key)       

def update_conf():
    global config
    print(f"{qe}42m" + "======================= " + t("upload_conf") + " =======================")
    os.remove('config.json')
    wget.download(url_cfg_up, 'config.json')
    time.sleep(1)
    with open('config.json', 'r') as f:
        content = f.read()
        config = json.loads(content)
    print('\n' + f'{qe}97m' + t("complete_upload_conf"))
    a = input('')
    return a      

if os.path.exists('settings.json'):
    logger.info(f'{tags["info"]} Файл настроек IPPE в наличии. Продолжаем запуск.')
    with open('settings.json', 'r') as f:
        content0 = f.read()
        settings = json.loads(content0)
else:
    logger.info(f'{tags["info"]} Файла настроек IPPE нет. Создаем базовую конфигурацию файла настроек.')
    settings_json_base = {
        "language": "en",
        "autoupdate_conf": "yes",
        "dont_steps": "no",
    }
    with open('settings.json', 'w+') as f:
        f.write(json.dumps(settings_json_base, sort_keys=True, indent='\t', separators=(',', ': ')))
    with open('settings.json', 'r') as f:
        content0 = f.read()
        settings = json.loads(content0)        

qe = '\033['

clear = lambda: os.system('cls')
url_cfg_up = "https://raw.githubusercontent.com/alfantasy/ifsinstaller/refs/heads/main/config.json"

init(autoreset=True)

def save_settings():
    try:
        with open('settings.json', "w+") as f:
            f.write(json.dumps(settings, sort_keys=True, indent='\t', separators=(',', ': ')))
        return True
    except:
        logger.exception(f'{tags["error"]} Ошибка при сохранении файла настроек IPPE.')
        return False

def help():
    clear()
    print('\033[34m' + '======================= Installer Program PE by InfoSecurity =======================')
    print('\033[36m' + f'========================= {t("help_message_title")} =========================')
    print(t('help_message'))
    print('\033[36m' + '')
    print('\033[34m' + t('help_message_warning'))
    print('\033[32m' + t('help_message_warning0'))
    print('\033[36m' + f'========================= {t("help_message_title")} =========================')
    print('\033[34m' + '======================= Installer Program PE by InfoSecurity =======================')
    choice = input('\033[97m' + t('for_escape'))
    if choice == '' or choice == None or choice != '':
        menu()

def offline_install_programs():
    clear()
    print('\033[34m======================= Installer Program PE by InfoSecurity - Offline =======================')
    print('')
    print(f'{qe}94m{t("coming_soon")}')
    print('')
    print('\033[34m======================= Installer Program PE by InfoSecurity - Offline =======================')
    choice = input(t('contenter'))
    if choice == '' or choice == None or choice != '':
        menu()

def online_install_programs():
    clear()
    print('\033[34m======================= Installer Program PE by InfoSecurity - Online =======================')
    print(t('online_install_programs_main'))
    print('\033[34m======================= Installer Program PE by InfoSecurity - Online =======================')
    choice = input('\033[97m' + t('types'))
    if choice == '0':
        menu()
    if choice == '1':
        select_category_online('browsers')
    elif choice == '2':
        select_category_online('archiver')
    elif choice == '3':
        select_category_online('text_editor')
    elif choice == '4':
        select_category_online('media_player')
    elif choice == '5':
        select_category_online('audio_player')
    else:
        try:
            print('\033[41m' + t("wrong_choice"))
            choice = input('\033[97m' + t("contenter"))           
            if choice == '' or choice == None or choice != '':
                online_install_programs()     
        except ValueError:
            logger.info(f'{tags["info"]} Внезапность неправильного ключа.')
            logger.exception(f'{tags["error"]} Вывод исключения.')

def step_1_install(url, name, args):
    print(f'{qe}94m ' + t("step1_to_install") + f' {name}')
    wget.download(url, 'installer.exe')
    print(f'\n{qe}94m ' + t("step1.0_to_install"))
    print(f'{qe}94m ' + t("step2_to_install") + args)
    print(f'{qe}94m ' + t("step2.0_to_install"))
    step_choice = input(f'{qe}96m ' + t("step2-confirm_to_install") + ' ')
    if 'д' in step_choice.lower() or 'y' in step_choice.lower():
        try:
            step_3_install(name, args)
        except:
            logger.exception(f'{tags["error"]} Не получилось запустить процесс установки.')
            step_choice = input(f"{qe}96m {t('step0_error')} {t('contenter')}")
            if step_choice == '' or step_choice == None or step_choice != '':
                online_install_programs()            
            return
    elif 'н' in step_choice.lower() or 'n' in step_choice.lower():
        step_2_install(name, args)
    else:
        step_choice = input(f'{qe}96m ' + t("step2-confirm_to_install") + ' ')

def step_2_install(name, args):
    print(f'\n{qe}94m ' + t("step2.1.1_to_install"))
    step_choice = input(f'{qe}96m ' + t("step2.1_to_install"))
    if 'exit' in step_choice.lower():
        online_install_programs()
    else:
        if step_choice != '':
            arguments = step_choice
            step_choice = input(f'{qe}94m {t("step2.1.0_to_install")} {arguments} {qe}96m\n {t("step2.1.0-confirm_to_install")}     ')
            if 'д' in step_choice.lower() or 'y' in step_choice.lower():
                try:
                    step_3_install(name, arguments)
                except:
                    logger.exception(f'{tags["error"]} Не получилось запустить процесс установки.')
                    step_choice = input(f"{qe}96m {t('step0_error')} {t('contenter')}")
                    if step_choice == '' or step_choice == None or step_choice != '':
                        online_install_programs()                    
                    return
            elif 'n' in step_choice.lower() or 'н' in step_choice.lower():
                step_2_install(name, args)
            else:
                step_2_install(name, args)

def step_3_install(name, args):
    step_choice = input(f'{qe}96m ' + t("step3_to_install") + ' ')
    if 'д' in step_choice.lower() or 'y' in step_choice.lower():
        if '/none' in args.lower():
            subprocess.call("installer.exe")
        else:
            subprocess.call(f"installer.exe {args}")
        time.sleep(2)
        os.remove('installer.exe')
        step_choice1 = input(f'{qe}96m {t("step5_to_install_complete")}')                    
        if step_choice1 == '' or step_choice1 == None or step_choice1 != '':
            online_install_programs()    
    elif 'н' in step_choice.lower() or 'n' in step_choice.lower():
        step_choice = input(f'{qe}96m {t("step4_cancel_install")}' + ' ')
        if step_choice == '' or step_choice == None or step_choice != '':
            online_install_programs()
    else:
        try:
            step_3_install(name, args)
        except:
            logger.exception(f'{tags["error"]} Не получилось запустить процесс установки.')
            step_choice = input(f"{qe}96m {t('step0_error')} {t('contenter')}")
            if step_choice == '' or step_choice == None or step_choice != '':
                online_install_programs()
            return 

def nosteps_install(url, name, args):
    print(f'{qe}94m ' + t("step1_to_install") + f' {name}')
    wget.download(url, 'installer.exe')
    print(f'\n{qe}94m ' + t("step1.0_to_install"))
    print(f'{qe}94m ' + t("step2_to_install") + args)
    print(f'{qe}94m ' + t("step2.0_to_install"))
    step_choice = input(f'{qe}96m {t("step3_to_install")}' + ' ')
    if 'д' in step_choice.lower() or 'y' in step_choice.lower():
        if '/none' in args.lower():
            subprocess.call("installer.exe")
        else:
            subprocess.call(f"installer.exe {args}")
        time.sleep(2)
        os.remove('installer.exe')
        step_choice1 = input(f'{qe}96m {t("step5_to_install_complete")}')                    
        if step_choice1 == '' or step_choice1 == None or step_choice1 != '':
            online_install_programs()    
    elif 'н' in step_choice.lower() or 'n' in step_choice.lower():
        step_choice = input(f'{qe}96m {t("step4_cancel_install")}' + ' ')
        if step_choice == '' or step_choice == None or step_choice != '':
            online_install_programs()
    else:
        nosteps_install(url, name, args)

def select_program_and_install(category=None, indexing=None):
    clear()
    if os.path.exists('installer.exe'):
        os.remove('installer.exe')
    if category != None and indexing != None:
        url_program = config['programs'][category][indexing-1]["url"]
        silentArgs = config['programs'][category][indexing-1]["silentArgs"]
        name_program = config['programs'][category][indexing-1]["name"]
        if settings['dont_steps'] == "no":
            step_1_install(url_program, name_program, silentArgs)     
        else:                  
            nosteps_install(url_program, name_program, silentArgs)

def select_category_online(category=None):
    clear()
    print('\033[34m======================= Installer Program PE by InfoSecurity - Online =======================')
    print(t("select_program"))
    if category != None:
        if category in config['programs']:
            i = 0
            for item in config['programs'][category]:
                i += 1
                print(f'{i}: {item["name"]}')
    print('')
    print('')
    print(t("back"))
    print('\033[34m======================= Installer Program PE by InfoSecurity - Online =======================')
    choice = input(t("types"))
    try:
        try:
            if choice == '0':
                online_install_programs()
                return
            elif int(choice) <= len(config['programs'][category]):
                select_program_and_install(category, int(choice))
                return
                # print(f'name: {config["programs"][category][int(choice)-1]["name"]}\nurl: {config["programs"][category][int(choice)-1]["url"]}\nsilentArgs: {config["programs"][category][int(choice)-1]["silentArgs"]}')
                # choice = input(f"{qe}97m" + t("contenter"))
                # if choice == '' or choice == None or choice != '':
                #     online_install_programs()        
            else:
                print('\033[41m' + t("wrong_choice"))
                choice = input('\033[97m' + t("contenter"))           
                if choice == '' or choice == None or choice != '':
                    online_install_programs()
                    return
        except: 
            print('\033[41m' + t("wrong_choice"))
            choice = input('\033[97m' + t("contenter"))           
            if choice == '' or choice == None or choice != '':
                online_install_programs()        
                return    
    except KeyError: 
        logger.exception(f'\n{tags["error"]} Ошибка конфигурационного файла. Программа не смогла захватить строчку ПО из категории: {category}\n')
        print(f'{qe}41m' + t("error_conf0"))
        print(f'{qe}97m' + t("error_conf1"))        
        choice = input()
        if choice == '' or choice == None or choice != '':
            online_install_programs()      
            return          
    except ValueError:
        return

def settings_ippe():
    global data_translation
    clear()
    print('\033[34m' + '======================= Installer Program PE by InfoSecurity =======================')
    print('\033[36m' + '======================= ' + t("settings_title") +' =======================')
    print(t("settings_text_main"))
    print('\033[36m' + '======================= ' + t("settings_title") +' =======================')
    print('\033[34m' + '======================= Installer Program PE by InfoSecurity =======================')
    choice = input(t("types"))
    if choice == "0":
        menu()
    elif choice == "1":
        print(f'\n{t("choice_lang")}')
        choice_lang = input(t("types"))
        if choice_lang == "1":
            settings['language'] = 'ru'
            if save_settings():
                print(f'{qe}97m {t("save_config")}')
            else:
                print('Error. See log.')
            settings_ippe()
        elif choice_lang == "2":
            settings['language'] = 'en'
            if save_settings():
                print(f'{qe}97m {t("save_config")}')
            else:
                print('Error. See log.')
            settings_ippe()
        else:
            print(f'{qe}41m' + t("wrong_choice"))
            print(f'{qe}97m' + t("for_escape"))
            if choice_lang == '' or choice_lang == None or choice_lang != '':
                settings_ippe()
    elif choice == "2":
        init_input = update_conf()
        if init_input == '' or init_input == None or init_input != '':
            settings_ippe() 
    elif choice == "3":
        if settings['autoupdate_conf'] == 'yes':
            settings['autoupdate_conf'] = 'no'
            if save_settings():
                print(f'{qe}97m {t("save_config")}')
            print('\n' + f'{qe}97m' + t("complete_disable_conf"))     
            aint = input()
            if aint == '' or aint == None or aint != '':
                settings_ippe()                        
        else:
            settings['autoupdate_conf'] = 'yes'
            if save_settings():
                print(f'{qe}97m {t("save_config")}')
            print('\n' + f'{qe}97m' + t("complete_enable_conf"))
        aint = input()
        if aint == '' or aint == None or aint != '':
            settings_ippe()         
    elif choice == "4":
        os.remove("translation.json")
        wget.download("https://raw.githubusercontent.com/alfantasy/ifsinstaller/refs/heads/main/translation.json", "translation.json")
        with open("translation.json", "r", encoding='UTF-8') as f:
            content_translate = f.read()
            data_translation = json.loads(content_translate)    
        print('\n' + f'{qe}97m' + t("complete_update_trans"))     
        aint = input()
        if aint == '' or aint == None or aint != '':
            settings_ippe()    
    elif choice == "5":
        if settings['dont_steps'] == 'no':
            settings['dont_steps'] = 'yes'
            if save_settings():
                print(f'{qe}97m {t("save_config")}')
            print(f'{qe}97m' + t("complete_disable_steps"))                        
        else:
            settings['dont_steps'] = 'no'
            if save_settings():
                print(f'{qe}97m{t("save_config")}')
            print(f'{qe}97m' + t("complete_enable_steps"))
        aint = input()
        if aint == '' or aint == None or aint != '':
            settings_ippe()

def menu():
    clear()
    print('\033[34m' + '======================= Installer Program PE by InfoSecurity =======================')
    print(t("menu"))
    print('\033[34m' + '======================= Installer Program PE by InfoSecurity =======================')
    choice = input(t("types"))
    if choice == '1':
        online_install_programs()
    elif choice == '2':
        clear()
        print(f'{qe}96m{t("coming_soon")}')
        choice = input(t("contenter"))
        if choice == '' or choice == None or choice != '':
            menu()
    elif choice == '3':
        help()
    elif choice == '4':
        settings_ippe()
    elif choice == '0':
        clear()
        print(f'{qe}34m' + t("thanks_usage"))
        try:
            exit()
        except SystemExit:
            logger.info(f'{tags["info"]} Пользователь завершил работу программы.')
    else:
        print(f'{qe}41m' + t("wrong_choice"))
        print(f'{qe}97m' + t("for_escape"))
        if choice == '' or choice == None or choice != '':
            menu()

if len(sys.argv) > 1:
    if sys.argv[1] == '-h' or sys.argv[1] == '-help':
        print(t("help_console"))
        try:
            exit()
        except SystemExit:
            ... 
    elif sys.argv[1] == '-oInstall':
        if len(sys.argv) == 3:
            if sys.argv[2] == '-noUpdate':
                print(f"{qe}42m" + t("off_update"))
            else:
                if settings['autoupdate_conf'] == 'yes':
                    print(f"{qe}42m======================= " + t("upload_conf") + " =======================")
                    if os.path.exists('config.json'):
                        os.remove('config.json')
                        time.sleep(0.5)
                    wget.download(url_cfg_up, 'config.json')
        else:
            if settings['autoupdate_conf'] == 'yes':
                print(f"{qe}42m======================= " + t("upload_conf") + " =======================")
                if os.path.exists('config.json'):
                    os.remove('config.json')
                    time.sleep(0.5)
                wget.download(url_cfg_up, 'config.json')
            time.sleep(1)
        print('\n' + f"{qe}42m" + t("launch_script"))
        online_install_programs()
        with open('config.json', 'r') as f:
            content = f.read()
            config = json.loads(content)
    elif sys.argv[1] == '-ofInstall':
        if len(sys.argv) == 3:
            if sys.argv[2] == '-noUpdate':
                print(f"{qe}42m" + t("off_update"))
            else:
                if settings['autoupdate_conf'] == 'yes':
                    print(f"{qe}42m======================= " + t("upload_conf") + " =======================")
                    if os.path.exists('config.json'):
                        os.remove('config.json')
                        time.sleep(0.5)
                    wget.download(url_cfg_up, 'config.json')
        else:
            if settings['autoupdate_conf'] == 'yes':
                print(f"{qe}42m======================= " + t("upload_conf") + " =======================")
                if os.path.exists('config.json'):
                    os.remove('config.json')
                    time.sleep(0.5)
                wget.download(url_cfg_up, 'config.json')
            time.sleep(1)
        print('\n' + f"{qe}42m" + t("launch_script"))
        offline_install_programs()
        with open('config.json', 'r') as f:
            content = f.read()
            config = json.loads(content)
    elif sys.argv[1] == '-noUpdate':
        print(f"{qe}42m" + t("off_update"))
        try:
            print('\033[42m======================= ' + t("load_config") + ' =======================')
            with open('config.json', 'r') as f:
                content = f.read()
                config = json.loads(content)
        except FileNotFoundError as e:
            print(f"{qe}41m" + t("error_load_config0"))
            print(f"{qe}97m" + t("error_load_config1"))            
        print('\n' + f"{qe}42m" + t("launch_script"))            
        time.sleep(1)
        menu()
    else:
        argument_wrong = ''
        for item in sys.argv[1::]:
            argument_wrong = f'{argument_wrong} {item}'
        print(f"{qe}41m" + t("wrong_argument") + argument_wrong)
        print(f"{qe}41m" + t("wrong_argument0"))
        try:
            exit()
        except SystemExit:
            ...
elif len(sys.argv) == 1:
    if settings['autoupdate_conf'] == 'yes':
        print(f"{qe}42m" + "======================= " + t("upload_conf") + " =======================")
        if os.path.exists('config.json'):
            os.remove('config.json')
            time.sleep(0.5)
        wget.download(url_cfg_up, 'config.json')
        time.sleep(1)
    print('\n' + f"{qe}42m" + t("launch_script"))   
    try:
        with open('config.json', 'r') as f:
            content = f.read()
            config = json.loads(content)
    except: 
        print(f"{qe}41m" + t("error_load_config0"))
        print(f"{qe}97m" + t("error_load_config1"))            
    menu()