try:
    import requests
    import os

    main_url = 'https://raw.githubusercontent.com/e500ky/arsBash/refs/heads/main/main.py'
    config_url = 'https://raw.githubusercontent.com/e500ky/arsBash/refs/heads/main/config.json'
    github_url = 'https://raw.githubusercontent.com/e500ky/arsBash/refs/heads/main/github.json'
    icon_url = 'https://raw.githubusercontent.com/e500ky/arsBash/refs/heads/main/icon.ico'
    user_url = 'https://raw.githubusercontent.com/e500ky/arsBash/refs/heads/main/user.json'

    main_rep = requests.get(main_url)

    config_rep = requests.get(config_url)

    github_rep = requests.get(github_url)

    user_rep = requests.get(user_url)

    # Dosyayı geçici bir yere kaydet
    with open("updated_main.py", "w", encoding="utf-8") as file:
        file.write(main_rep.text)
        file.close()

    with open("config.json", "w", encoding="utf-8") as file:
        file.write(config_rep.text)
        file.close()

    with open("github.json", "w", encoding="utf-8") as file:
        file.write(github_rep.text)
        file.close()

    with open("user.json", "w", encoding="utf-8") as file:
        file.write(user_rep.text)
        file.close()

    # İndirilecek resmin kaydedileceği yer
    resim_adi = os.path.join(os.getcwd(), 'icon.ico')

    # Resmi indirme işlemi
    response = requests.get(icon_url)

    if response.status_code == 200:
        with open(resim_adi, 'wb') as resim:  # Binary modda açıyoruz
            resim.write(response.content)  # Burada response.content kullanmalısın
    else:
        print(f"Resim indirilemedi. Hata kodu: {response.status_code}")

    # PyInstaller komutunu çalıştır
    import os
    os.system('pyinstaller --onefile --icon=icon.ico --distpath "./" --workpath "./" --name=Terminal updated_main.py')

    os.remove("updated_main.py")

except Exception as e:
    print(f"Error: {e}")