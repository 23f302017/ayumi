import streamlit as st
import spacy

# spaCyの日本語モデルをロード
nlp = spacy.load('ja_core_news_sm')

# Streamlitウェブアプリのタイトル
st.title('テキスト解析アプリ')

# ユーザーにテキスト入力を求める
text = st.text_area("テキストをここに入力してください", "")

# テキストが入力されたら処理を実行
if text:
    doc = nlp(text)
    tokens = [token.text for token in doc]
    normalized_tokens = [token.lemma_ for token in doc
                         if not token.is_stop and not token.is_punct]
    keywords = [token.text for token in doc if token.pos_ == 'NOUN']

    # 結果を表示
    st.write('Tokens:', tokens)
    st.write('Normalized Tokens:', normalized_tokens)
    st.write('Keywords:', keywords)
