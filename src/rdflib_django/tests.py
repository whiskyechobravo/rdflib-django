"""
Unittests and doctests for the rdflib_django app.
"""
import doctest
import rdflib_django
import unittest
from rdflib_django import store


def load_tests(loader, tests, ignore):
    """
    Generate the test suite.
    """
    tests.addTest(doctest.DocTestSuite(rdflib_django))
    tests.addTest(doctest.DocTestSuite(store))
    return tests
