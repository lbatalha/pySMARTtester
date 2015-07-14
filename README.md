# pySMARTtester
Simple script used to run smart self-tests on multiple drives at once

###Usage:

`-t : --test <test_type>`
`-h : --help`

####Test types:
  - short: Short SMART self-test (`smartctl -t short`)
  - long: Extended SMART self-test (`smartctl -t long`)
  - badblocks: runs `badblocks` with default settings and `-o /<log_path>/badblocks-<drive_path>`
