# import pytest
#
# from pytestfunctions.arithmetic_class import ArithmeticClass
#
# class TestArithmeticModule:
#
#     def test_add(self):
#         ac = ArithmeticClass
#         res = ac.add(self,10,20)
#         assert res ==30
#
#     def test_mod(self):
#         ac = ArithmeticClass
#         res = ac.mod(self,10,20)
#         assert res ==0
#
#     def test_product(self):
#         ac = ArithmeticClass
#         res = ac.product(self,10,20)
#         assert res == 200


# import pytest
#
# from pytestfunctions.arithmetic_class import ArithmeticClass
#
#
#
# class TestArithmeticModule:
#
#     @pytest.fixture()
#     def SetUp(self):
#         self.ac = ArithmeticClass()
#
#     def test_add(self, SetUp, OneTimeSetUp):
#         # ac = ArithmeticClass
#         res = self.ac.add(10,20)
#         assert res ==30
#
#     def test_mod(self, SetUp, OneTimeSetUp):
#         # ac = ArithmeticClass
#         res = self.ac.mod(10,20)
#         assert res ==0
#
#     def test_product(self, SetUp, OneTimeSetUp):
#         # ac = ArithmeticClass
#         res = self.ac.product(10,20)
#         assert res == 200

import pytest

from pytestfunctions.arithmetic_class import ArithmeticClass


# from pytestfunctions.conftest import OneTimeSetUp

#
# @pytest.mark.usefixtures('OneTimeSetUp','SetUp' )
# class TestArithmeticModule:
#
#     @pytest.fixture()
#     def SetUp(self):
#         self.ac = ArithmeticClass()
#
#     def test_add(self):
#         # ac = ArithmeticClass
#         res = self.ac.add(10,20)
#         assert res ==30
#
#     def test_mod(self):
#         # ac = ArithmeticClass
#         res = self.ac.mod(10,20)
#         assert res ==0
#
#     def test_product(self):
#         # ac = ArithmeticClass
#         res = self.ac.product(10,20)
#         assert res == 200


@pytest.mark.usefixtures('OneTimeSetUp', 'SetUp')
class TestArithmeticModule:

    @pytest.fixture()
    def SetUp(self):
        self.ac = ArithmeticClass()
    @pytest.mark.smoke
    def test_add(self):
        # ac = ArithmeticClass
        res = self.ac.add(10, 20)
        assert res == 30

    @pytest.mark.smoke
    def test_mod(self):
        # ac = ArithmeticClass
        res = self.ac.mod(10, 20)
        assert res == 0

    # @pytest.mark.smoke
    # @pytest.mark.retest
    @pytest.mark.regression
    # @pytest.mark.sanity
    # @pytest.mark.unit
    def test_product(self):
        # ac = ArithmeticClass
        res = self.ac.product(10, 20)
        assert res == 200
# for generating html report we have to install "pip install pytest-html
# to generate html reportwe have to define in command line as below
#pytest -v -s ./pytestfunctions/test_arithmetic_class.py --html=report_name.html

#to execute specific function among all first we have to sort bye giving
# @pytest.mark.skome, @pytest.mark.retest, @pytest.mark.regression etc.
# at the time of execution in command line command  will be
# pytest -v -s ./pytestfunctions/test_arithmetic_class.py -m="smoke and regression"
# or -m ="retest or smoke" as per requirnment