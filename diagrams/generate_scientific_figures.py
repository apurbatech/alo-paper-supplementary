#!/usr/bin/env python3
"""Generate the three scientific figures used by the ALO manuscript.

All plotted values are transcribed from ALO_Screen_Reader_Paper.tex.  The
script deliberately writes vector PDF and SVG files in addition to PNG
previews so that every number and visual encoding remains reproducible.
"""

from __future__ import annotations

import os
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
os.environ.setdefault("MPLCONFIGDIR", str(SCRIPT_DIR / ".mplconfig"))

import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


# Colorblind-safe Okabe-Ito-derived palette.
BLUE = "#0072B2"
SKY = "#56B4E9"
ORANGE = "#E69F00"
GREEN = "#009E73"
VERMILLION = "#D55E00"
PURPLE = "#CC79A7"
DARK = "#263645"
MID = "#66737F"
GRID = "#D7DEE3"
PALE_BLUE = "#EAF4FA"
PALE_ORANGE = "#FFF4DD"
PALE_GREEN = "#E9F6F1"
PALE_PURPLE = "#F8ECF5"
PALE_RED = "#FBEDEA"
WHITE = "#FFFFFF"

mpl.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial Unicode MS", "Arial", "Helvetica", "DejaVu Sans"],
        "font.size": 8,
        "axes.titlesize": 8.5,
        "axes.labelsize": 7.5,
        "xtick.labelsize": 7,
        "ytick.labelsize": 7,
        "legend.fontsize": 7,
        "axes.edgecolor": DARK,
        "axes.labelcolor": DARK,
        "xtick.color": DARK,
        "ytick.color": DARK,
        "text.color": DARK,
        "svg.fonttype": "none",
        "pdf.fonttype": 42,
        "savefig.facecolor": WHITE,
        "figure.facecolor": WHITE,
    }
)


def panel_title(ax, label: str, title: str) -> None:
    ax.text(
        0.0,
        1.02,
        f"({label})",
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=9,
        fontweight="bold",
    )
    ax.text(
        0.14,
        1.02,
        title,
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=8.5,
        fontweight="bold",
    )


def rounded_box(
    ax,
    x: float,
    y: float,
    w: float,
    h: float,
    title: str,
    details: str,
    face: str,
    edge: str,
    *,
    linestyle: str = "-",
    title_size: float = 7.3,
    detail_size: float = 6.5,
) -> None:
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.012,rounding_size=0.018",
        linewidth=1.05,
        edgecolor=edge,
        facecolor=face,
        linestyle=linestyle,
        transform=ax.transAxes,
        clip_on=False,
    )
    ax.add_patch(patch)
    ax.text(
        x + w / 2,
        y + h * 0.66,
        title,
        ha="center",
        va="center",
        transform=ax.transAxes,
        fontsize=title_size,
        fontweight="bold",
        color=DARK,
    )
    ax.text(
        x + w / 2,
        y + h * 0.30,
        details,
        ha="center",
        va="center",
        transform=ax.transAxes,
        fontsize=detail_size,
        color=DARK,
        linespacing=1.1,
    )


def arrow(
    ax,
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    *,
    color: str = DARK,
    style: str = "-|>",
    linestyle: str = "-",
    linewidth: float = 1.05,
    connectionstyle: str = "arc3",
) -> None:
    ax.add_patch(
        FancyArrowPatch(
            (x1, y1),
            (x2, y2),
            transform=ax.transAxes,
            arrowstyle=style,
            mutation_scale=8,
            linewidth=linewidth,
            color=color,
            linestyle=linestyle,
            connectionstyle=connectionstyle,
            clip_on=False,
        )
    )


def clean_axis(ax, *, horizontal_grid: bool = True) -> None:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(MID)
    ax.spines["bottom"].set_color(MID)
    if horizontal_grid:
        ax.grid(axis="y", color=GRID, linewidth=0.55, zorder=0)
    ax.set_axisbelow(True)


def value_labels(ax, bars, fmt: str = "{:.1f}", suffix: str = "") -> None:
    ymax = ax.get_ylim()[1]
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + ymax * 0.025,
            fmt.format(height) + suffix,
            ha="center",
            va="bottom",
            fontsize=6.7,
            fontweight="bold",
        )


def save_figure(fig, stem: str) -> None:
    fig.savefig(SCRIPT_DIR / f"{stem}.svg", bbox_inches=None)
    fig.savefig(SCRIPT_DIR / f"{stem}.pdf", bbox_inches=None)
    fig.savefig(SCRIPT_DIR / f"{stem}.png", dpi=220, bbox_inches=None)
    plt.close(fig)


