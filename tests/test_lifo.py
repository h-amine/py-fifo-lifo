import pytest

from src.lifo import Lifo
from data_test import *


class Test000LifoCapacity:
    @staticmethod
    def test_000_lifo_capacity_000_init_default():
        # setup
        test_lifo = Lifo()
        lifo_size = test_lifo.size()
        lifo_empty = test_lifo.empty()

        # test
        assert lifo_size == 0, f"Expected Lifo size to be == to 0, got {lifo_size}"
        assert lifo_empty is True, f"Expected Lifo empty to be True, got {lifo_empty}"

    @staticmethod
    def test_000_lifo_capacity_001_init_non_empty_list():
        # setup
        max_size = 10_000
        elements = list(range(0, max_size))
        test_lifo = Lifo(elements=elements)
        lifo_size = test_lifo.size()
        lifo_empty = test_lifo.empty()

        # test
        assert lifo_size == max_size, f"Expected Lifo size to be == to {max_size}, got {lifo_size}"
        assert lifo_empty is False, f"Expected Lifo empty to be False, got {lifo_empty}"

    @staticmethod
    def test_000_lifo_capacity_002_clear_empty_lifo():
        # setup
        test_lifo = Lifo()

        # test
        test_lifo.clear()
        lifo_size = test_lifo.size()
        lifo_empty = test_lifo.empty()

        assert lifo_size == 0, f"Expected Lifo size to be == to 0, got {lifo_size}"
        assert lifo_empty is True, f"Expected Lifo empty to be True, got {lifo_empty}"

    @staticmethod
    def test_000_lifo_capacity_003_clear_non_empty_lifo():
        # setup
        max_size = 10_000
        elements = list(range(0, max_size))
        test_lifo = Lifo(elements=elements)

        # test
        test_lifo.clear()
        lifo_size = test_lifo.size()
        lifo_empty = test_lifo.empty()
        assert lifo_size == 0, f"Expected Lifo size to be == to 0, got {lifo_size}"
        assert lifo_empty is True, f"Expected Lifo empty to be True, got {lifo_empty}"

    @staticmethod
    def test_000_lifo_capacity_004_push():
        # setup
        max_size = 10_000
        test_lifo = Lifo()

        # test
        for elem in range(0, max_size):
            test_lifo.push(elem)
            lifo_size = test_lifo.size()
            lifo_empty = test_lifo.empty()
            assert lifo_size == elem + 1, f"Expected Lifo size to be == to {elem + 1}, got {lifo_size}"
            assert lifo_empty is False, f"Expected Lifo empty to be False, got {lifo_empty}"

    @staticmethod
    def test_000_lifo_capacity_005_pop():
        # setup
        max_size = 10_000
        test_lifo = Lifo()
        for elem in range(0, max_size):
            test_lifo.push(elem)

        # test
        for elem in range(0, max_size):
            test_lifo.pop()
            lifo_size = test_lifo.size()
            assert lifo_size == max_size - (elem + 1), f"Expected Lifo size to be == to {max_size - (elem + 1)}, " \
                                                       f"got {lifo_size}"

        lifo_empty = test_lifo.empty()
        assert lifo_empty is True, f"Expected Lifo empty to be True, got {lifo_empty}"


