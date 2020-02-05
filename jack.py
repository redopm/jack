import comtypes.client
import pyttsx3
from _ctypes import COMError



engine = pyttsx3.init(driverName="sapi5", debug=True)