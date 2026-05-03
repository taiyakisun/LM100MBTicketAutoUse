---
description: LinksLateの100MBチケットを自動で使用する
---

# LinksLate 100MB チケット自動利用

デフォルトのチケット使用回数は **52回** です。ユーザーが別の回数を指定した場合はそちらを使用してください。

## 手順

1. `LM100MBTicketAutoUseLogin.py` を実行する（venvを使用: `.venv\Scripts\python.exe`）
// turbo

2. ブラウザが開いてログインページが表示されるので、ユーザーに手動ログインしてもらう。ログインが完了したらユーザーから報告をもらう。

3. ユーザーからログイン完了の報告を受けたら、ターミナルに Enter を送信して Login スクリプトを終了させる。
// turbo

4. `LM100MBTicketAutoUseRun.py --count 52` を実行する（ユーザーから別の回数指定があればその値を使う）。

5. スクリプトの完了（Exit code: 0）を待つ。完了したらユーザーに報告する。
