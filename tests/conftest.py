# coding=utf-8
from __future__ import unicode_literals

import pytest


pytest_plugins = ["pytester"]


@pytest.fixture
def one_test_passing(testdir):
    testdir.makepyfile("""
        def test_passing():
            assert True
    """)


@pytest.fixture
def two_tests_failing(testdir):
    testdir.makepyfile("""
        def test_failing():
            assert False

        def test_raises():
            raise Exception
    """)


@pytest.fixture
def errors_in_setup_and_teardown_conftest(testdir):
    testdir.makeconftest("""
        import pytest


        @pytest.fixture
        def error_in_setup():
            raise Exception


        @pytest.fixture
        def error_in_teardown():
            yield
            raise Exception
    """)


@pytest.fixture
def bunch_of_skipped_tests(testdir, errors_in_setup_and_teardown_conftest):
    testdir.makepyfile("""
        import pytest


        @pytest.mark.skip
        def test_skip():
            pass


        @pytest.mark.skip
        def test_error_in_setup_and_test_is_skipped(error_in_setup):
            pass


        @pytest.mark.skip
        def test_error_in_teardown_and_test_is_skipped(error_in_teardown):
            pass


        @pytest.mark.skipif(True, reason="conditional skip, skipped")
        def test_skipif_true():
            pass


        @pytest.mark.skipif(False, reason="conditional skip, not skipped")
        def test_skipif_false():
            pass


        @pytest.mark.xfail
        @pytest.mark.skip
        def test_skip_and_xfail():
            pass


        @pytest.mark.skip
        @pytest.mark.xfail
        def test_xfail_and_skip():
            pass


        def test_skipped_within_test():
            pytest.skip()
    """)


@pytest.fixture
def errors_in_setup_and_teardown(testdir, errors_in_setup_and_teardown_conftest):
    testdir.makepyfile("""
        def test_error_in_setup(error_in_setup):
            pass


        def test_error_in_teardown(error_in_teardown):
            pass


        def test_errors_in_setup_and_teardown(error_in_setup, error_in_teardown):
            pass
    """)


@pytest.fixture
def xfail_tests(testdir):
    testdir.makepyfile("""
        import pytest


        @pytest.mark.xfail
        def test_expected_fail_but_passes():
            assert True


        @pytest.mark.xfail
        def test_expected_fail_and_fails():
            assert False


        @pytest.mark.xfail(strict=True)
        def test_expected_fail_but_passes_strict():
            assert True


        @pytest.mark.xfail(strict=True)
        def test_expected_fail_and_fails_strict():
            assert False


        @pytest.mark.xfail
        def test_error_in_setup_and_expected_fail_mark(error_in_setup):
            pass


        @pytest.mark.xfail
        def test_error_in_teardown_and_expected_fail_mark(error_in_teardown):
            pass
    """)


@pytest.fixture
def one_of_each_result_type(errors_in_setup_and_teardown_conftest, testdir):
    testdir.makepyfile("""
        import pytest

        def test_passed():
            assert True

        @pytest.mark.xfail
        def test_xpassed():
            assert True

        def test_failed():
            assert False

        @pytest.mark.xfail
        def test_xfailed():
            assert False        

        def test_skipped():
            pytest.skip()

        def test_error(error_in_setup):
            assert True
    """)


@pytest.fixture
def symbols_in_inifile(testdir):
    testdir.makeini("""
        [pytest]

        report_passed = ✔
        report_xpassed = 🦄
        report_failed = ✗
        report_xfailed = !
        report_skipped = ?
        report_error = 🔥

        report_passed_verbose = OH YEAH
        report_xpassed_verbose = WHAT IN TARNATION?
        report_failed_verbose = OH CRAP
        report_xfailed_verbose = YEAH WHATEVER
        report_skipped_verbose = DON'T CARE
        report_error_verbose = YOU MEDDLING KIDS!
    """)
