#!/bin/sh
cat << "EOF"
 _,-""`""-~`)
(`~           \
 |     a   a   \
 ;        o     ; ___  _,,,,_     _.-~'.
  \      `^`    /`_.-"~      `~-;`      \
   \_      _  .'                 `,     |
     |`-                           \'__/
    /                      ,_       \  `'-.
   /    .-""~~--.            `"-,   ;_    /
  |              \               \  | `""`
   \__.--'`"-.   /_               |'
              `"`  `~~~---..,     |
 jgs                         \ _.-'`-.
                              \       \
                               '.     /
                                 `"~"`
EOF
cat << "EOF"
      __          ________  _____  ____  __  __ ______   _______ _____   _____
     /\ \        / /  ____|/ ____|/ __ \|  \/  |  ____| |__   __|  __ \ |  __ \
    /  \ \  /\  / /| |__  | (___ | |  | | \  / | |__       | |  | |  | || |  | |
   / /\ \ \/  \/ / |  __|  \___ \| |  | | |\/| |  __|      | |  | |  | || |  | |
  / ____ \  /\  /  | |____ ____) | |__| | |  | | |____     | |_ | |__| || |__| |
 /_/    \_\/  \/   |______|_____/ \____/|_|  |_|______|    |_(_)|_____(_)_____/
EOF

# cd ../src && python3 manage.py test --settings=superapi.settings.developments
# -x --ipdb 는 첫 실패시에 그 다음 코드에 브레이크 포인터를 걸어버린다.
# pytest-ipdb repo https://github.com/mverteuil/pytest-ipdb

unset DATABASE_HOST
unset DATABASE_PORT
unset DATABASE_NAME
unset DATABASE_USER
unset DATABASE_PASSWORD

export DEFAULT_FROM_EMAIL = "YourEmailExample!!@gmail.com"
export EMAIL_HOST="smtp.gmail.com"
export EMAIL_PORT=587
export EMAIL_HOST_USER="YourEmailExample!!@gmail.com"
export EMAIL_HOST_PASSWORD="Password"
export SERVER_EMAIL="YourEmailExample!!@gmail.com"

echo $DATABASE_HOST
echo $DATABASE_PORT
echo $DATABASE_NAME
echo $DATABASE_USER
echo $DATABASE_PASSWORD

echo $EMAIL_HOST
echo $EMAIL_PORT

# cd ../src && pytest -s posts/tests/test_models.py -x --ipdb
# cd ../src && pytest -s posts/tests/test_views.py -x --ipdb
cd ../src && pytest -s posts/tests/test_views.py
# cd ../src && pytest -s posts/tests/tests_async/test_celery_jobs.py

# cd ../src && pytest -s tools/email/tests/test_send_email.py
# cd ../src && pytest -s posts/tests/test_oauth2_models.py

