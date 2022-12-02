#!/usr/bin/env bash

set -eux

poetry run isort --check acoustid_web/
poetry run black --check acoustid_web/

poetry run flake8 acoustid_web/
poetry run mypy acoustid_web/

# poetry run python manage.py collectstatic --verbosity 0 --clear --link --no-input
# poetry run python manage.py test --verbosity 2
