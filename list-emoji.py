# -*- coding: utf-8 -*-
# 指定フォルダ内の画像ファイル一覧をMarkdown形式に出力するだけのコード

import os

path = "./emoji"

files = [filename for filename in sorted(os.listdir(path)) if not filename.startswith('.')]

for f in files:
    print '!['+ f +'](emoji/'+ f +'?raw=true "'+ f +'")'
