#!/usr/bin/env python3

import os
import time

from MiSmSerial import MiSmSerial


if os.name == "nt":
    PORT = "COM3"
else:
    PORT = "/dev/ttyACM0"

BAUD = 9600
DELAY = 1.0

OUTPUTS = [
    "Q0030",
    "Q0031",
    "Q0032",
    "Q0033",
    "Q0034",
    "Q0035",
    "Q0036",
    "Q0037",
]


plc = MiSmSerial(
    PORT,
    device="FF",
    baud=BAUD,
    timeout=1.0,
    debug=False,
    bcc_mode="auto",
)


def set_output(q, state):
    y = "Y" + q[1:]

    plc.output(q, state)
    readback = plc.read_bit(y)

    print(
        f"{q}: command={'ON ' if state else 'OFF'} "
        f"readback={readback}"
    )


try:
    print(f"Connected on {PORT}")
    print("FC6A-T08P4 output test")
    print()

    print("Setting all outputs OFF")
    for q in OUTPUTS:
        set_output(q, 0)

    print()
    print("Walking outputs Q0030-Q0037")
    print()

    for q in OUTPUTS:
        print(f"Testing {q}")

        set_output(q, 1)
        time.sleep(DELAY)

        set_output(q, 0)
        time.sleep(0.25)

    print()
    print("Test complete")

finally:
    print()
    print("Turning all test outputs OFF")

    for q in OUTPUTS:
        try:
            plc.output(q, 0)
        except Exception as e:
            print(f"Could not turn off {q}: {e}")

    plc.close()
