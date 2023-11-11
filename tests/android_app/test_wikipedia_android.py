import allure

from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_search():
    with allure.step('Skip wellcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with allure.step('Verify found content'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


def test_open_article_page():
    with allure.step('Skip wellcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with allure.step('Open article page'):
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).first.click()

    with allure.step('Verify opened article'):
        browser.element((AppiumBy.XPATH, '(//android.widget.TextView[@text="Appium"])[1]')).should(
            be.visible)


def test_onboarding_screen():
    continue_button = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button'))
    page_title = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))

    with allure.step('Verify first page'):
        page_title.should(have.text('The Free Encyclopedia'))
        continue_button.click()

    with allure.step('Verify second page'):
        page_title.should(have.text('New ways to explore'))
        continue_button.click()

    with allure.step('Verify third page'):
        page_title.should(have.text('Reading lists with sync'))
        continue_button.click()

    with allure.step('Verify fourth page'):
        page_title.should(have.text('Send anonymous data'))