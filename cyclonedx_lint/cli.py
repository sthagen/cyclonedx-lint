#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long
""""Visit folder tree with CycloneDX documents, validate the latter, and generate reports."""
import os
import sys

import cyclonedx_lint.lint as cyclonedx_lint


# pylint: disable=expression-not-assigned
def main(argv=None):
    """Process the job."""
    argv = sys.argv[1:] if argv is None else argv
    cyclonedx_lint.main(argv)
 
