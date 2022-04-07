# coding=utf-8
from __future__ import unicode_literals

import pytest_custom_report


def test_pass_custom_symbol(testdir, one_test_passing):
    result = testdir.runpytest('--report-passed=👍')
    result.stdout.fnmatch_lines([
        'test_pass_custom_symbol.py 👍 *',
    ])
    assert result.ret == 0
    result.assert_outcomes(passed=1)


def test_pass_custom_symbol_verbose(testdir, one_test_passing):
    result = testdir.runpytest('--report-passed-verbose=OHYEAH', '-v')
    result.stdout.fnmatch_lines([
        'test_pass_custom_symbol_verbose.py::test_passing OHYEAH *',
    ])
    assert result.ret == 0
    result.assert_outcomes(passed=1)


def test_fail_custom_symbol(testdir, two_tests_failing):
    result = testdir.runpytest('--report-failed=💩')
    result.stdout.fnmatch_lines([
        'test_fail_custom_symbol.py 💩💩 *',
    ])
    assert result.ret == 1
    result.assert_outcomes(failed=2)


def test_fail_custom_symbol_verbose(testdir, two_tests_failing):
    result = testdir.runpytest('--report-failed-verbose=OHCRAP', '-v')
    result.stdout.fnmatch_lines([
        'test_fail_custom_symbol_verbose.py::test_failing OHCRAP *',
        'test_fail_custom_symbol_verbose.py::test_raises OHCRAP *',
    ])
    assert result.ret == 1
    result.assert_outcomes(failed=2)


def test_skip_custom_symbol(testdir, bunch_of_skipped_tests):
    result = testdir.runpytest('--report-skipped=?')
    result.stdout.fnmatch_lines([
        'test_skip_custom_symbol.py ????.??? *',
    ])
    assert result.ret == 0
    result.assert_outcomes(passed=1, skipped=7)


def test_skip_custom_symbol_verbose(testdir, bunch_of_skipped_tests):
    result = testdir.runpytest('--report-skipped-verbose=WHATEVS', '--verbose')
    result.stdout.fnmatch_lines([
        'test_skip_custom_symbol_verbose.py::test_skip WHATEVS *',
        'test_skip_custom_symbol_verbose.py::test_error_in_setup_and_test_is_skipped WHATEVS *',
        'test_skip_custom_symbol_verbose.py::test_error_in_teardown_and_test_is_skipped WHATEVS *',
        'test_skip_custom_symbol_verbose.py::test_skipif_true WHATEVS *',
        'test_skip_custom_symbol_verbose.py::test_skipif_false PASSED *',
        'test_skip_custom_symbol_verbose.py::test_skip_and_xfail WHATEVS *',
        'test_skip_custom_symbol_verbose.py::test_xfail_and_skip WHATEVS *',
        'test_skip_custom_symbol_verbose.py::test_skipped_within_test WHATEVS *',
    ])
    assert result.ret == 0
    result.assert_outcomes(passed=1, skipped=7)


def test_error_in_setup_and_teardown(testdir, errors_in_setup_and_teardown):
    result = testdir.runpytest('--report-error=!')
    result.stdout.fnmatch_lines([
        'test_error_in_setup_and_teardown.py !.!! *',
    ])
    assert result.ret == 1
    result.assert_outcomes(passed=1, errors=3)


def test_error_in_setup_and_teardown_verbose(testdir, errors_in_setup_and_teardown):
    result = testdir.runpytest('--report-error-verbose=UHOH', '--verbose')
    result.stdout.fnmatch_lines([
        'test_error_in_setup_and_teardown_verbose.py::test_error_in_setup UHOH *',
        'test_error_in_setup_and_teardown_verbose.py::test_error_in_teardown PASSED *',
        'test_error_in_setup_and_teardown_verbose.py::test_error_in_teardown UHOH *',
        'test_error_in_setup_and_teardown_verbose.py::test_errors_in_setup_and_teardown UHOH *',
    ])
    assert result.ret == 1
    result.assert_outcomes(passed=1, errors=3)


def test_xfail(testdir, xfail_tests):
    result = testdir.runpytest(
        '--report-failed=f',
        '--report-xfailed=✗',
        '--report-xpassed=P',
    )
    result.stdout.fnmatch_lines([
        'test_xfail.py P✗f✗✗✗ *',
    ])
    assert result.ret == 1
    result.assert_outcomes(xpassed=1, failed=1, xfailed=4)