def figure_architecture() -> None:
    fig = plt.figure(figsize=(7.16, 5.35))

    # (a) End-to-end scientific architecture.
    ax = fig.add_axes([0.045, 0.655, 0.91, 0.285])
    ax.set_axis_off()
    panel_title(ax, "a", "Evaluated end-to-end processing architecture")

    x_positions = [0.005, 0.175, 0.345, 0.515, 0.685, 0.855]
    widths = [0.13, 0.13, 0.13, 0.13, 0.13, 0.13]
    y, h = 0.29, 0.54
    boxes = [
        ("Accessibility\ninput", "UIA events\n+ keyboard", PALE_BLUE, BLUE),
        ("Classification", "type, priority\ncriticality", PALE_PURPLE, PURPLE),
        ("Temporal\ncoalescing", r"$\delta=50$ ms" + "\n3 priority queues", PALE_ORANGE, ORANGE),
        ("Indexed\nnavigation", "cached buffer\n" + r"$O(\log n)$ lookup", PALE_GREEN, GREEN),
        ("Bilingual\nrouting", "NFKC, script\n5k lexicon", PALE_BLUE, BLUE),
        ("Prioritized\nspeech", "Bengali / English\nTTS + preemption", PALE_RED, VERMILLION),
    ]
    for x, w, (title, detail, face, edge) in zip(x_positions, widths, boxes):
        rounded_box(ax, x, y, w, h, title, detail, face, edge)
    for left, right in zip(x_positions[:-1], x_positions[1:]):
        arrow(ax, left + 0.13, y + h / 2, right - 0.008, y + h / 2)

    ax.text(
        0.005,
        0.08,
        "Observed event types: focus • structure • property",
        transform=ax.transAxes,
        fontsize=6.5,
        color=MID,
    )
    rounded_box(
        ax,
        0.505,
        0.01,
        0.31,
        0.15,
        "Application adaptation boundary",
        "Word • Excel • Zoom • WhatsApp • Web",
        WHITE,
        MID,
        linestyle="--",
        title_size=6.5,
        detail_size=6.1,
    )
    arrow(
        ax,
        0.66,
        0.16,
        0.58,
        y - 0.005,
        color=MID,
        linestyle="--",
        linewidth=0.9,
    )

    # (b) Event raster and coalesced output.
    ax = fig.add_axes([0.095, 0.365, 0.86, 0.205])
    panel_title(ax, "b", "Illustrative priority-stratified suppression within 50-ms windows")
    ax.set_xlim(0, 200)
    ax.set_ylim(-0.55, 3.55)
    ax.set_yticks([3, 2, 1, 0])
    ax.set_yticklabels(["Focus", "Structure", "Property", "Emitted"])
    ax.set_xlabel("Arrival time (ms)")
    ax.set_xticks([0, 50, 100, 150, 200])
    for boundary in [0, 50, 100, 150, 200]:
        ax.axvline(boundary, color=GRID, linestyle="--", linewidth=0.75, zorder=0)

    event_sets = {
        3: ([8, 18, 34, 63, 79, 96, 124, 164, 176], PURPLE),
        2: ([11, 22, 41, 68, 72, 119, 137, 146, 183], GREEN),
        1: ([5, 15, 25, 32, 39, 55, 59, 84, 89, 107, 114, 132, 142, 158, 169, 190], BLUE),
    }
    for lane, (times, color) in event_sets.items():
        ax.scatter(
            times,
            [lane] * len(times),
            marker="o",
            s=20,
            facecolor=WHITE,
            edgecolor=color,
            linewidth=1.1,
            zorder=3,
        )

    emitted = [34, 41, 39, 96, 72, 89, 124, 146, 142, 176, 183, 190]
    emitted_colors = [
        PURPLE,
        GREEN,
        BLUE,
        PURPLE,
        GREEN,
        BLUE,
        VERMILLION,
        GREEN,
        BLUE,
        PURPLE,
        GREEN,
        BLUE,
    ]
    ax.scatter(
        emitted,
        [0] * len(emitted),
        marker="s",
        s=23,
        c=emitted_colors,
        edgecolor=DARK,
        linewidth=0.4,
        zorder=4,
    )
    ax.scatter([124], [3], marker="*", s=78, c=VERMILLION, edgecolor=DARK, linewidth=0.4, zorder=5)
    ax.annotate(
        "critical bypass",
        xy=(124, 3),
        xytext=(135, 3.32),
        fontsize=6.3,
        color=VERMILLION,
        arrowprops=dict(arrowstyle="->", color=VERMILLION, lw=0.7),
    )
    ax.text(
        199,
        -0.42,
        "○ received    ■ retained    ★ immediate",
        ha="right",
        va="bottom",
        fontsize=6.2,
        color=MID,
    )
    clean_axis(ax, horizontal_grid=True)

    # (c) Three ablation summaries.
    fig.text(0.045, 0.282, "(c)", fontsize=9, fontweight="bold")
    fig.text(0.087, 0.282, "Measured contribution of suppression and indexed navigation", fontsize=8.5, fontweight="bold")

    ax1 = fig.add_axes([0.075, 0.055, 0.245, 0.165])
    vals = [3.7, 1.0]
    bars = ax1.bar([0, 1], vals, color=[SKY, ORANGE], edgecolor=DARK, linewidth=0.55, width=0.62, zorder=2)
    ax1.set_title("Raw-to-emitted events", pad=4)
    ax1.set_xticks([0, 1], ["Raw", "Emitted"])
    ax1.set_ylabel("Relative event count")
    ax1.set_ylim(0, 4.4)
    value_labels(ax1, bars, suffix="×")
    clean_axis(ax1)

    ax2 = fig.add_axes([0.395, 0.055, 0.245, 0.165])
    vals = [7.1, 9.4]
    bars = ax2.bar(
        [0, 1],
        vals,
        yerr=[0, 0.6],
        capsize=2.2,
        color=[BLUE, ORANGE],
        edgecolor=DARK,
        linewidth=0.55,
        width=0.62,
        zorder=2,
    )
    ax2.set_title("Zoom-workload CPU", pad=4)
    ax2.set_xticks([0, 1], ["Full ALO", "No\ncoalescer"])
    ax2.set_ylabel("Mean CPU (%)")
    ax2.set_ylim(0, 12.5)
    value_labels(ax2, bars, suffix="%")
    ax2.text(1, 11.45, "±0.6 pp (95% CI)", ha="center", va="bottom", fontsize=5.8, color=MID)
    clean_axis(ax2)

    ax3 = fig.add_axes([0.715, 0.055, 0.245, 0.165])
    vals = [38.4, 217.6]
    bars = ax3.bar(
        [0, 1],
        vals,
        yerr=[7.1, 34.8],
        capsize=2.2,
        color=[GREEN, VERMILLION],
        edgecolor=DARK,
        linewidth=0.55,
        width=0.62,
        zorder=2,
    )
    ax3.set_title("400-heading navigation", pad=4)
    ax3.set_xticks([0, 1], ["Indexed\nbuffer", "No buffer"])
    ax3.set_ylabel("Heading jump (ms)")
    ax3.set_ylim(0, 285)
    value_labels(ax3, bars, suffix="")
    ax3.text(0.5, 269, "error bars: SD", ha="center", va="top", fontsize=5.8, color=MID)
    clean_axis(ax3)

    save_figure(fig, "alo_scientific_architecture")


