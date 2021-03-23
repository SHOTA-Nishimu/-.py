import re
import random
import streamlit as st
import numpy as np

#テキストの読み込み
source = '児のそら寝単語.txt'

f = open(source, encoding='utf-8')
d = f.read()
f.close()    
#print(d)

#正規表現
keys = re.findall(r'[^a-z\n]+', d)

#テキストの読み込み（答え）
source02 ='児のそら寝単語解答.txt'

f02= open(source02, encoding='utf-8')
d2 = f02.read()
f02.close()    
#print(d2)

#正規表現
values = re.findall(r'[^a-z\n]+', d2)
#print(values)

word_dict = dict(zip(keys, values))
#print(word_dict)

st.title('児のそら寝')

"""

### 次の（　）の単語の意味を答えなさい。

"""

question_word = random.choice(keys)
correct_answer = word_dict[question_word]
c_answer=correct_answer

st.header(question_word)

expander = st.beta_expander('答えを表示する')
expander.header(c_answer)
    
button = st.button('次の問題を表示する')
