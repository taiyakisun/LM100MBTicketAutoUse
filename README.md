# LM100MBTicketAutoUse

LinksMateのマイページ上で「100MBデータ通信容量チケット」を、ブラウザ操作（Playwright / Python）で自動的に利用するためのスクリプト集です。

- 初回実行（ログイン状態の保存）: `LM100MBTicketAutoUseLogin.py`
- 2回目以降（チケット自動利用）: `LM100MBTicketAutoUseRun.py`

> 本リポジトリは非公式ツールです。LinksMate運営会社とは一切関係ありません。利用は自己責任でお願いします。

---

## 動作環境

- Python 3.8 以上
- Playwright（Python版）
- 対応ブラウザ: Chromium（デフォルト）
- 想定OS: Windows 10 / 11（Playwrightが動作する環境であれば他OSでも利用可能です）

---

## セットアップ

1. Playwright をインストールします。

```bash
pip install playwright
```

2. Playwright が使用するブラウザ本体をインストールします。

```bash
playwright install
```

---

## 使い方

### 1) 初回ログイン（LM100MBTicketAutoUseLogin.py）

1. 次を実行します。

```bash
python LM100MBTicketAutoUseLogin.py
```

2. 起動したブラウザでLinksMateにログインします（手動で操作します）。
3. スクリプトの指示に従い、ログイン状態をファイルに保存します。

- 以降の自動実行で、ここで保存したログイン状態（例: `state.json`）を再利用します。
- ログインが切れた場合は、再度このスクリプトを実行してください。

### 2) チケット自動利用（LM100MBTicketAutoUseRun.py）

1. 次を実行します。

```bash
python LM100MBTicketAutoUseRun.py
```

2. 保存済みのログイン状態を読み込み、チケット利用の一連操作を繰り返します。

---

## 実装の前提（セレクタ例）

本ツールは、以下のような要素をPlaywrightでクリックすることを想定しています。

- チケット利用ボタン（IDで一意に指定できる場合）

```python
page.locator("#use_ticket_100mb").click()
```

- 表示されるWebページ内モーダルの「追加する」ボタン（IDが不明でも文字列で指定）

```python
page.get_by_role("button", name="追加する").click()
```

※ サイト側のHTMLや文言が変わった場合は、上記の指定方法を実ページに合わせて修正してください。

---

## 待機（ウェイト）について

「クリックごとに2〜3秒待つ」など、意図的に間隔を入れたい場合は次のように待機を挟めます。

```python
page.locator("#use_ticket_100mb").click()
page.wait_for_timeout(2000)  # 2000ms = 2秒

page.get_by_role("button", name="追加する").click()
page.wait_for_timeout(2000)
```

---

## 注意事項

- 本ツールは、利用者本人が自分のアカウントを操作する用途のみを想定しています。
- 利用先サービスの利用規約・約款に反する使い方は行わないでください。
- サイト側の仕様変更により動作しなくなる可能性があります。
- 本ツールの利用により生じた損害について、作者は一切の責任を負いません。

---

## 著作権

- 著作権者: taiyakisun(たい焼き太陽)
- 製作年: 2025

```text
Copyright (c) 2025 taiyakisun(たい焼き太陽)
All rights reserved.
```
