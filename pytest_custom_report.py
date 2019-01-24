"""Custom report symbols for pass/fail/skip"""

names = "passed xpassed failed xfailed skipped error".split()
defaults = dict(zip(names, ".XFxsE"))
help = """
symbol to use in the report when a test has passed (default {passed})
symbol to use when a test is marked as an expected failure, but it doesn't fail (default {xpassed})
symbol to use when a test fails, either by assertion or an unhandled exception (default {failed})
symbol to use when a test fails, but it is marked as an expected failure (default {xfailed})
symbol to use when a test is skipped, e.g. by @pytest.skip decorator (default {skipped})
symbol to use when a test encounters an exception during setup or teardown (default {error})
"""
help = dict(zip(names, help.strip().format(**defaults).splitlines()))
defaults_verbose = "PASSED XPASS FAILED XFAIL SKIPPED ERROR".split()
msg_verbose = "as above, when '--verbose' is enabled (default {})"
help_verbose = [msg_verbose.format(v) for v in defaults_verbose]
defaults_verbose = dict(zip(names, defaults_verbose))
help_verbose = dict(zip(names, help_verbose))
symbols = {}


def pytest_addoption(parser):
    group = parser.getgroup("custom-report")
    for name in names:
        group.addoption("--report-" + name, help=help[name])
        group.addoption("--report-" + name + "-verbose", help=help_verbose[name])
        parser.addini("report_" + name, default=defaults[name], help=help[name])
        parser.addini("report_" + name + "_verbose", default=defaults_verbose[name], help=help_verbose[name])


def pytest_configure(config):
    # this is called once after command line args have been parsed

    def get(name):
        # returns a 3-tuple of short and verbose strings, along with the test outcome string
        # the command line arguments, if specified, take precedence over config file settings
        if name not in names:
            return
        short = config.getoption("report_" + name, None)
        if short is None:
            short = config.getini("report_" + name)
        long = config.getoption("report_" + name + "_verbose", None)
        if long is None:
            long = config.getini("report_" + name + "_verbose")
        return name, short, long

    symbols.update({
        # was expected fail, outcome, when: category, short symbol, verbose symbol
        (False, "failed",  "setup"):    get("error"),
        (False, "failed",  "teardown"): get("error"),
        (False, "skipped", "setup"):    get("skipped"),
        (False, "skipped", "call"):     get("skipped"),
        (False, "passed",  "call"):     get("passed"),
        (False, "failed",  "call"):     get("failed"),
        (True,  "passed",  "call"):     get("xpassed"),
        (True,  "skipped", "setup"):    get("xfailed"),
        (True,  "skipped", "call"):     get("xfailed"),
        (True,  "skipped", "teardown"): get("xfailed"),
    })


def pytest_report_teststatus(report):
    return symbols.get((hasattr(report, "wasxfail"), report.outcome, report.when))
