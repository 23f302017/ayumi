import tkinter as tk
import spacy

# spaCyの日本語モデルをロード
nlp = spacy.load('ja_core_news_sm')

# テキスト処理関数
def process_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    doc = nlp(text)
    tokens = [token.text for token in doc]
    normalized_tokens = [token.lemma_ for token
                         in doc if not token.is_stop and not token.is_punct]
    keywords = [token.text for token in doc if token.pos_ == 'NOUN']

    return tokens, normalized_tokens, keywords

# GUIの設定
def setup_gui(tokens, normalized_tokens, keywords):
    root = tk.Tk()
    root.title("テキスト処理結果")

    # ウィンドウを最大化
    root.state('zoomed')

    # tk.Label(root, text="Tokens:").pack()
    # tk.Label(root, text=', '.join(tokens)).pack()
    #
    # tk.Label(root, text="Normalized Tokens:").pack()
    # tk.Label(root, text=', '.join(normalized_tokens)).pack()

    tk.Label(root, text="Keywords:").pack()
    tk.Label(root, text=', '.join(keywords)).pack()

    # ウィンドウを閉じる関数
    def close_window():
        root.destroy()

    # ボタンウィジェットを作成し、クリック時にウィンドウを閉じる
    button = tk.Button(root, text="閉じる", command=close_window)
    button.pack()

    # メインループを実行し、ウィンドウを表示
    root.mainloop()

# メイン処理
if __name__ == '__main__':
    file_path = 'sample_text.txt'  # ファイルパスを指定
    tokens, normalized_tokens, keywords = process_text(file_path)
    setup_gui(tokens, normalized_tokens, keywords)
