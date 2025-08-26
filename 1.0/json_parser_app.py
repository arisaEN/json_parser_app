import json
import tkinter as tk
from tkinter import messagebox, scrolledtext
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class JsonFormatterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JSON Formatter App")
        self.root.geometry("1000x600")

        # タイトル
        title = ttk.Label(root, text="JSON Formatter", font=("Segoe UI", 16, "bold"))
        title.grid(row=0, column=0, columnspan=3, pady=10)

        # 左: 入力
        ttk.Label(root, text="入力 (生 JSON)").grid(row=1, column=0, sticky=W, padx=5)
        self.input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Consolas", 11))
        self.input_text.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

        # Ctrl+Enter で整形
        self.input_text.bind("<Control-Return>", self.parse_json_event)

        # 真ん中: ボタン
        self.parse_button = ttk.Button(
            root,
            text="▶ パースして整形 ▶\n(Ctrl+Enter でも実行)",
            bootstyle=PRIMARY,
            command=self.parse_json
        )
        self.parse_button.grid(row=2, column=1, padx=5, pady=5, sticky="ns")

        # 右: 出力
        ttk.Label(root, text="出力 (整形済み JSON)").grid(row=1, column=2, sticky=W, padx=5)
        self.output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Consolas", 11), state=tk.DISABLED)
        self.output_text.grid(row=2, column=2, sticky="nsew", padx=5, pady=5)

        # グリッドの伸縮設定
        root.grid_columnconfigure(0, weight=1)  # 左
        root.grid_columnconfigure(1, weight=0)  # 真ん中（固定）
        root.grid_columnconfigure(2, weight=1)  # 右
        root.grid_rowconfigure(2, weight=1)

    def parse_json(self):
        raw_text = self.input_text.get("1.0", tk.END).strip()
        if not raw_text:
            messagebox.showwarning("警告", "JSONを入力してください")
            return

        try:
            parsed = json.loads(raw_text)
            formatted = json.dumps(parsed, indent=4, ensure_ascii=False)

            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, formatted)
            self.output_text.config(state=tk.DISABLED)

        except json.JSONDecodeError as e:
            messagebox.showerror("エラー", f"JSONのパースに失敗しました:\n{e}")

    def parse_json_event(self, event):
        """キーバインド用 (イベント引数あり)"""
        self.parse_json()
        return "break"  # ← テキストに改行が入らないようにする


if __name__ == "__main__":
    root = ttk.Window(themename="flatly")
    app = JsonFormatterApp(root)
    root.mainloop()
