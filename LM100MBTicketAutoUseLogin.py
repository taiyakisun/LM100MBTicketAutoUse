from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://linksmate.jp/login/")

        # ここで手動ログインしてOK
        print("手動でログインしたらEnterを押してください...")
        input()

        # ログイン後の状態を保存
        context.storage_state(path="state.json")
        browser.close()

if __name__ == "__main__":
    main()
