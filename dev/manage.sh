#!/usr/bin/env bash

set -eux

cd $(dirname $0)/..

poetry run python manage.py "$@"
