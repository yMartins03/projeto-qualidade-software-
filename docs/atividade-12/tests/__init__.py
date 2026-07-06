import sys
import os

# Garante que o módulo localeats seja encontrado tanto localmente quanto no CI
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
