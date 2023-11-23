import os
import subprocess

# Set the path to your Premake executable
dirname = os.path.dirname(__file__)
premake_path = os.path.join(dirname, 'premake/premake5.exe')

# Run Premake to generate project files
subprocess.run([premake_path, 'vs2022'], shell=True, check=True)

# Build and clone the Google Test library

# Check if the 'external/googletest' directory exists
googletest_path = os.path.join(dirname, 'external/googletest')
if not os.path.exists(googletest_path):
    # If the directory doesn't exist, clone the submodule
    subprocess.run(['git', 'submodule', 'add', 'https://github.com/google/googletest.git', 'external/googletest'], shell=True, check=True)
else:
    # If the directory exists, update the submodule
    subprocess.run(['git', 'submodule', 'update', '--recursive', '--remote'], shell=True, check=True)

os.chdir(googletest_path)
os.makedirs('build', exist_ok=True)
os.chdir('build')
subprocess.run(['cmake', '..'], shell=True, check=True)
subprocess.run(['cmake', '--build', '.'], shell=True, check=True)

# Return to the project root
os.chdir('../../..')

print('Bootstrap complete.')