def figure_bilingual_routing() -> None:
    fig = plt.figure(figsize=(7.16, 5.25))

    # (a) Algorithmic routing path.
    ax = fig.add_axes([0.045, 0.67, 0.91, 0.27])
    ax.set_axis_off()
    panel_title(ax, "a", "Deterministic Bengali–English routing path")

    ax.text(
        0.5,
        0.91,
        'Example input:  "আমি payment successful — ami khushi"',
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=7.5,
        fontweight="bold",
    )
    rounded_box(ax, 0.01, 0.31, 0.135, 0.42, "Normalize", "Unicode NFKC\nclean controls", PALE_BLUE, BLUE)
    rounded_box(ax, 0.19, 0.31, 0.135, 0.42, "Tokenize", "sliding window\nby script", PALE_PURPLE, PURPLE)
    rounded_box(ax, 0.38, 0.47, 0.15, 0.31, "Bengali script", "U+0980–U+09FF", PALE_GREEN, GREEN)
    rounded_box(ax, 0.38, 0.08, 0.15, 0.31, "Latin script", "lexicon lookup", PALE_ORANGE, ORANGE)
    rounded_box(ax, 0.59, 0.47, 0.15, 0.31, "Bengali unit", "native token or\ncanonical form", PALE_GREEN, GREEN)
    rounded_box(ax, 0.59, 0.08, 0.15, 0.31, "English unit", "unmatched / OOV /\nambiguous collision", PALE_BLUE, BLUE)
    rounded_box(ax, 0.80, 0.31, 0.18, 0.42, "Ordered synthesis", "Bengali + English TTS\nboundary pauses", PALE_RED, VERMILLION)

    arrow(ax, 0.145, 0.52, 0.19, 0.52)
    arrow(ax, 0.325, 0.52, 0.38, 0.63)
    arrow(ax, 0.325, 0.52, 0.38, 0.235)
    arrow(ax, 0.53, 0.63, 0.59, 0.63)
    arrow(ax, 0.53, 0.235, 0.59, 0.63, color=GREEN, connectionstyle="arc3,rad=-0.30")
    arrow(ax, 0.53, 0.235, 0.59, 0.235, color=BLUE)
    arrow(ax, 0.74, 0.63, 0.80, 0.57, color=GREEN)
    arrow(ax, 0.74, 0.235, 0.80, 0.45, color=BLUE)
    ax.text(0.555, 0.44, "match", transform=ax.transAxes, fontsize=5.8, color=GREEN, ha="center")
    ax.text(0.555, 0.17, "no safe match", transform=ax.transAxes, fontsize=5.8, color=BLUE, ha="center")

    # (b) Worked token decisions.
    ax = fig.add_axes([0.055, 0.375, 0.89, 0.235])
    ax.set_axis_off()
    panel_title(ax, "b", "Representative routing decisions")
    columns = ["Observed token", "Evidence", "Decision", "Synthesized form"]
    rows = [
        ["আমি", "Bengali code points", "Bengali TTS", "আমি"],
        ["payment", "Latin; no lexicon match", "English TTS", "payment"],
        ["ami", "5,000-entry lexicon match", "Bengali TTS", "আমি"],
        ["to", "English collision; excluded", "English TTS", "to"],
        ["unseen form", "Out of vocabulary", "Conservative English fallback", "unchanged"],
    ]
    table = ax.table(
        cellText=rows,
        colLabels=columns,
        loc="center",
        cellLoc="left",
        colLoc="left",
        colWidths=[0.17, 0.30, 0.27, 0.22],
        bbox=[0.0, 0.0, 1.0, 0.88],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(6.7)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor(GRID)
        cell.set_linewidth(0.55)
        if row == 0:
            cell.set_facecolor(DARK)
            cell.get_text().set_color(WHITE)
            cell.get_text().set_fontweight("bold")
        else:
            cell.set_facecolor(WHITE if row % 2 else "#F6F8F9")
            if col == 2:
                text = rows[row - 1][2]
                cell.get_text().set_color(GREEN if "Bengali" in text else BLUE)
                cell.get_text().set_fontweight("bold")

    # (c) Measured latency and scope.
    ax = fig.add_axes([0.18, 0.09, 0.76, 0.22])
    panel_title(ax, "c", "Measured language-processing latency")
    labels = [
        "Boundary identification",
        "ALO end-to-end switch",
        "NVDA engine switch only",
        "Complete mixed sentence",
    ]
    means = np.array([23.7, 105.0, 134.6, 258.3])
    errors = np.array([8.3, 18.7, 0.0, 42.4])
    colors = [SKY, GREEN, ORANGE, PURPLE]
    y = np.arange(len(labels))
    bars = ax.barh(
        y,
        means,
        xerr=errors,
        capsize=2.2,
        color=colors,
        edgecolor=DARK,
        linewidth=0.55,
        height=0.58,
        zorder=2,
    )
    bars[2].set_hatch("///")
    bars[2].set_facecolor(WHITE)
    bars[2].set_edgecolor(ORANGE)
    ax.set_yticks(y, labels)
    ax.invert_yaxis()
    ax.set_xlim(0, 325)
    ax.set_xlabel("Latency (ms); error bars show SD where reported")
    ax.grid(axis="x", color=GRID, linewidth=0.55, zorder=0)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for i, (mean, err) in enumerate(zip(means, errors)):
        label = f"{mean:.1f}" + (f" ± {err:.1f}" if err else "")
        ax.text(mean + err + 5, i, label, va="center", ha="left", fontsize=6.6, fontweight="bold")
    ax.text(
        0.995,
        0.92,
        "Striped NVDA bar: engine-switch scope only;\nnot an end-to-end equivalent.",
        transform=ax.transAxes,
        ha="right",
        va="top",
        fontsize=5.8,
        color=MID,
    )

    save_figure(fig, "alo_bilingual_routing")


def add_significance(ax, x1: float, x2: float, y: float, text: str, height: float = 6) -> None:
    ax.plot([x1, x1, x2, x2], [y, y + height, y + height, y], color=DARK, linewidth=0.65, clip_on=False)
    ax.text((x1 + x2) / 2, y + height + 1.5, text, ha="center", va="bottom", fontsize=6.2, fontweight="bold")


def figure_task_results() -> None:
    fig = plt.figure(figsize=(7.16, 5.45))

    systems = ["ALO", "NVDA", "JAWS"]
    colors = [BLUE, ORANGE, GREEN]
    hatches = ["", "///", "..."]
    tasks = ["English\nnavigation", "Mixed-language\ninput", "Bengali web\nbrowsing"]

    # (a) Completion time.
    ax = fig.add_axes([0.085, 0.57, 0.54, 0.34])
    panel_title(ax, "a", "Task-completion time")
    means = np.array(
        [
            [47.3, 51.6, 49.8],
            [92.6, 168.4, 174.1],
            [118.7, 224.6, 231.8],
        ]
    )
    sds = np.array(
        [
            [8.4, 9.1, 8.7],
            [14.2, 27.3, 29.1],
            [0.0, 0.0, 0.0],
        ]
    )
    x = np.arange(len(tasks))
    width = 0.23
    for idx, (system, color, hatch) in enumerate(zip(systems, colors, hatches)):
        xpos = x + (idx - 1) * width
        bars = ax.bar(
            xpos,
            means[:, idx],
            width,
            yerr=sds[:, idx],
            capsize=2.0,
            label=system,
            color=color,
            edgecolor=DARK,
            linewidth=0.5,
            hatch=hatch,
            zorder=2,
        )
        for bar, value in zip(bars, means[:, idx]):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                value + 5,
                f"{value:.1f}",
                ha="center",
                va="bottom",
                fontsize=5.5,
                rotation=90,
            )
    ax.set_xticks(x, tasks)
    ax.set_ylabel("Mean completion time (s)")
    ax.set_ylim(0, 290)
    ax.legend(ncol=3, loc="upper left", frameon=False)
    add_significance(ax, x[0] - width, x[0] + width, 82, "NS", height=4)
    add_significance(ax, x[1] - width, x[1] + width, 217, "p < 0.01", height=5)
    add_significance(ax, x[2] - width, x[2] + width, 265, "p < 0.01", height=5)
    ax.text(
        0.0,
        -0.28,
        "Error bars: SD where reported in the manuscript.",
        transform=ax.transAxes,
        fontsize=5.8,
        color=MID,
    )
    clean_axis(ax)

    # (b) Mean error count.
    ax = fig.add_axes([0.70, 0.57, 0.27, 0.34])
    panel_title(ax, "b", "Task errors")
    errors = np.array(
        [
            [1.2, 1.5, 1.3],
            [2.1, 6.8, 7.2],
            [2.8, 8.4, 8.9],
        ]
    )
    x = np.arange(len(tasks))
    width = 0.23
    for idx, (system, color, hatch) in enumerate(zip(systems, colors, hatches)):
        xpos = x + (idx - 1) * width
        bars = ax.bar(
            xpos,
            errors[:, idx],
            width,
            color=color,
            edgecolor=DARK,
            linewidth=0.5,
            hatch=hatch,
            zorder=2,
        )
        for bar, value in zip(bars, errors[:, idx]):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                value + 0.18,
                f"{value:.1f}",
                ha="center",
                va="bottom",
                fontsize=5.4,
                rotation=90,
            )
    ax.set_xticks(x, ["English", "Mixed", "Bengali\nweb"])
    ax.set_ylabel("Mean error count")
    ax.set_ylim(0, 10.5)
    ax.text(
        0.5,
        -0.23,
        "Mixed + Bengali:\np < 0.01",
        transform=ax.transAxes,
        ha="center",
        va="top",
        fontsize=5.8,
        fontweight="bold",
    )
    clean_axis(ax)

    # (c) Preference proportions with exact binomial CIs.
    ax = fig.add_axes([0.22, 0.17, 0.72, 0.24])
    panel_title(ax, "c", "Participant preference for ALO")
    pref_labels = [
        "Bengali / mixed content",
        "General navigation + Bengali web",
        "English-only content",
    ]
    values = np.array([100.0, 86.7, 53.3])
    ci_low = np.array([78.2, 59.5, 26.6])
    ci_high = np.array([100.0, 98.3, 78.7])
    y = np.arange(3)
    xerr = np.vstack((values - ci_low, ci_high - values))
    ax.errorbar(
        values,
        y,
        xerr=xerr,
        fmt="o",
        markersize=6,
        color=BLUE,
        ecolor=DARK,
        elinewidth=1.2,
        capsize=3,
        markeredgecolor=DARK,
        markeredgewidth=0.6,
        zorder=3,
    )
    ax.axvline(50, color=MID, linestyle="--", linewidth=0.8, zorder=1)
    ax.set_yticks(y, pref_labels)
    ax.invert_yaxis()
    ax.set_xlim(0, 120)
    ax.set_xticks([0, 20, 40, 50, 60, 80, 100])
    ax.set_xlabel("Participants selecting ALO (%) with exact binomial 95% CI")
    ax.grid(axis="x", color=GRID, linewidth=0.55, zorder=0)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    counts = ["15/15", "13/15", "8/15"]
    for i, (value, low, high, count) in enumerate(zip(values, ci_low, ci_high, counts)):
        ax.text(
            116.5,
            i,
            f"{count} • {value:.1f}%\nCI {low:.1f}–{high:.1f}",
            ha="right",
            va="center",
            fontsize=5.9,
            fontweight="bold",
            linespacing=1.05,
        )

    fig.text(
        0.965,
        0.018,
        "Within-subject study; two-sided Wilcoxon tests with Bonferroni correction.",
        ha="right",
        va="bottom",
        fontsize=5.8,
        color=MID,
    )
    fig.text(
        0.22,
        0.055,
        "n = 15; preference proportions are descriptive and intervals remain wide at this sample size.",
        ha="left",
        va="bottom",
        fontsize=5.8,
        color=MID,
    )
    save_figure(fig, "alo_task_study_results")


