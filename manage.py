#!/usr/bin/env python
import os
import sys

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")