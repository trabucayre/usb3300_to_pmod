from migen import *

from litex.build.generic_platform import *

def add_usb3300_pmod(name="ulpi_ext", j3="pmodc", j2="pmodb", iostd="LVCMOS33"):
    return [
        (name, 0,
            Subsignal("rst",   Pins(f"{j2}:7")),
            Subsignal("clk_n", Pins(f"{j2}:6")),
            Subsignal("dir",   Pins(f"{j2}:3")),
            Subsignal("nxt",   Pins(f"{j2}:1")),
            Subsignal("stp",   Pins(f"{j2}:0")),
            Subsignal("data",  Pins(f"{j3}:3 {j3}:7 {j3}:2 {j3}:6 {j3}:1 {j3}:5 {j3}:0 {j3}:4")),
            IOStandard(iostd)
        ),
    ]
