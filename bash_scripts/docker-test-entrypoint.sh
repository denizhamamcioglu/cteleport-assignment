#!/bin/sh

echo "Bash: Installing requirements"
tail -f /dev/null
pip install -r requirements.txt
echo "Bash: Executing tests."
# shellcheck disable=SC2086
pytest $PYTEST_ARGS || exit 1  # the disable rule above is to prevent the PyCharm IDE quoting PYTEST_ARGS, causing the pipeline to fail.
echo "Bash: Changing the current directory to allure-results"
cd allure-results
echo "Bash: Giving write permissions to all files inside allure-results for the current group"
chmod g+w *