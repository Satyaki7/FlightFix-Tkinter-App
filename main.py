import customtkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

a = tk
b = ttk

from my_package123 import *

login_page = login.loginop(a,b)
if(login_page == 1):
   sign_page = signin.signop(a,b)
