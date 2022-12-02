#!/usr/bin/env bash

set -eux

poetry run isort acoustid_web/
poetry run black acoustid_web/
