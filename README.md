# 8BitDo Firmware Update Checker

## About
This is just a small utility to check if firmware updates are available for 8BitDo products, in my case the wireless usb adapter. 8BitDo has a useful firmware update utility which shows the latest firmware versions for devices, but I haven't been able to find anywhere that they announce updates. This script checks the same endpoint the firmware updater does, and sends a notification if there's an update to the changelog.

## Usage
I've got this set up as a cron job, and am using IFTTT to forward on the notification. The `type` in the headers defines which device to check updates for, and `beta` determines whether beta firmware should be included.