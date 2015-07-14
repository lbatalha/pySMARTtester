# pySMARTtester
Simple script used to run smart self-tests on multiple drives at once

###Usage:
- Type of test to run
  - `-t, --test <test_type>`
- Show Options
  - `-h, --help`

####Test types:
  - short: Short SMART self-test (`smartctl -t short`)
  - long: Extended SMART self-test (`smartctl -t long`)
  - badblocks: runs `badblocks` with default settings and `-o /<log_path>/badblocks-<drive_path>`

##Dependencies:
  - [smartmontools](https://www.smartmontools.org/)
  - [badblocks (e2fsprogs)](http://e2fsprogs.sourceforge.net/) - Only for `-t badblocks`
