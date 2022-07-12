from .base import AuthorsBaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AuthorsRegisterTest(AuthorsBaseTest):
    def get_by_placeholder(self, web_element, placeholder):
        return web_element.find_element(
            By.XPATH, f'//input[@placeholder="{placeholder}"]'
        )

    def fill_forms_with_data(self, form):
        fields = form.find_elements(By.TAG_NAME, 'input')
        for field in fields:
            if field.is_displayed():
                field.send_keys(' ' * 20)

    def test_empty_first_name_error_message(self):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.browser.find_element(
            By.XPATH,
            '/html/body/header/main/div[2]/form'
        )
        self.fill_forms_with_data(form)
        form.find_element(By.NAME, 'email').send_keys('ex@email.com')
        first_name_field = self.get_by_placeholder(form, 'Ex.: João')
        first_name_field.send_keys(' ')
        first_name_field.send_keys(Keys.ENTER)
        #Necessário selecionar o form novamente aqui
        form = self.browser.find_element(
            By.XPATH,
            '/html/body/header/main/div[2]/form'
        )
        self.sleep(5)
        self.assertIn('Write your first name', form.text)