class Test001LifoElementAccess:
    @staticmethod
    def test_001_lifo_element_access_000_front_empty_lifo():
        # setup
        test_lifo = Lifo()

        # test
        lifo_front = test_lifo.front()
        assert lifo_front is None, f"Expected Lifo front to be None, got {lifo_front}"

    @staticmethod
    @pytest.mark.parametrize('elements', TEST_LISTS)
    def test_001_lifo_element_access_001_front_non_empty_lifo(elements):
        # setup
        test_lifo = Lifo(elements=elements)

        # test
        lifo_front = test_lifo.front()
        assert lifo_front is elements[-1], f"Expected Lifo front to be {elements[-1]}, got {lifo_front}"

    @staticmethod
    @pytest.mark.parametrize('elements', TEST_LISTS)
    def test_001_lifo_element_access_002_front_after_push(elements):
        # setup
        test_lifo = Lifo()

        # test
        for elem in elements:
            test_lifo.push(element=elem)
            lifo_front = test_lifo.front()
            assert lifo_front is elem, f"Expected Lifo front to be {elem}, got {lifo_front}"

    @staticmethod
    @pytest.mark.parametrize('elements', TEST_LISTS)
    def test_001_lifo_element_access_003_front_after_pop(elements):
        # setup
        size = len(elements)
        test_lifo = Lifo(elements)

        # test
        for index in range(-2, -size, -1):
            test_lifo.pop()
            lifo_front = test_lifo.front()
            assert lifo_front is elements[index], f"Expected Lifo front to be {elements[index]}, got {lifo_front}"

    @staticmethod
    @pytest.mark.parametrize('elements', TEST_LISTS)
    def test_001_lifo_element_access_004_front_after_clear(elements):
        # setup
        test_lifo = Lifo(elements)

        # test
        test_lifo.clear()
        lifo_front = test_lifo.front()
        assert lifo_front is None, f"Expected Lifo front to be None, got {lifo_front}"

    @staticmethod
    def test_001_lifo_element_access_005_back_empty_lifo():
        # setup
        test_lifo = Lifo()

        # test
        lifo_back = test_lifo.back()
        assert lifo_back is None, f"Expected Lifo back to be None, got {lifo_back}"

    @staticmethod
    @pytest.mark.parametrize('elements', TEST_LISTS)
    def test_001_lifo_element_access_006_back_non_empty_lifo(elements):
        # setup
        test_lifo = Lifo(elements=elements)

        # test
        lifo_back = test_lifo.back()
        assert lifo_back is elements[0], f"Expected Lifo back to be {elements[0]}, got {lifo_back}"

    @staticmethod
    @pytest.mark.parametrize('elements', TEST_LISTS)
    def test_001_lifo_element_access_007_back_after_push(elements):
        # setup
        test_lifo = Lifo()

        # test
        for elem in elements:
            test_lifo.push(element=elem)
            lifo_back = test_lifo.back()
            assert lifo_back is elements[0], f"Expected Lifo back to be {elements[0]}, got {lifo_back}"

    @staticmethod
    @pytest.mark.parametrize('elements', TEST_LISTS)
    def test_001_lifo_element_access_008_back_after_pop(elements):
        # setup
        size = len(elements)
        test_lifo = Lifo(elements)

        # test
        for x in range(0, size - 1):
            test_lifo.pop()
            lifo_back = test_lifo.back()
            assert lifo_back is elements[0], f"Expected Lifo back to be {elements[0]}, got {lifo_back}"

    @staticmethod
    @pytest.mark.parametrize('elements', TEST_LISTS)
    def test_001_lifo_element_access_009_back_after_clear(elements):
        # setup
        test_lifo = Lifo(elements)

        # test
        test_lifo.clear()
        lifo_back = test_lifo.back()
        assert lifo_back is None, f"Expected Lifo back to be None, got {lifo_back}"


class Test002LifoModifiers:
    @staticmethod
    @pytest.mark.parametrize('elements', TEST_LISTS)
    def test_002_lifo_modifiers_000_push(elements):
        # setup
        test_lifo = Lifo()

        # test
        for elem in elements:
            test_lifo.push(elem)
            # check front and back
            lifo_front = test_lifo.front()
            lifo_back = test_lifo.back()
            assert lifo_front is elem, f"Expected Lifo front to be {elem}, got {lifo_front}"
            assert lifo_back is elements[0], f"Expected Lifo back to be {elements[0]}, got {lifo_back}"

    @staticmethod
    @pytest.mark.parametrize('elements', TEST_LISTS)
    def test_002_lifo_modifiers_001_pop(elements):
        # setup
        size = len(elements)
        test_lifo = Lifo(elements)

        # test
        for index in range(0, size):
            elem = test_lifo.pop()
            assert elem is elements[-1 - index], f"Expected Fifo pop to be {elements[-1 - index]}, got {elem}"
            # check front and back
            fifo_front = test_lifo.front()
            fifo_back = test_lifo.back()
            if index != (size - 1):
                assert fifo_front is elements[-2 - index], f"Expected Fifo front to be " \
                                                          f"{elements[-2 - index]}, got {fifo_front}"
                assert fifo_back is elements[0], f"Expected Fifo back to be {elements[0]}, got {fifo_back}"
            else:
                assert fifo_front is None, f"Expected Fifo front to be None, got {fifo_front}"
                assert fifo_back is None, f"Expected Fifo back to be None, got {fifo_back}"

        elem = test_lifo.pop()
        assert elem is None, f"Expected Fifo pop to be None, got {elem}"
