#!/usr/bin/env python3
"""Generate lightweight hand-drawn-style PNG diagrams for README/tutorial docs."""

from __future__ import annotations

import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parents[1] / "assets" / "diagrams"
W, H = 1600, 900
PAPER = "#f8f1df"
INK = "#2f3a3f"
BLUE = "#7fb3c8"
GREEN = "#a9c89e"
ORANGE = "#e8b36d"
RED = "#dd8c7a"


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
        "/Library/Fonts/Arial.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def jitter(points: list[tuple[int, int]], amount: int = 4) -> list[tuple[int, int]]:
    return [(x + random.randint(-amount, amount), y + random.randint(-amount, amount)) for x, y in points]


def paper() -> tuple[Image.Image, ImageDraw.ImageDraw]:
    random.seed(7)
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    for _ in range(1400):
        x, y = random.randrange(W), random.randrange(H)
        c = random.choice(["#f3e8cf", "#fff8e8", "#efe1c2"])
        draw.point((x, y), fill=c)
    return img, draw


def box(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], label: str, fill: str) -> None:
    x1, y1, x2, y2 = xy
    for offset in range(3):
        draw.rounded_rectangle((x1 + offset, y1 + offset, x2 + offset, y2 + offset), radius=24, outline=INK, width=3, fill=fill if offset == 0 else None)
    lines = label.split("\n")
    f = font(36)
    total_h = len(lines) * 44
    y = y1 + ((y2 - y1) - total_h) // 2
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=f)
        draw.text((x1 + ((x2 - x1) - (bbox[2] - bbox[0])) // 2, y), line, fill=INK, font=f)
        y += 44


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str = INK) -> None:
    pts = jitter([start, ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2), end], 5)
    draw.line(pts, fill=color, width=5)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    for delta in (2.6, -2.6):
        p = (end[0] - int(28 * math.cos(angle + delta)), end[1] - int(28 * math.sin(angle + delta)))
        draw.line([end, p], fill=color, width=5)


def title(draw: ImageDraw.ImageDraw, text: str, subtitle: str) -> None:
    draw.text((80, 48), text, fill=INK, font=font(54))
    draw.text((84, 118), subtitle, fill="#5d676b", font=font(28))


def save(img: Image.Image, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    img.save(OUT / name)


def overview() -> None:
    img, draw = paper()
    title(draw, "Research-to-Paper Harness", "From public health data to an SCI submission package")
    items = [
        ((80, 290, 300, 430), "Data", BLUE),
        ((350, 290, 570, 430), "Research\nQuestion", GREEN),
        ((620, 290, 840, 430), "Analysis", ORANGE),
        ((890, 290, 1110, 430), "Manuscript", BLUE),
        ((1160, 290, 1380, 430), "Review", GREEN),
        ((570, 620, 1030, 770), "Submission\nPackage", ORANGE),
    ]
    for rect, label, fill in items:
        box(draw, rect, label, fill)
    for x in [300, 570, 840, 1110]:
        arrow(draw, (x + 15, 360), (x + 45, 360))
    arrow(draw, (1270, 440), (820, 610))
    save(img, "01-overview-japanese-handdrawn.png")


def checkpoint_loop() -> None:
    img, draw = paper()
    title(draw, "Checkpoint-First Loop", "No stage advances until the human confirms the artifact")
    nodes = [
        ((120, 340, 360, 480), "Plan", BLUE),
        ((500, 200, 820, 340), "Produce\nArtifact", GREEN),
        ((980, 340, 1220, 480), "Validate", ORANGE),
        ((820, 620, 1180, 760), "Human\nConfirm", RED),
        ((300, 620, 620, 760), "Next\nStage", BLUE),
    ]
    for rect, label, fill in nodes:
        box(draw, rect, label, fill)
    arrow(draw, (360, 360), (500, 280))
    arrow(draw, (820, 280), (980, 360))
    arrow(draw, (1100, 480), (1000, 620))
    arrow(draw, (820, 690), (620, 690))
    arrow(draw, (300, 620), (220, 480))
    draw.text((690, 520), "STOP: no auto-continue", fill="#9a4b3f", font=font(34))
    save(img, "02-checkpoint-loop-japanese-handdrawn.png")


def architecture() -> None:
    img, draw = paper()
    title(draw, "Academic Research Harness", "A small engineering layer around AI research work")
    boxes = [
        ((80, 250, 360, 390), "Skill\nRouter", BLUE),
        ((450, 250, 730, 390), "Workflow", GREEN),
        ((820, 250, 1120, 390), "Stage\nContract", ORANGE),
        ((1200, 250, 1500, 390), "State\nJSON", BLUE),
        ((450, 570, 730, 710), "Validator", RED),
        ((820, 570, 1120, 710), "Artifacts", GREEN),
        ((1200, 570, 1500, 710), "Human\nConfirm", ORANGE),
    ]
    for rect, label, fill in boxes:
        box(draw, rect, label, fill)
    arrow(draw, (360, 320), (450, 320))
    arrow(draw, (730, 320), (820, 320))
    arrow(draw, (1120, 320), (1200, 320))
    arrow(draw, (1350, 390), (1350, 570))
    arrow(draw, (1200, 640), (1120, 640))
    arrow(draw, (820, 640), (730, 640))
    arrow(draw, (590, 570), (590, 400))
    save(img, "03-harness-architecture-japanese-handdrawn.png")


def nhanes_case() -> None:
    img, draw = paper()
    title(draw, "NHANES Case Path", "A small public dataset becomes tables, figures, and a Word package")
    nodes = [
        ((80, 300, 360, 450), "NHANES\nSmall Pack", BLUE),
        ((430, 300, 710, 450), "Survey\nAnalysis", GREEN),
        ((780, 190, 1060, 340), "Table\n1 / 2", ORANGE),
        ((780, 470, 1060, 620), "Figures", BLUE),
        ((1130, 300, 1410, 450), "Manuscript\nDOCX", GREEN),
    ]
    for rect, label, fill in nodes:
        box(draw, rect, label, fill)
    arrow(draw, (360, 375), (430, 375))
    arrow(draw, (710, 350), (780, 270))
    arrow(draw, (710, 400), (780, 540))
    arrow(draw, (1060, 270), (1130, 350))
    arrow(draw, (1060, 540), (1130, 400))
    draw.text((520, 690), "checkpointed S0-S9 trail", fill="#5d676b", font=font(36))
    save(img, "04-nhanes-case-path-japanese-handdrawn.png")


def main() -> None:
    overview()
    checkpoint_loop()
    architecture()
    nhanes_case()


if __name__ == "__main__":
    main()
