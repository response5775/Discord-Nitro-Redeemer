import os

csa = 'py -m pip install' # change if it doesnt work

def exec(command):
  os.system(command=command)

def install_requirements():
  os.system("cls")
  try:
    import tls_client
    import yaml
    import colorama
    import requests
    import pyfiglet
    import termcolor
    import typing_extensions
    import ctypes
    import licensing
  except:
    exec(f'{csa} tls_client')
    exec(f'{csa} pyyaml')
    exec(f'{csa} colorama')
    exec(f'{csa} requests')
    exec(f'{csa} pyfiglet')
    exec(f'{csa} termcolor')
    #exec(f'{csa} concurrent.futures')
    exec(f'{csa} typing_extentions')
    exec(f'{csa} ctypes')
    exec(f'{csa} licensing')

