import numpy as np
from tensorflow.keras.models import load_model

# Load model
model = load_model("model/gemstone_model.h5")

# 🔥 IMPORTANT: MUST MATCH YOUR DATASET FOLDER NAMES EXACTLY
class_names = [
    "aquamarine",
    "australian_opal",
    "aventurine",
    "black_haqeeq",
    "blue_moonstone",
    "blue_sapphire_bkk",
    "blue_topaz",
    "cats_eye",
    "citrine",
    "crystal",
    "ethiopian_black_opal",
    "ethiopian_opal",
    "green_amethyst",
    "irani_feroza",
    "italian_coral",
    "japanese_coral",
    "karnite",
    "lapis_lazuli",
    "malchite",
    "moissanate",
    "nishapuri_feroza",
    "odisha_quartz",
    "paridot",
    "pink_tourmaline",
    "rhodolite_garnet",
    "rose_quartz",
    "ruby",
    "smokey_topaz",
    "south_sea_pearl",
    "sudan_ruby",
    "triangular_coral",
    "white_topaz",
    "yellow_sapphire_bkk",
    "yemeni_haqeeq",
    "zambian_emerald",
    "zambian_emerald_lg"
]

def predict_image(img):
    img = img.resize((224,224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)

    index = np.argmax(prediction)
    confidence = float(np.max(prediction))

    label = class_names[index]

    # 🔥 FORCE EXACT FORMAT
    label = str(label).strip().lower().replace(" ", "_")

    if confidence < 0.8:
        return "Low Confidence", confidence

    return label, confidence