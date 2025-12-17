from playwright.sync_api import Page, expect

BASE_URL = "http://127.0.0.1:8000/"

def test_cube(page: Page):
    page.goto(BASE_URL)

    input = page.get_by_placeholder("Enter a number")
    input.fill("5")

    page.get_by_role(
        "button", name="Find Cube"
    ).click()

    result = page.locator("#result")
    expect(result).to_contain_text("The cube of 5 is 125.")

def test_empty_input(page: Page):
    page.goto(BASE_URL)

    input = page.get_by_placeholder("Enter a number")
    input.fill("")

    page.get_by_role(
        "button", name="Find Cube"
    ).click()
    
    message = page.locator("#message")
    result = page.locator("#result")
    expect(message).to_have_text(
        "Enter something!"
        )
    expect(result).to_have_text("")
