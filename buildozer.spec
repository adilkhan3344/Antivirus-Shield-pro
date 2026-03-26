[app]
title = Antivirus Shield Pro
package.name = antivirus_shield
package.domain = org.cybersecurity
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy

# Permissions for Professional Cyber Security
android.permissions = INTERNET, READ_PHONE_STATE, CALL_PHONE, ACCESS_FINE_LOCATION, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MODIFY_PHONE_STATE

orientation = portrait
fullscreen = 0
android.arch = arm64-v8a
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1

