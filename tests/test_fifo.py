import pytest

from src.fifo import Fifo
from data_test import *


class Test000FifoCapacity:
    @staticmethod
    def test_000_fifo_capacity_000_init_default():
        # setup
        test_fifo = Fifo()
        fifo_size = test_fifo.size()
        fifo_empty = test_fifo.empty()

        # test
        assert fifo_size == 0, f"Expected fifo size to be == to 0, got {fifo_size}"
        assert fifo_empty is True, f"Expected fifo empty to be True, got {fifo_empty}"

    @staticmethod
    def test_000_fifo_capacity_001_init_non_empty_list():
        # setup
        max_size = 10_000
        elements = list(range(0, max_size))
        test_fifo = Fifo(elements=elements)
        fifo_size = test_fifo.size()
        fifo_empty = test_fifo.empty()

        # test
        assert fifo_size == max_size, f"Expected fifo size to be == to {max_size}, got {fifo_size}"
        assert fifo_empty is False, f"Expected fifo empty to be False, got {fifo_empty}"

    @staticmethod
    def test_000_fifo_capacity_002_clear_empty_fifo():
        # setup
        test_fifo = Fifo()

        # test
        test_fifo.clear()
        fifo_size = test_fifo.size()
        fifo_empty = test_fifo.empty()

        assert fifo_size == 0, f"Expected fifo size to be == to 0, got {fifo_size}"
        assert fifo_empty is True, f"Expected fifo empty to be True, got {fifo_empty}"

    @staticmethod
    def test_000_fifo_capacity_003_clear_non_empty_fifo():
        # setup
        max_size = 10_000
        elements = list(range(0, max_size))
        test_fifo = Fifo(elements=elements)

        # test
        test_fifo.clear()
        fifo_size = test_fifo.size()
        fifo_empty = test_fifo.empty()
        assert fifo_size == 0, f"Expected fifo size to be == to 0, got {fifo_size}"
        assert fifo_empty is True, f"Expected fifo empty to be True, got {fifo_empty}"

    @staticmethod
    def test_000_fifo_capacity_004_push():
        # setup
        max_size = 10_000
        test_fifo = Fifo()

        # test
        for elem in range(0, max_size):
            test_fifo.push(elem)
            fifo_size = test_fifo.size()
            fifo_empty = test_fifo.empty()
            assert fifo_size == elem + 1, f"Expected fifo size to be == to {elem + 1}, got {fifo_size}"
            assert fifo_empty is False, f"Expected fifo empty to be False, got {fifo_empty}"

    @staticmethod
    def test_000_fifo_capacity_005_pop():
        # setup
        max_size = 10_000
        test_fifo = Fifo()
        for elem in range(0, max_size):
            test_fifo.push(elem)

        # test
        for elem in range(0, max_size):
            test_fifo.pop()
            fifo_size = test_fifo.size()
            assert fifo_size == max_size - (elem + 1), f"Expected fifo size to be == to {max_size - (elem + 1)}, " \
                                                       f"got {fifo_size}"

        fifo_empty = test_fifo.empty()
        assert fifo_empty is True, f"Expected fifo empty to be True, got {fifo_empty}"


