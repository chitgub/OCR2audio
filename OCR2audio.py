try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import pyttsx3

ocr_to_text = pytesseract.image_to_string(Image.open('image.png'))
print(ocr_to_text)
engine = pyttsx3.init()
engine.say(ocr_to_text)
engine.runAndWait()



