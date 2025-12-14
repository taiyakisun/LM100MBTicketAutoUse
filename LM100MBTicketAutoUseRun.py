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
        page.goto(TARGET_URL)

        page.on("dialog", lambda d: d.accept())

        for i in range(args.count):
            # チケット利用ボタン (ID指定)
            page.locator("#use_ticket_100mb").click()

            # ページ内モーダルのOKを2回押す想定
            page.get_by_role("button", name="追加する").click()
            page.get_by_role("button", name="閉じる").click()

        browser.close()

if __name__ == "__main__":
    main()