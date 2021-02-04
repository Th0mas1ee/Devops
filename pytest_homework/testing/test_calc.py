import allure
import pytest

"""
课后作业
补全计算器中加法和除法的测试用例
使用参数化完成测试用例的自动生成
在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
"""


@allure.feature("Calculator Testing")
class TestCalc:
    @allure.story("Addition Testing")
    @pytest.mark.add
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=1)
    @allure.link('https://github.com/Th0mas1ee', name='Link')
    def test_add(self, get_calc, add_get_data):
        # 调用相加方法
        with allure.step("Computing the sum of two numbers"):
            result = get_calc.add(add_get_data[0], add_get_data[1])
        if isinstance(result, float):
            result = round(result, 2)
        # 得到相加结果之后写断言
        assert result == add_get_data[2]

    @allure.story("Division Testing")
    @pytest.mark.div
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=4)
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    def test_div(self, get_calc, div_get_data):
        # 调用相除方法
        with allure.step("Computing the division of two numbers"):
            divisor = div_get_data[1]
            if divisor == 0:
                raise Exception("The divisor couldn't be zero!")
            else:
                result = get_calc.div(div_get_data[0], div_get_data[1])
        if isinstance(result, float):
            result = round(result, 2)
        # 得到相除结果之后写断言
        allure.attach("<div>This is a html attachment</div>", 'Html attachment',
                      attachment_type=allure.attachment_type.HTML)
        assert result == div_get_data[2]

    @allure.story("Subtraction Testing")
    @pytest.mark.sub
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=2)
    def test_sub(self, get_calc, sub_get_data):
        # 调用相减方法
        with allure.step("Computing the difference of two numbers"):
            result = get_calc.sub(sub_get_data[0], sub_get_data[1])
        if isinstance(result, float):
            result = round(result, 2)
        # 得到相减结果之后写断言
        assert result == sub_get_data[2]

    @allure.story("Multiplication Testing")
    @pytest.mark.mul
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=3)
    def test_mul(self, get_calc, mul_get_data):
        # 调用相乘方法
        with allure.step("Computing the product of two numbers"):
            result = get_calc.mul(mul_get_data[0], mul_get_data[1])
        if isinstance(result, float):
            result = round(result, 2)
        # 得到相乘结果之后写断言
        assert result == mul_get_data[2]
