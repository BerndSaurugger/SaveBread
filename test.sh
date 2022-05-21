#!/bin/sh

pytest --junitxml=report.xml
flake8 src/