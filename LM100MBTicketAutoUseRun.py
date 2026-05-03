import argparse
from playwright.sync_api import sync_playwright

TARGET_URL = "https://linksmate.jp/mypage/capacity-ticket/"

def parse_args():
    parser = argparse.ArgumentParser(description="LinksMate 100MB ticket auto use")
    parser.add_argument(
        "--count", "-n",
        type=int,
        required=True,
        help="繰り返し回数（使用するチケット枚数）"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    if args.count <= 0:
        raise SystemExit("--count は 1 以上を指定してください。")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        # Loginスクリプト側で保存した state.json を使う
        context = browser.new_context(storage_state="state.json")
        page = context.new_page()

        # 対象ページへ
        page.goto(TARGET_URL, wait_until="networkidle")

        page.on("dialog", lambda d: d.accept())

        for i in range(args.count):
            print(f"[{i+1}/{args.count}] チケットを利用中...")

            # チケット利用ボタン (ID指定) — 表示を待ってからクリック
            page.locator("#use_ticket_100mb").wait_for(state="visible", timeout=60000)
            page.locator("#use_ticket_100mb").click()

            # 確認モーダルの「追加する」ボタンをクリック
            page.get_by_role("button", name="追加する").wait_for(state="visible", timeout=30000)
            page.get_by_role("button", name="追加する").click()

            # 完了モーダルの「閉じる」ボタンをクリック
            page.get_by_role("button", name="閉じる").wait_for(state="visible", timeout=30000)
            page.get_by_role("button", name="閉じる").click()

            # 次のチケット利用に備えて待機
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(1000)

            print(f"[{i+1}/{args.count}] 完了")

        print("すべてのチケット利用が完了しました。")
        browser.close()

if __name__ == "__main__":
    main()