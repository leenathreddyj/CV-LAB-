#!/usr/bin/env python3
"""
Startup check script for Railway deployment
Author: Venkata Saileenath Reddy
"""
import sys
import os

print("=" * 60)
print("Railway Startup Check")
print("=" * 60)

errors = []

# Check Python version
print(f"Python version: {sys.version}")
if sys.version_info < (3, 8):
    errors.append("Python 3.8+ required")

# Check critical imports
print("\nChecking imports...")
try:
    import flask
    print("✓ Flask")
except ImportError as e:
    errors.append(f"Flask: {e}")

try:
    import cv2
    print(f"✓ OpenCV {cv2.__version__}")
except ImportError as e:
    errors.append(f"OpenCV: {e}")

try:
    import numpy
    print(f"✓ NumPy {numpy.__version__}")
except ImportError as e:
    errors.append(f"NumPy: {e}")

try:
    from app import app
    print("✓ App imports successfully")
except Exception as e:
    errors.append(f"App import: {e}")

# Check environment
print("\nChecking environment...")
port = os.environ.get('PORT', 'Not set')
print(f"PORT: {port}")

# Summary
print("\n" + "=" * 60)
if errors:
    print("❌ ERRORS FOUND:")
    for error in errors:
        print(f"  - {error}")
    sys.exit(1)
else:
    print("✓ All checks passed!")
    sys.exit(0)

