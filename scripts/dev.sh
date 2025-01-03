#!/bin/bash

# Set environment
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Run linting
echo "Running flake8 linting..."
flake8 src/ tests/ --max-line-length=120 --exclude=__init__.py

# Run type checking
echo "Running mypy type checking..."
mypy src/ tests/ --ignore-missing-imports

# Run tests
echo "Running pytest..."
pytest tests/ -v --cov=src --cov-report=html

# Run formatting
echo "Running black formatting..."
black src/ tests/ --line-length 120

# Run security checks
echo "Running bandit security checks..."
bandit -r src/

echo "Development tasks completed!"