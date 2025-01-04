import streamlit as st
import pandas as pd

df = pd.read_csv('英単語.csv')

# Streamlitアプリのタイトル
st.title('英単語とその答え')

# データフレームのスタイルを設定
styled_df = df.style.set_properties(**{
    'text-align': 'center',
    'background-color': '#f0f0f0',
    'border': '1px solid black',
    'color': 'black'  # テキストカラーを黒に設定
}).set_table_styles([{
    'selector': 'th',
    'props': [('background-color', '#404040'), ('color', 'white')]
}])

# スタイリングされたデータフレームを表示
st.table(styled_df)