def figure_plugin_adaptation() -> None:
    """Consolidate architecture, component, and lifecycle UML into one figure."""
    fig = plt.figure(figsize=(7.16, 4.35))

    ax = fig.add_axes([0.045, 0.61, 0.91, 0.32])
    ax.set_axis_off()
    panel_title(ax, "a", "Stable core with foreground-context adaptation")
    stages = [
        (0.01, "Foreground\ncontext", "process + window\nidentity", PALE_BLUE, BLUE),
        (0.205, "Adapter\nselection", "match active\napplication", PALE_PURPLE, PURPLE),
        (0.40, "Isolated reader\nmodule", "application-specific\nsemantics", PALE_ORANGE, ORANGE),
        (0.595, "Shared service\ncontract", "navigation • events\nsettings • speech", PALE_GREEN, GREEN),
        (0.79, "Stable ALO\ncore", "coalescing • buffer\nbilingual output", PALE_RED, VERMILLION),
    ]
    for x, title, detail, face, edge in stages:
        rounded_box(ax, x, 0.34, 0.16, 0.46, title, detail, face, edge)
    for left, right in zip(stages[:-1], stages[1:]):
        arrow(ax, left[0] + 0.16, 0.57, right[0] - 0.008, 0.57)
    ax.text(
        0.48,
        0.16,
        "Only the selected reader subscribes to the active application context",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=6.6,
        color=MID,
        fontweight="bold",
    )
    for i, (name, color) in enumerate(
        [("Word", BLUE), ("Excel", GREEN), ("Zoom", ORANGE), ("WhatsApp", PURPLE), ("Web", VERMILLION)]
    ):
        x = 0.28 + i * 0.105
        rounded_box(ax, x, -0.04, 0.085, 0.14, name, "", WHITE, color, title_size=6.1, detail_size=1)
        arrow(ax, x + 0.042, 0.10, 0.48, 0.33, color=color, linestyle="--", linewidth=0.65)

    ax = fig.add_axes([0.055, 0.12, 0.56, 0.37])
    ax.set_axis_off()
    panel_title(ax, "b", "Context-scoped lifecycle and cleanup invariant")
    life = [
        (0.01, "Discover", "assembly", PALE_BLUE, BLUE),
        (0.205, "Register", "factory", PALE_PURPLE, PURPLE),
        (0.40, "Initialize", "on match", PALE_ORANGE, ORANGE),
        (0.595, "Active", "process events", PALE_GREEN, GREEN),
        (0.79, "Detach", "dispose", PALE_RED, VERMILLION),
    ]
    for x, title, detail, face, edge in life:
        rounded_box(ax, x, 0.40, 0.15, 0.31, title, detail, face, edge, title_size=6.6, detail_size=5.8)
    for left, right in zip(life[:-1], life[1:]):
        arrow(ax, left[0] + 0.15, 0.555, right[0] - 0.008, 0.555, linewidth=0.9)
    ax.text(
        0.50,
        0.18,
        "Invariant: subscriptions and owned resources end when focus leaves the application",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=6.3,
        color=DARK,
        bbox=dict(boxstyle="round,pad=0.25", facecolor="#F6F8F9", edgecolor=GRID),
    )
    arrow(ax, 0.865, 0.38, 0.09, 0.36, color=MID, linestyle="--", connectionstyle="arc3,rad=-0.24")
    ax.text(0.49, 0.01, "next foreground context", transform=ax.transAxes, ha="center", fontsize=5.8, color=MID)

    ax = fig.add_axes([0.665, 0.12, 0.29, 0.37])
    ax.set_axis_off()
    panel_title(ax, "c", "Adaptation strategy by workload")
    rows = [
        ["Word / Excel", "structured navigation"],
        ["Zoom", "priority state + chat"],
        ["WhatsApp", "conversation context"],
        ["Web", "buffer + landmarks"],
    ]
    table = ax.table(
        cellText=rows,
        colLabels=["Context", "Specialized behavior"],
        cellLoc="left",
        colLoc="left",
        colWidths=[0.39, 0.61],
        bbox=[0, 0.13, 1, 0.68],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(5.9)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor(GRID)
        cell.set_linewidth(0.55)
        if row == 0:
            cell.set_facecolor(DARK)
            cell.get_text().set_color(WHITE)
            cell.get_text().set_fontweight("bold")
        else:
            cell.set_facecolor(WHITE if row % 2 else "#F6F8F9")
    ax.text(
        0.5,
        0.02,
        "Shared processing semantics remain unchanged.",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=5.8,
        color=MID,
    )
    save_figure(fig, "alo_plugin_adaptation")


def figure_interaction_priority() -> None:
    """Consolidate startup, focus, and hotkey sequences into a causal model."""
    fig = plt.figure(figsize=(7.16, 4.55))

    ax = fig.add_axes([0.045, 0.61, 0.91, 0.32])
    ax.set_axis_off()
    panel_title(ax, "a", "Triggers, priority policy, and observable effects")
    left = [
        (0.01, 0.67, "System ready", "services + index", BLUE),
        (0.01, 0.42, "Focus change", "new UI element", PURPLE),
        (0.01, 0.17, "User command", "semantic navigation", GREEN),
    ]
    for x, y, title, detail, color in left:
        rounded_box(ax, x, y, 0.19, 0.17, title, detail, WHITE, color, title_size=6.5, detail_size=5.7)
    rounded_box(
        ax,
        0.31,
        0.26,
        0.25,
        0.47,
        "Priority and state policy",
        "critical → immediate\nuser/focus → preemptive\nproperty → coalesced",
        PALE_ORANGE,
        ORANGE,
        title_size=7.0,
        detail_size=6.1,
    )
    right = [
        (0.68, 0.67, "Update context", "element + position", PURPLE),
        (0.68, 0.42, "Navigate / act", "buffer or adapter", GREEN),
        (0.68, 0.17, "Speak current state", "cancel stale output", VERMILLION),
    ]
    for x, y, title, detail, color in right:
        rounded_box(ax, x, y, 0.22, 0.17, title, detail, WHITE, color, title_size=6.5, detail_size=5.7)
    for _, y, *_ in left:
        arrow(ax, 0.20, y + 0.085, 0.31, 0.495, color=MID)
    for _, y, *_ in right:
        arrow(ax, 0.56, 0.495, 0.68, y + 0.085, color=MID)
    rounded_box(
        ax,
        0.915,
        0.35,
        0.075,
        0.30,
        "User",
        "current\naudio",
        PALE_BLUE,
        BLUE,
        title_size=6.2,
        detail_size=5.6,
    )
    arrow(ax, 0.90, 0.255, 0.915, 0.45, color=VERMILLION)

    ax = fig.add_axes([0.095, 0.12, 0.51, 0.36])
    panel_title(ax, "b", "Illustrative speech preemption under a higher-priority command")
    ax.set_xlim(0, 180)
    ax.set_ylim(-0.45, 2.6)
    ax.set_yticks([2, 1, 0])
    ax.set_yticklabels(["Speech state", "Trigger", "Output"])
    ax.set_xlabel("Relative time (ms)")
    ax.hlines(2, 0, 55, color=SKY, linewidth=8, label="low-priority utterance")
    ax.hlines(2, 62, 118, color=VERMILLION, linewidth=8, label="high-priority announcement")
    ax.hlines(2, 125, 175, color=SKY, linewidth=8, linestyle="--", label="resume/defer")
    ax.scatter([55], [1], marker="D", s=36, c=GREEN, edgecolor=DARK, zorder=4)
    ax.vlines(55, 1.1, 2.35, color=GREEN, linestyle="--", linewidth=0.9)
    ax.text(55, 0.74, "user command", ha="center", va="top", fontsize=6.0, color=GREEN)
    ax.scatter([62], [0], marker="s", s=27, c=VERMILLION, edgecolor=DARK, zorder=4)
    ax.text(62, -0.20, "current state", ha="center", va="top", fontsize=6.0, color=VERMILLION)
    ax.annotate(
        "cancellation token",
        xy=(56, 2.0),
        xytext=(82, 2.42),
        fontsize=5.9,
        color=DARK,
        arrowprops=dict(arrowstyle="->", color=DARK, lw=0.7),
    )
    ax.text(
        176,
        0.38,
        "Without cancellation:\n+40–60 ms at p95",
        ha="right",
        va="center",
        fontsize=6.0,
        color=VERMILLION,
        fontweight="bold",
    )
    ax.grid(axis="x", color=GRID, linewidth=0.55)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax = fig.add_axes([0.66, 0.12, 0.295, 0.36])
    ax.set_axis_off()
    panel_title(ax, "c", "Policy applied to each trigger")
    rows = [
        ["Focus", "context", "preempt"],
        ["Hotkey", "navigation", "cancel + speak"],
        ["Critical", "control state", "immediate"],
        ["Property", "cached state", "coalesce"],
    ]
    table = ax.table(
        cellText=rows,
        colLabels=["Trigger", "State effect", "Speech action"],
        cellLoc="left",
        colLoc="left",
        colWidths=[0.24, 0.37, 0.39],
        bbox=[0, 0.08, 1, 0.76],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(5.7)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor(GRID)
        cell.set_linewidth(0.55)
        if row == 0:
            cell.set_facecolor(DARK)
            cell.get_text().set_color(WHITE)
            cell.get_text().set_fontweight("bold")
        else:
            cell.set_facecolor(WHITE if row % 2 else "#F6F8F9")
    save_figure(fig, "alo_interaction_priority")


def figure_uia_resource_safety() -> None:
    """Consolidate UIA navigation and COM lifecycle into one mechanism figure."""
    fig = plt.figure(figsize=(7.16, 4.55))

    ax = fig.add_axes([0.045, 0.60, 0.91, 0.33])
    ax.set_axis_off()
    panel_title(ax, "a", "Cached UIA traversal and indexed navigation")
    stages = [
        (0.01, "UIA subtree", "foreground\napplication", PALE_BLUE, BLUE),
        (0.19, "Batch retrieval", "CacheRequest\nsingle traversal", PALE_PURPLE, PURPLE),
        (0.37, "Flattened buffer", "crawl cap\n" + r"$m=250$", PALE_ORANGE, ORANGE),
        (0.55, "Typed indices", "heading • link\nform • table", PALE_GREEN, GREEN),
        (0.73, "Navigation query", r"$O(\log n)$" + "\nlocal lookup", PALE_BLUE, BLUE),
        (0.91, "Context\n+ speech", "current\nelement", PALE_RED, VERMILLION),
    ]
    widths = [0.13, 0.13, 0.13, 0.13, 0.13, 0.08]
    for (x, title, detail, face, edge), w in zip(stages, widths):
        rounded_box(ax, x, 0.37, w, 0.43, title, detail, face, edge, title_size=6.5, detail_size=5.8)
    for i in range(len(stages) - 1):
        arrow(ax, stages[i][0] + widths[i], 0.585, stages[i + 1][0] - 0.008, 0.585, linewidth=0.9)
    rounded_box(
        ax,
        0.30,
        0.02,
        0.34,
        0.18,
        "StructureChanged event",
        "invalidate affected subtree → patch buffer and indices",
        WHITE,
        MID,
        linestyle="--",
        title_size=6.2,
        detail_size=5.6,
    )
    arrow(ax, 0.47, 0.20, 0.435, 0.36, color=MID, linestyle="--", linewidth=0.8)
    arrow(ax, 0.64, 0.11, 0.61, 0.36, color=MID, linestyle="--", linewidth=0.8)

    ax = fig.add_axes([0.055, 0.11, 0.55, 0.37])
    ax.set_axis_off()
    panel_title(ax, "b", "Explicit ownership and release of COM-backed resources")
    rounded_box(ax, 0.01, 0.52, 0.20, 0.25, "Primary objects", "plugin / context lifetime", PALE_PURPLE, PURPLE)
    rounded_box(ax, 0.01, 0.16, 0.20, 0.25, "Secondary objects", "short-lived operation", PALE_BLUE, BLUE)
    rounded_box(ax, 0.34, 0.34, 0.24, 0.30, "Two-tier tracker", "register ownership\nobserve lifetime", PALE_ORANGE, ORANGE)
    rounded_box(ax, 0.72, 0.52, 0.25, 0.25, "Deterministic release", "plugin unload or\ncontext switch", PALE_RED, VERMILLION)
    rounded_box(ax, 0.72, 0.16, 0.25, 0.25, "Periodic sweep", "low-activity window\nor timeout", PALE_GREEN, GREEN)
    arrow(ax, 0.21, 0.645, 0.34, 0.52, color=PURPLE)
    arrow(ax, 0.21, 0.285, 0.34, 0.45, color=BLUE)
    arrow(ax, 0.58, 0.52, 0.72, 0.645, color=VERMILLION)
    arrow(ax, 0.58, 0.45, 0.72, 0.285, color=GREEN)
    ax.text(
        0.50,
        0.02,
        "Goal: mitigate retained references; not a platform-independent memory model",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=5.8,
        color=MID,
    )

    ax = fig.add_axes([0.66, 0.11, 0.295, 0.37])
    ax.set_axis_off()
    panel_title(ax, "c", "Eight-hour stability observations")
    metrics = [
        ("324 ± 18.4 MB", "stabilized memory"),
        ("< 1.2% / h", "observed memory growth"),
        ("> 99%", "COM objects recycled"),
        ("100%", "listener cleanup"),
    ]
    for i, (value, label) in enumerate(metrics):
        y = 0.68 - i * 0.20
        face, edge = [(PALE_BLUE, BLUE), (PALE_GREEN, GREEN), (PALE_ORANGE, ORANGE), (PALE_PURPLE, PURPLE)][i]
        rounded_box(ax, 0.04, y, 0.92, 0.14, value, label, face, edge, title_size=7.0, detail_size=5.8)
    ax.text(
        0.50,
        0.00,
        "Observed behavior; no claim of absolute leak elimination.",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=5.7,
        color=MID,
    )
    save_figure(fig, "alo_uia_resource_safety")


def main() -> None:
    figure_architecture()
    figure_bilingual_routing()
    figure_task_results()
    figure_plugin_adaptation()
    figure_interaction_priority()
    figure_uia_resource_safety()
    print("Generated SVG, PDF, and PNG assets for all six scientific figures.")


if __name__ == "__main__":
    main()