class Test001FifoElementAccess:
    @staticmethod
    def test_001_fifo_element_access_000_front_empty_fifo():
        # setup
        test_fifo = Fifo()

        # test
        fifo_front = test_fifo.front()
        assert fifo_front is None, f"Expected Fifo front to be None, got {fifo_front}"

    @staticmethod
    @pytest.mark.parametrize('elements', TEST_LISTS)
    def test_001_fifo_element_access_001_front_non_empty_fifo(elements):
        # setup
        test_fifo = Fifo(elements=elements)

        # test
        fifo_front = test_fifo.front()
        assert fifo_front is elements[0], f"Expected Fifo front to be {elements[0]}, got {fifo_front}"

    @staticmethod
    @pytest.mark.parametrize('elements', TEST_LISTS)
    def test_001_fifo_element_access_002_front_after_push(elements):
        # setup
        test_fifo = Fifo()

        # test
        for elem in elements:
            test_fifo.push(element=elem)
            fifo_front = test_fifo.front()
            assert fifo_front is elements[0], f"Expected Fifo front to be {elements[0]}, got {fifo_front}"

    @staticmethod
    @pytest.mark.parametrize('elements', TEST_LISTS)
    def test_001_fifo_element_access_003_front_after_pop(elements):
        # setup
        size = len(elements)
        test_fifo = Fifo(elements)

        # test
        for index in range(1, size):
            test_fifo.pop()
            fifo_front = test_fifo.front()
            assert fifo_front is elements[index], f"Expected Fifo front to be {elements[index]}, got {fifo_front}"

    @staticmethod
    @pytest.mark.parametrize('elements', TEST_LISTS)
    def test_001_fifo_element_access_004_front_after_clear(elements):
        # setup
        test_fifo = Fifo(elements)

        # test
        test_fifo.clear()
        fifo_front = test_fifo.front()
        assert fifo_front is None, f"Expected Fifo front to be None, got {fifo_front}"

    @staticmethod
    def test_001_fifo_element_access_005_back_empty_fifo():
        # setup
        test_fifo = Fifo()

        # test
        fifo_back = test_fifo.back()
        assert fifo_back is None, f"Expected Fifo back to be None, got {fifo_back}"

    @staticmethod
    @pytest.mark.parametrize('elements', TEST_LISTS)
    def test_001_fifo_element_access_006_back_non_empty_fifo(elements):
        # setup
        test_fifo = Fifo(elements=elements)

        # test
        fifo_back = test_fifo.back()
        assert fifo_back is elements[-1], f"Expected Fifo back to be {elements[-1]}, got {fifo_back}"

    @staticmethod
    @pytest.mark.parametrize('elements', TEST_LISTS)
    def test_001_fifo_element_access_007_back_after_push(elements):
        # setup
        size = len(elements)
        test_fifo = Fifo()

        # test
        for index in range(0, size):
            test_fifo.push(element=elements[index])
            fifo_back = test_fifo.back()
            assert fifo_back is elements[index], f"Expected Fifo back to be {elements[index]}, got {fifo_back}"

    @staticmethod
    @pytest.mark.parametrize('elements', TEST_LISTS)
    def test_001_fifo_element_access_008_back_after_pop(elements):
        # setup
        size = len(elements)
        test_fifo = Fifo(elements)

        # test
        for x in range(0, size - 1):
            test_fifo.pop()
            fifo_back = test_fifo.back()
            assert fifo_back is elements[-1], f"Expected Fifo back to be {elements[-1]}, got {fifo_back}"

    @staticmethod
    @pytest.mark.parametrize('elements', TEST_LISTS)
    def test_001_fifo_element_access_009_back_after_clear(elements):
        # setup
        test_fifo = Fifo(elements)

        # test
        test_fifo.clear()
        fifo_back = test_fifo.back()
        assert fifo_back is None, f"Expected Fifo back to be None, got {fifo_back}"


class Test002FifoModifiers:
    @staticmethod
    @pytest.mark.parametrize('elements', TEST_LISTS)
    def test_002_fifo_modifiers_000_push(elements):
        # setup
        test_fifo = Fifo()

        # test
        for elem in elements:
            test_fifo.push(elem)
            # check front and back
            fifo_front = test_fifo.front()
            fifo_back = test_fifo.back()
            assert fifo_front is elements[0], f"Expected Fifo front to be {elements[0]}, got {fifo_front}"
            assert fifo_back is elem, f"Expected Fifo back to be {elem}, got {fifo_back}"

    @staticmethod
    @pytest.mark.parametrize('elements', TEST_LISTS)
    def test_002_fifo_modifiers_001_pop(elements):
        # setup
        size = len(elements)
        test_fifo = Fifo(elements)

        # test
        for index in range(0, size):
            elem = test_fifo.pop()
            assert elem is elements[index], f"Expected Fifo pop to be {elements[index]}, got {elem}"
            # check front and back
            fifo_front = test_fifo.front()
            fifo_back = test_fifo.back()
            if index != (size - 1):
                assert fifo_front is elements[index + 1], f"Expected Fifo front to be " \
                                                          f"{elements[index + 1]}, got {fifo_front}"
                assert fifo_back is elements[-1], f"Expected Fifo back to be {elements[-1]}, got {fifo_back}"
            else:
                assert fifo_front is None, f"Expected Fifo front to be None, got {fifo_front}"
                assert fifo_back is None, f"Expected Fifo back to be None, got {fifo_back}"

        elem = test_fifo.pop()
        assert elem is None, f"Expected Fifo pop to be None, got {elem}"
