SECRET DROPS — публикация без Cloudflare

Сайт игры можно разместить на GitHub Pages. Бот при этом продолжит работать
на вашем Mac; он подключается к Telegram через polling и публичный адрес ему
нужен только для кнопки с игрой.

1. На github.com создайте новый публичный репозиторий, например secret-drops.
   Не добавляйте в файлы токен бота. Содержимое GitHub Pages будет публично.
2. В Терминале перейдите в папку проекта и отправьте нужные файлы в GitHub
   (замените YOUR-LOGIN на ваш логин, REPOSITORY на имя репозитория):

   cd ~/Desktop/secret-drops/secret-drops
   git init -b main
   git add bot.py requirements.txt README.txt 2_start_bot.command webapp .github
   git commit -m "Prepare Secret Drops for GitHub Pages"
   git remote add origin https://github.com/YOUR-LOGIN/REPOSITORY.git
   git push -u origin main

   Если GitHub попросит войти, завершите вход в браузере. Папки .venv и
   __pycache__ этими командами не загружаются.
3. Откройте Settings → Pages. В разделе Build and deployment выберите
   Source: GitHub Actions.
4. Откройте вкладку Actions и дождитесь успешного запуска workflow
   «Publish game to GitHub Pages». Страница будет доступна по адресу:
   https://ВАШ-ЛОГИН.github.io/ИМЯ-РЕПОЗИТОРИЯ/
5. Запустите 2_start_bot.command. Введите токен бота от @BotFather и адрес
   страницы из шага 4. Оставьте окно бота открытым.
6. В Telegram отправьте боту /start и нажмите «Играть».

После каждого обновления webapp GitHub Actions автоматически опубликует игру.
Сборка публикует только папку webapp; Python-бот и его файлы не попадают
на сайт.

Безопасность: ранее введённый токен был опубликован в сообщении. Отзовите его
через @BotFather командой /revoke и используйте новый токен.

Если macOS пишет «нет прав», в Терминале выполните:
  chmod +x /путь/к/папке/2_start_bot.command

Официальная инструкция GitHub Pages:
https://docs.github.com/en/pages/getting-started-with-github-pages
