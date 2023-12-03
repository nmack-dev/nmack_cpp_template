import os
import subprocess

def main():
    # Set the path to your Premake executable
    dirname = os.path.dirname(__file__)
    premake_path = os.path.join(dirname, 'premake/premake5.exe')

    # Run Premake to generate project files
    subprocess.run([premake_path, 'vs2022'], shell=True, check=True)

    # Build the Google Test library
    subprocess.run(['git', 'submodule', 'update', '--recursive', '--remote'], shell=True, check=True)

    googletest_path = os.path.join(dirname, 'external/googletest')

    os.chdir(googletest_path)
    os.makedirs('build', exist_ok=True)
    os.chdir('build')
    subprocess.run(['cmake', '..'], shell=True, check=True)
    subprocess.run(['cmake', '--build', '.', '--target', 'clean'], shell=True, check=True)

    # Return to the project root
    os.chdir('../../..')

    print('Bootstrap complete.')

if __name__ == '__main__':
    main()