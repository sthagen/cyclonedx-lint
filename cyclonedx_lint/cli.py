"""Visit folder tree with CycloneDX documents, validate the latter, and generate reports."""
import sys
from typing import no_type_check

import cyclonedx_lint.lint as cyclonedx_lint


@no_type_check
def main(argv=None):
    """Process the job."""
    argv = sys.argv[1:] if argv is None else argv
    cyclonedx_lint.parse(argv)
