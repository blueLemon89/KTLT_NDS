import subprocess
import sys

# Đường dẫn tới môi trường Python của Blender
blender_python_path = sys.executable

# Lệnh pip install
pip_install_command = [blender_python_path, "-m", "pip", "install", "SpeechRecognition"]
pip_install_command = [blender_python_path, "-m", "pip", "install", "pyaudio"]

# Chạy lệnh pip install
subprocess.call(pip_install_command)


