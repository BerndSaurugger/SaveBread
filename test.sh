#!/bin/sh

coverage run -m pytest
coverage report
coverage xml
flake8 src/