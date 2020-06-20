from unittest import TestCase
from unittest.mock import patch, call

import cuisine.__main__


class TestMain(TestCase):
    def test_main(self):
        with patch("sys.argv", ["test", "jajca"]):
            cuisine.__main__.main()