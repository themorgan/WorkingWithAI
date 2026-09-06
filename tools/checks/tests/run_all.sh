#!/bin/bash
# GENERATED FILE -- do not hand-edit. Written by tools/precedent_materialize.py
# on every sync; any edit here is overwritten without warning.
#
# Runs every materialized check's two-direction test. The glob is the point:
# this driver runs whatever tests this repo actually materialized, which is
# why it is generated here rather than copied from any one practice source.
set -uo pipefail
cd "$(dirname "$0")"
status=0
for t in test_*.sh; do
  # A repo that materialized no tests leaves the glob unexpanded; without
  # this the driver would try to run a file literally named test_*.sh and
  # report a failure that is really an empty set.
  [ -e "$t" ] || continue
  echo "--- $t ---"
  if ! bash "$t"; then
    status=1
  fi
done
exit $status
