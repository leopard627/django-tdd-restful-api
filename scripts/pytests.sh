#!/bin/sh

# cd ../src && python3 manage.py test --settings=superapi.settings.developments
# -x --ipdb 는 첫 실패시에 그 다음 코드에 브레이크 포인터를 걸어버린다.
# pytest-ipdb repo https://github.com/mverteuil/pytest-ipdb


# cd ../src && pytest -s posts/tests/test_models.py -x --ipdb

# cd ../src && pytest -s posts/tests/test_views.py -x --ipdb
# cd ../src && pytest -s posts/tests/test_views.py

cd ../src && pytest -s posts/tests/tests_async/test_celery_jobs.py

# cd ../src && pytest -s posts/tests/test_oauth2_models.py

