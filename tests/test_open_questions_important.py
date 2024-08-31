from pages.section_important import CheckSections
from iniconf.data import safe_keeper
import pytest
import allure

class TestImportntQuestions:
    @allure.title('Проверяем вопроссы о важном"')
    @allure.description('Проверяем что по клику на вопрос откроется выпадающее меню с ответом')
    @pytest.mark.parametrize("meaning, get_text", [(0, safe_keeper[0]), (1, safe_keeper[1]), (2, safe_keeper[2]), (3, safe_keeper[3]), (4, safe_keeper[4]), (5, safe_keeper[5]), (6, safe_keeper[6]), (7, safe_keeper[7])])
    def test_questions_navigation(self, start_from_login_page, meaning, get_text):
        check_selections = CheckSections(start_from_login_page)
        check_selections.click_buttons_cockies()
        check_selections.scroll_page_for_live()
        element = check_selections.check_block_of_questions(meaning)
        comparison_results = check_selections.find_answer(meaning)
        assert get_text[element] == comparison_results
