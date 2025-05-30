import json

json_table = {
    "programs":
        {
            "browsers": 
                [
                    {
                        "name": "Chrome", 
                        "url": "https://dl.google.com/chrome/install/standalonesetup.exe", 
                        "silentArgs": "/silent /install"
                    }, 
                    {
                        "name": "Firefox", 
                        "url": "https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=ru", 
                        "silentArgs": "/silent"
                    }
                ],
            "text_editor": 
                [
                    {
                        "name": "Visual Studio Code", 
                        "url": "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user", 
                        "silentArgs": "/None"
                    }, 
                    {
                        "name": "Notepad++ 8.6.7", 
                        "url": "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.6.7/npp.8.6.7.Installer.x64.exe", 
                        "silentArgs": "/S"
                    }
                ],
            "media_player": 
                [
                    {
                        "name": "VLC Media Player 3.0.21",
                        "url": "https://download.videolan.org/pub/videolan/vlc/last/win64/vlc-3.0.21-win64.exe",
                        "silentArgs": "/L=ru /S"
                    },
                    {
                        "name": "K-Lite Codec Pack Standard 1875 Edition",
                        "url": "https://files2.codecguide.com/K-Lite_Codec_Pack_1875_Standard.exe",
                        "silentArgs": "/None"
                    }
                ],
            "audio_player":
                [
                    {
                        "name": "AIMP 5.30.2563",
                        "url": "https://aimp.ru/files/windows/builds/aimp_5.30.2563_w64.exe",
                        "silentArgs": "/None"
                    }
                ],
            "archiver": {
                [
                    {
                        "name": "7-Zip 24.09",
                        "url": "https://www.7-zip.org/a/7z2409-x64.exe",
                        "silentArgs": "/S"
                    }
                ]
            }
        } 
    }