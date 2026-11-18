#!/usr/bin/env bash
# Runs once when the codespace is created.
# It installs the Python tools and downloads the Java tools, so that the lab is ready to start.
set -e

echo "Installing the Python tools (pytest, pytest-cov) ..."
pip install --no-cache-dir -r requirements.txt

echo "Downloading the Java tools (JUnit, JaCoCo, PIT) ..."
cd java
mvn -B -q test org.pitest:pitest-maven:mutationCoverage > /dev/null
mvn -B -q clean
cd ..
rm -rf .pytest_cache __pycache__ .coverage

echo
echo "Lab 5 is ready. Open README.md and follow the steps."
