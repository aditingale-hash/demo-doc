# build.py
import os
import shutil
import zipfile
import subprocess

print("--- Starting Build Process ---")

# 1. Create a build directory
build_dir = 'build'
dist_dir = 'dist'
if os.path.exists(build_dir):
    shutil.rmtree(build_dir)
os.makedirs(build_dir)
if os.path.exists(dist_dir):
    shutil.rmtree(dist_dir)
os.makedirs(dist_dir)

# 2. Copy application files
print("Copying application files...")
shutil.copy('app.py', build_dir)
shutil.copy('requirements.txt', build_dir)
# Add any other necessary files (templates, static assets)

# 3. Install dependencies into the build directory (optional, for bundling)
# print("Installing dependencies for bundling...")
# subprocess.check_call([
#     'pip', 'install',
#     '-r', os.path.join(build_dir, 'requirements.txt'),
#     '--target', os.path.join(build_dir, 'libs') # Example: Install into a 'libs' subdir
# ])

# 4. Create a distributable archive
archive_name = os.path.join(dist_dir, 'simple-flask-app-package.zip')
print(f"Creating archive: {archive_name}")
with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, _, files in os.walk(build_dir):
        for file in files:
            file_path = os.path.join(root, file)
            archive_path = os.path.relpath(file_path, build_dir)
            print(f"Adding {archive_path} to zip...")
            zf.write(file_path, archive_path)

print("--- Build Process Finished ---")
print(f"Artifact created: {archive_name}")