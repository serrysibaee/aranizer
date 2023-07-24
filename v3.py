import streamlit as st
import transformers
from transformers import AutoTokenizer
from transformers import PreTrainedTokenizerFast


import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpeg;base64,{encoded_string.decode()});
            background-size: 100%;
            direction: rtl; /* Set the text direction to right-to-left */;
            
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local('wp3186008.jpg')



# Load the AraBERT tokenizer
tokenizer = PreTrainedTokenizerFast(tokenizer_file="sentence peice tokenizers/SP_tokenizer_32.0K.json")
arabic_diacritics = ['َ', 'ِ', 'ُ', 'ّ', 'ً', 'ٍ', 'ٌ', 'ْ', 'َّ', 'ِّ', 'ُّ', 'ّـ', 'ًّ', 'ٍّ', 'ٌّ', 'ٍّ']
tokenizer._add_tokens(arabic_diacritics)

# Title and description in Arabic
st.title("مقسم النصوص Aranizer")
st.subheader("أدخل نصك العربي")

# Create a function to tokenize the input text in Arabic
def tokenize_text_arabic(text):
  tokens = tokenizer(text=text, return_tensors="pt")["input_ids"]
  return tokens

# Add a bar on the left to write details about the tokenizer in Arabic
st.sidebar.image("download.png", use_column_width=True)
st.sidebar.write("عن Aranizer")
st.sidebar.write("بِسمِ اللهِ الرَّحمٰنِ الرَّحِيمِ")
st.sidebar.write("آرانايزر هو توكينايزر جديد مصمَّم خصيصًا للغة العربية. يعمل آرانايزر على تجزئة النصوص العربية إلى أجزاء صغيرة تُعرف باسم الـتوكنز، ويُسهِّل قراءة النصوص وتحليلها. يُعدُّ آرانايزر أداة مفيدة للمطورين والباحثين الذين يعملون في مجال معالجة اللغة العربية وتحليلها. بفضل تصميمه القوي وسهولة استخدامه، يعد آرانايزر اختيارًا مثاليًا لمشاريع متعدِّدة تتطلب التعامل مع النصوص العربية بفعالية ودقة.")
st.sidebar.write("مع آرانايزر، ستكون قادرًا على توفير تجربة تحليل نصوص محسَّنة وفعَّالة للمستخدمين الناطقين بالعربية، مما يعزز من تطوير التطبيقات والحلول اللغوية القائمة على هذه اللغة الجميلة والغنية.")
st.sidebar.write('*Omar Najar, Serry Sibaee. (July 2023).[Aranizer]: A Tokenizer for Arabic Language. Supervised by Dr. Lahouari Ghouti and Dr. Anis Kouba. Prince Sultan University, Riyadh, Saudi Arabia*', )
# Add a text input field for the user to write their text in Arabic
user_input = st.text_area("", "")

# Tokenize the user input in Arabic
if st.button("تقسيم النص"):
    if user_input.strip() == "":
        st.warning("يرجى إدخال نص قبل التقسيم.")
    else:
        tokenized_output = tokenizer.tokenize(user_input)
        decode_output = tokenizer.encode(user_input)
        st.subheader("النص بعد التقسيم:")
        st.write(tokenized_output)

        # Calculate number of tokens and words
        num_tokens = len(tokenized_output)
        num_words = len(user_input.split())
        decoded_str = str(decode_output)
        col1, col2, col3 = st.columns(3)
        col1.metric("الأجزاء", decoded_str)
        col2.metric("عدد العناصر", num_tokens)
        col3.metric("عدد الكلمات", num_words )