def test_xfail_verbose(testdir, xfail_tests):
    result = testdir.runpytest(
        '--report-failed-verbose=WTF',
        '--report-xfailed-verbose=SHRUGS',
        r'--report-xpassed-verbose=¯\_(ツ)_/¯',
        '-v',
    )
    result.stdout.fnmatch_lines([
        r'test_xfail_verbose.py::test_expected_fail_but_passes ¯\_(ツ)_/¯ *',
        'test_xfail_verbose.py::test_expected_fail_and_fails SHRUGS *',
        'test_xfail_verbose.py::test_expected_fail_but_passes_strict WTF *',
        'test_xfail_verbose.py::test_expected_fail_and_fails_strict SHRUGS *',
        'test_xfail_verbose.py::test_error_in_setup_and_expected_fail_mark SHRUGS *',
        'test_xfail_verbose.py::test_error_in_teardown_and_expected_fail_mark SHRUGS *',
    ])
    assert result.ret == 1
    result.assert_outcomes(xpassed=1, failed=1, xfailed=4)


def test_report_symbols_parsed_from_ini_file(testdir, symbols_in_inifile, one_of_each_result_type):
    result = testdir.runpytest()
    result.stdout.fnmatch_lines([
        'test_report_symbols_parsed_from_ini_file.py ✔🦄✗!?🔥  *',
    ])
    result.assert_outcomes(passed=1, skipped=1, failed=1, errors=1, xfailed=1, xpassed=1)


def test_report_symbols_parsed_from_ini_file_verbose(testdir, symbols_in_inifile, one_of_each_result_type):
    result = testdir.runpytest('--verbose')
    result.stdout.fnmatch_lines([
        'test_report_symbols_parsed_from_ini_file_verbose.py::test_passed OH YEAH [ 16%]',
        'test_report_symbols_parsed_from_ini_file_verbose.py::test_xpassed WHAT IN TARNATION? [ 33%]',
        'test_report_symbols_parsed_from_ini_file_verbose.py::test_failed OH CRAP [ 50%]',
        'test_report_symbols_parsed_from_ini_file_verbose.py::test_xfailed YEAH WHATEVER [ 66%]',
        "test_report_symbols_parsed_from_ini_file_verbose.py::test_skipped DON'T CARE [ 83%]",
        'test_report_symbols_parsed_from_ini_file_verbose.py::test_error YOU MEDDLING KIDS! [100%]',
    ])
    result.assert_outcomes(passed=1, skipped=1, failed=1, errors=1, xfailed=1, xpassed=1)
    outcomes = result.parseoutcomes()
    assert outcomes == {"passed": 1, "skipped": 1, "failed": 1, "xpassed": 1, "xfailed": 1, "errors": 1}


def test_default_symbols():
    assert pytest_custom_report.symbols == {
        (False, 'failed',  'call'):     ('failed',  'F', 'FAILED'),
        (False, 'failed',  'setup'):    ('error',   'E', 'ERROR'),
        (False, 'failed',  'teardown'): ('error',   'E', 'ERROR'),
        (False, 'passed',  'call'):     ('passed',  '.', 'PASSED'),
        (False, 'skipped', 'call'):     ('skipped', 's', 'SKIPPED'),
        (False, 'skipped', 'setup'):    ('skipped', 's', 'SKIPPED'),
        (True,  'passed',  'call'):     ('xpassed', 'X', 'XPASS'),
        (True,  'skipped', 'call'):     ('xfailed', 'x', 'XFAIL'),
        (True,  'skipped', 'setup'):    ('xfailed', 'x', 'XFAIL'),
        (True,  'skipped', 'teardown'): ('xfailed', 'x', 'XFAIL'),
    }


expected_cli_options = '''\
custom-report:
  --report-passed=*
  --report-passed-verbose=*
  --report-xpassed=*
  --report-xpassed-verbose=*
  --report-failed=*
  --report-failed-verbose=*
  --report-xfailed=*
  --report-xfailed-verbose=*
  --report-skipped=*
  --report-skipped-verbose=*
  --report-error=*
  --report-error-verbose=*
'''.splitlines()


expected_ini_options = '''\
  report_passed (string)*
  report_passed_verbose (string)*
  report_xpassed (string)*
  report_xpassed_verbose (string)*
  report_failed (string)*
  report_failed_verbose (string)*
  report_xfailed (string)*
  report_xfailed_verbose (string)*
  report_skipped (string)*
  report_skipped_verbose (string)*
  report_error (string)*
  report_error_verbose (string)*
'''.splitlines()


def test_help_text_contains_cli_options(testdir):
    result = testdir.runpytest('--help')
    result.stdout.fnmatch_lines(expected_cli_options)


def test_help_text_contains_ini_options(testdir):
    result = testdir.runpytest('--help')
    result.stdout.fnmatch_lines(expected_ini_options)
