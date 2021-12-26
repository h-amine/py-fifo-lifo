from src.fifo import Fifo


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

