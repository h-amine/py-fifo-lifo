from src.lifo import Lifo


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

