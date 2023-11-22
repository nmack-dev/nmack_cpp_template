import os
import subprocess

# Set the path to your Premake executable
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'relative/path/to/file/you/want')
premake_path = os.path.join(dirname, 'premake/premake5.exe')

# Run Premake to generate project files
subprocess.run([premake_path, 'vs2022'], shell=True, check=True)

# Build and clone the Google Test library
subprocess.run(['git', 'submodule', 'update', '--init', '--recursive'], shell=True, check=True)
os.chdir('external/googletest')
os.makedirs('build', exist_ok=True)
os.chdir('build')
subprocess.run(['cmake', '..'], shell=True, check=True)
subprocess.run(['cmake', '--build', '.'], shell=True, check=True)

# Return to the project root
os.chdir('../../..')

print('Bootstrap complete.')