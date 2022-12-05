#!/usr/bin/env bash

set -eux

cd $(dirname $0)/..

poetry run isort acoustid_web/
poetry run black acoustid_web/
