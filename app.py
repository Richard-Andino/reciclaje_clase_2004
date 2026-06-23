import json
from pathlib import Path
import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image

st.set_page_config(page_tittle = "Reciclaje IA_ISC", layout = "centered")
st.tittle("Modelo predictivo Reciclaje clase de IA-ISC-Campus Comayagua-2026")
st.write("Suba una imagen para clasificar con el modelo Mobilenet V2 pre entrenado")
