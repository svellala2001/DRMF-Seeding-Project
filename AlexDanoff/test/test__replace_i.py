from unittest import TestCase
from replace_special import replace_special


class Test_replace_special(TestCase):
    def test__replace_special(self):
        tex = 'z^a = \\underbrace{z \\cdot z \\cdots z}_{n \\text{ times}} = 1 / z^{-a}.'
        result = replace_special(tex)
        self.assertEqual(tex, result)
