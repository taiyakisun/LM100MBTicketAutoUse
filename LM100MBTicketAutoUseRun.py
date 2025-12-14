from playwright.sync_api import sync_playwright

TARGET_URL = "https://linksmate.jp/mypage/capacity-ticket/"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="state.json")
        page = context.new_page()

        page.goto(TARGET_URL)

        # もしJS標準ダイアログなら自動でOK
        page.on("dialog", lambda d: d.accept())

        for i in range(38):  # 複数回繰り返す
            # 例：最初のボタン
            #page.get_by_role("button", name="実行").click()
            page.locator("#use_ticket_100mb").click()
            #page.wait_for_timeout(1000)

            # 例：ページ内モーダルのOKを2回押す想定
            # ボタン名が同じならこう書けます
            #page.get_by_role("button", name="OK").click()
            page.get_by_role("button", name="追加する").click()
            #page.wait_for_timeout(1000)

            #page.get_by_role("button", name="OK").click()
            page.get_by_role("button", name="閉じる").click()
            #page.wait_for_timeout(1000)

        browser.close()

if __name__ == "__main__":
    main()