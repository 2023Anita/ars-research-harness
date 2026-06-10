#!/usr/bin/env python3
"""Download the NHANES 2017-2018 small pack used by the example workflow."""

from __future__ import annotations

from pathlib import Path
from urllib.request import urlretrieve


FILES = {
    "DEMO_J.xpt": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DEMO_J.XPT",
    "BMX_J.xpt": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/BMX_J.XPT",
    "BPX_J.xpt": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/BPX_J.XPT",
    "DIQ_J.xpt": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DIQ_J.XPT",
    "GHB_J.xpt": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/GHB_J.XPT",
    "GLU_J.xpt": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/GLU_J.XPT",
    "BPQ_J.xpt": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/BPQ_J.XPT",
    "TCHOL_J.xpt": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/TCHOL_J.XPT",
    "HDL_J.xpt": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/HDL_J.XPT",
    "PAQ_J.xpt": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/PAQ_J.XPT",
    "SMQ_J.xpt": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/SMQ_J.XPT",
    "SLQ_J.xpt": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/SLQ_J.XPT",
}


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    raw_dir = root / "data" / "nhanes_2017_2018" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    for name, url in FILES.items():
        target = raw_dir / name
        if target.exists() and target.stat().st_size > 0:
            print(f"skip {name}")
            continue
        print(f"download {name}")
        urlretrieve(url, target)


if __name__ == "__main__":
    main()
