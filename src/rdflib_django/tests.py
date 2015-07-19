"""
Unittests and doctests for the rdflib_django app.
"""
import doctest
from django.utils import unittest
import rdflib_django
from rdflib_django import store, test_store, test_rdflib, test_seq, test_namespaces


def suite():
    """
    Generate the test suite.
    """
    s = unittest.TestSuite()
    s.addTest(doctest.DocTestSuite(rdflib_django))
    s.addTest(doctest.DocTestSuite(store))
    s.addTest(unittest.findTestCases(test_store))  # pylint: disable=no-member
    s.addTest(unittest.findTestCases(test_rdflib))  # pylint: disable=no-member
    s.addTest(unittest.findTestCases(test_seq))  # pylint: disable=no-member
    s.addTest(unittest.findTestCases(test_namespaces))  # pylint: disable=no-member
    return s
