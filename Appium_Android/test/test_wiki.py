import allure
from allure import step, title, tag
from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from Appium_Android.test import conftest
from selene.support.shared import browser


@tag('Android')
@title('Getting started page')
def test_onboarding_screen():
    with step('First page checking'):
        browser.element((AppiumBy.ID, "org.wikipedia:id/primaryTextView")) \
            .should(have.text("The Free Encyclopedia\n"
                              "…in over 300 languages"))
        browser.element((AppiumBy.ID, "org.wikipedia:id/fragment_onboarding_forward_button")).click()

    with step('Second page checking'):
        browser.element((AppiumBy.ID, "org.wikipedia:id/primaryTextView")) \
            .should(have.text("New ways to explore"))
        browser.element((AppiumBy.ID, "org.wikipedia:id/fragment_onboarding_forward_button")).click()

    with step('Third page checking'):
        browser.element((AppiumBy.ID, "org.wikipedia:id/primaryTextView")) \
            .should(have.exact_text("Reading lists with sync"))
        browser.element((AppiumBy.ID, "org.wikipedia:id/fragment_onboarding_forward_button")).click()

    with step('Fourth page checking'):
        browser.element((AppiumBy.ID, "org.wikipedia:id/primaryTextView")) \
            .should(have.text("Send anonymous data"))
        browser.element((AppiumBy.ID, "org.wikipedia:id/fragment_onboarding_done_button")).click()
        browser.element((AppiumBy.ID, "org.wikipedia:id/search_container")) \
            .should(be.visible)
