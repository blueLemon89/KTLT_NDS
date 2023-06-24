import bpy
import speech_recognition as sr

# Khởi tạo đối tượng recognizer từ thư viện SpeechRecognition
recognizer = sr.Recognizer()

# Hàm xử lý lệnh khi nhận được giọng nói từ người dùng
def process_speech(text):
    if "di chuyển" in text:
        # Lệnh di chuyển đối tượng
        bpy.context.object.location += bpy.context.object.location.normalized()
    if "thay đổi màu" in text:
        # Lệnh thay đổi màu sắc đối tượng
        bpy.context.object.data.materials[0].diffuse_color = (1.0, 0.0, 0.0)  
        

# Hàm xử lý giọng nói
def process_audio():
    with sr.Microphone() as source:
        print("Lắng nghe...")
        audio = recognizer.listen(source)
        try:
            # Sử dụng recognizer để chuyển đổi âm thanh thành văn bản
            text = recognizer.recognize_google(audio, language="vi-VN")
            print("Người dùng nói: " + text)
            process_speech(text)
        except sr.UnknownValueError:
            print("Không nhận dạng được giọng nói.")
        except sr.RequestError as e:
            print("Lỗi trong quá trình xử lý giọng nói: {0}".format(e))

# Bắt đầu lắng nghe giọng nói liên tục
def start_voice_interaction():
    while True:
        process_audio()

# Gọi hàm start_voice_interaction để bắt đầu tương tác giọng nói
start_voice_interaction()
