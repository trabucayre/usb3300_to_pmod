# Waveshare USB3300 to dual PMOD PCB adapter

This repository is dedicated to a PCB adapter for the
[Waveshare USB3300 USB HS Board](https://www.waveshare.com/wiki/USB3300_USB_HS_Board).

The Waveshare module exposes the **USB3300 ULPI** interface on a 2x10 2.54 mm
header. Wiring this header to an FPGA board with loose jumpers can easily cause
signal integrity issues, especially with the 60 MHz `CLKOUT` signal and the
8-bit ULPI data bus.

This adapter converts the Waveshare 2x10 header to two standard 2x6 PMOD-style
connectors:

- `J3` carries the 8-bit ULPI data bus.
- `J2` carries the ULPI control signals, clock and reset.
- `J4` is the 2x10 connector for the Waveshare USB3300 board.
- `J1` exposes `+5V` and `GND`.

The board is passive: it does not include level shifters, buffers or regulators.
The FPGA board must be compatible with 3.3 V I/O for the ULPI signals.

<center><img width=800 alt="waveshare_usb3300_to_dual_pmod" src=picts/waveshare_usb3300_to_dual_pmod.png /></center>

## Connector mapping

The PMOD connectors are dual-row 2x6 headers. Pins `1` to `6` are on the first
row, and pins `7` to `12` are on the second row.

### PMOD J3: ULPI data bus

| Row 1 pin | Signal  | Row 2 pin | Signal  |
| --------- | ------- | --------- | ------- |
| 1         | `DATA6` |  7        | `DATA7` |
| 2         | `DATA4` |  8        | `DATA5` |
| 3         | `DATA2` |  9        | `DATA3` |
| 4         | `DATA0` | 10        | `DATA1` |
| 5         | `GND`   | 11        | `GND`   |
| 6         | `+3.3V` | 12        | `+3.3V` |

### PMOD J2: ULPI control

| Row 1 pin | Signal  | Row 2 pin |  Signal  |
| --------- | ------- | --------- | -------- |
| 1         | `STP`   |  7        | NC       |
| 2         | `NXT`   |  8        | NC       |
| 3         | NC      |  9        | `CLKOUT` |
| 4         | `DIR`   | 10        | `RESET`  |
| 5         | `GND`   | 11        | `GND`    |
| 6         | `+3.3V` | 12        | `+3.3V`  |

### Waveshare USB3300 header J4

| J4 pin | Signal   | J4 pin | Signal  |
| ------ | -------- | ------ | ------- |
|  1     | `+5V`    |  2     | `DATA0` |
|  3     | `+5V`    |  4     | `DATA1` |
|  5     | NC       |  6     | `DATA2` |
|  7     | `RESET`  |  8     | `DATA3` |
|  9     | `CLKOUT` | 10     | `DATA4` |
| 11     | `DIR`    | 12     | `DATA5` |
| 13     | `NXT`    | 14     | `DATA6` |
| 15     | `STP`    | 16     | `DATA7` |
| 17     | `GND`    | 18     | `GND`   |
| 19     | `+3.3V`  | 20     | `+3.3V` |

## Electrical notes

- The adapter routes the ULPI bus directly between the Waveshare board and the
  PMOD connectors.
- `+3.3V` is distributed to the PMOD power pins and to the Waveshare header.
- `+5V` is routed to the Waveshare header and to the auxiliary `J1` header (Only
  required in device mode).
- Use short PMOD connections and keep both PMOD connectors attached to the same
  FPGA bank when possible.
- Verify the target board pinout before connecting. Not all 2x6 connectors use
  the same PMOD orientation or power-pin placement.

## Examples

The `examples` directory contains modified LiteX targets using the USB3300 as a
USB CDC ACM UART.

### Prerequisites

Using CDC ACM requires [amaranth](https://github.com/amaranth-lang/amaranth),
[Luna](https://github.com/greatscottgadgets/luna) and
[LiteX](https://github.com/enjoy-digital/litex).

**amaranth**

```bash
git clone https://github.com/amaranth-lang/amaranth.git
cd amaranth
# v0.5.8 is required by Luna
git checkout v0.5.8
pip3 install --user --break-system-packages -e .
cd ..
```

**Luna**

```bash
git clone https://github.com/greatscottgadgets/luna.git
cd luna
git checkout 0.2.3
# A commit has introduced a regression and must be reverted
# (https://github.com/greatscottgadgets/luna/issues/280)
git revert --no-edit cf6abaae922bd3f04ca6118f0a7d26b768859d28
pip3 install --user --break-system-packages -e .
cd ..
```

**LiteX**

This step is well documented in the
[official page](https://github.com/enjoy-digital/litex/#quick-start-guide)

### Build

To build a gateware image, use:

```bash
cd examples
./board_name.py --uart-name usb_acm --build --load
```

Where `board_name.py` may be:

- `digilent_arty_s7.py`

  <img width=400 alt="digilent_arty_s7" src=picts/digilent_arty_s7.jpeg />
- `sipeed_tang_mega_138k.py`

  <img width=400 alt="sipeed_tang_mega_138k" src=picts/sipeed_tang_mega_138k.jpeg />
- `arrow_axe5000.py`
  Requires the [Ziggy Bridge MKR](https://github.com/steieio/ziggybridge-mkr)

  <img width=400 alt="arrow_axe5000" src=picts/arrow_axe5000.jpg />

## Contact

E-mail: Gwenhael Goavec-Merou <gwenhael.goavec-merou@trabucayre.com></br>
Copyright (C) <b>2026</b></br>
