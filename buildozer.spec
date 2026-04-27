[app]

# (str) Title of your application
title = Control Iluminacion

# (str) Package name
package.name = controliluminacion

# (str) Package domain (needed for android/ios packaging)
package.domain = org.fmi

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
# Do not prefix with './'
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = python3,kivy,aiohttp==3.9.0,mygeotab==0.8.1

# (str) Presplash of the application
presplash.filename = %(source.dir)s/logo.png

# (str) Icon of the application
icon.filename = %(source.dir)s/icon.png

# (list) Supported orientations
orientation = portrait

#
# Android specific
#

fullscreen = 0

# Permisos necesarios
android.permissions = INTERNET

# --- Configuración para API 36 (Android 16 Baklava) y p4a develop ---
android.api = 36
android.minapi = 21
android.ndk = 25
android.sdk = 30

# Arquitecturas (solo 64 bits recomendado para Play Store)
android.archs = arm64-v8a

android.allow_backup = True

# --- Usar la rama develop de python-for-android (requerido para API 36 / Play Store) ---
p4a.branch = develop

# (str) Bootstrap to use for android builds
# p4a.bootstrap = sdl2

# (str) extra command line arguments to pass when invoking pythonforandroid.toolchain
# p4a.extra_args =

#
# iOS specific (no se usa)
#
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0
ios.codesign.allowed = false

[buildozer]

log_level = 2
warn_on_root = 1
