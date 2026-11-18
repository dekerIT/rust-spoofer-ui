# Rust Spoofer — UI Prototype

![Platform](https://img.shields.io/badge/Platform-Windows%2010%20%7C%2011-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Language](https://img.shields.io/badge/C%2B%2B-17-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Framework](https://img.shields.io/badge/UI-Clean%20Win32-5C2D91?style=for-the-badge&logo=microsoft&logoColor=white)
![Status](https://img.shields.io/badge/Status-Visual%20Prototype-2ea44f?style=for-the-badge)

This repository contains a dark-themed Win32 interface prototype named **Rust Spoofer**.

> [!IMPORTANT]
> This project is UI demonstration software only. It does not read or change HWIDs, install or communicate with drivers, bypass hardware bans, interfere with Easy Anti-Cheat or other anti-cheat systems, or modify Rust or Windows security components.

## Preview

<p align="center">
  <img src="resources/preview.png" alt="Rust Spoofer UI prototype preview" width="600">
</p>

The application window is approximately 600×350 pixels and includes:

- A custom dark title bar and borderless window
- A red Rust-style logo placeholder
- A status section for `Ready`, `Spoofing...`, and `Successfully spoofed!`
- A wide prototype button
- A small application footer

## Prototype Behavior

Clicking **Spoof HWID** only demonstrates local UI transitions:

1. The button becomes disabled.
2. `Status` changes from `Ready` to `Spoofing...`.
3. The UI waits for 2.5 seconds.
4. `HWID` displays `Successfully spoofed!`.
5. `Status` returns to `Ready`.
6. The button becomes enabled again.

No operating system identifiers or security products are accessed.

## Technology

- C++17
- Win32 API
- GDI+
- Common Controls v6
- CMake
- Visual Studio 2022

No Qt or third-party runtime framework is required.

## Project Structure

```text
rust-spoofer-ui/
│
├── main.py
├── rust_logo.png
├── requirements.txt
├── README.md
├── .gitignore
│
└── assets/
    └── screenshot.png
```

## Disclaimer

This project is a visual UI demonstration.

The HWID functionality is simulated and does not perform actual hardware identification modification, system changes, or game-ban bypass operations.

Rust is a trademark of Facepunch Studios. This is an independent fan-made project and is not affiliated with or endorsed by Facepunch Studios.

## License

No license has been granted at this time. All rights reserved unless otherwise stated.
