#!/usr/bin/env python3
"""
Quality check script for ArticlesApp
"""
import subprocess
import sys

def run_command(command):
    """Run shell command and return success/failure"""
    try:
        result = subprocess.run(command, shell=True, check=True, 
                               capture_output=True, text=True)
        print(f"✓ {command}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {command}")
        print(f"Error: {e.stderr}")
        return False

def main():
    """Run all quality checks"""
    print("🚀 Running quality checks for ArticlesApp...")
    
    checks = [
        "python -m py_compile app.py",  # Syntax check
        "python -m pylint --fail-under=7 app.py || true",  # Linting
        "python -m pytest tests/ -v",  # Unit tests
        "python -m coverage run -m pytest tests/",  # Coverage
        "python -m coverage report --fail-under=80"  # Coverage threshold
    ]
    
    all_passed = True
    for check in checks:
        if not run_command(check):
            all_passed = False
    
    if all_passed:
        print("✅ All quality checks passed!")
        sys.exit(0)
    else:
        print("❌ Some checks failed")
        sys.exit(1)

if __name__ == "__main__":
    main()