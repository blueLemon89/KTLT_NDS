import bpy
import speech_recognition as sr

# Tạo một đối tượng Recognizer
r = sr.Recognizer()

def recognize_speech():
    # Ghi âm từ microphone
    with sr.Microphone() as source:
        print("Hãy nói gì đó:")
        audio = r.listen(source)

    # Sử dụng Google Speech Recognition để nhận dạng giọng nói
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Không thể nhận dạng giọng nói")
    except sr.RequestError as e:
        print("Lỗi kết nối tới dịch vụ nhận dạng giọng nói: {0}".format(e))

# Gọi hàm nhận dạng giọng nói
textt = recognize_speech()
if textt:
    textt = textt.lower()
    print("You say: " + textt)
    
    if(textt != null):
        change_color(object);
