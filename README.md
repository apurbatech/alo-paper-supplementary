# ALO Screen Reader — Supplementary Materials

**Paper:** ALO: A Screen Reader Architecture for Bengali–English Code-Switching with Temporal Event Coalescing  
**Journal:** IEEE Access  
**Manuscript ID:** Access-2026-19242  

This repository is the **single public package** of supplementary materials for the ALO Windows screen reader paper.

**Repository:** https://github.com/apurbatech/alo-paper-supplementary  

---

## Scope

| Item | Status |
|------|--------|
| **Platform evaluated** | **Windows only** (Windows 10/11, UI Automation + COM) |
| **Android / Linux** | Not part of the experimental evaluation in this paper |
| **Evaluation data** | Aggregate summary only (`Testing Report.pdf`) |
| **Per-participant raw logs** | **Not included** |
| **Full multi-configuration benchmark dumps** | **Not included** |

ALO was **developed by Apurba Technologies Ltd.** Human evaluation was authorized by **EBLICT, Bangladesh Computer Council (BCC)**, with external testing support involving a **Dhaka University** testing team (full ethics detail is in the main manuscript).

---

## Repository layout (current)

```text
alo-paper-supplementary/
├── README.md
├── SCREEN READER ALO WINDOWS INSTALLATION GUIDE.pdf
├── ALO User Manual.pdf
├── Alo_Screen_Reader_Full_Guide.docx.pdf
├── Testing Report.pdf
├── ALO_ Supplementary Materials.pdf
└── diagrams/
    └── (main paper figures + supplementary UML / implementation diagrams)
```

**Windows installer (EXE)** is published under **GitHub Releases** (not as a large binary in the main tree):

- **Release tag:** `ieee-access-resubmission`  
- **Direct download:**  
  https://github.com/apurbatech/alo-paper-supplementary/releases/download/ieee-access-resubmission/AloScreenReaderApplicationSetupFile.exe  
- **Releases page:**  
  https://github.com/apurbatech/alo-paper-supplementary/releases  

---

## Files in this repository

| File / folder | Description |
|---------------|-------------|
| **Windows installer (EXE)** | `AloScreenReaderApplicationSetupFile.exe` — provided via [GitHub Release `ieee-access-resubmission`](https://github.com/apurbatech/alo-paper-supplementary/releases/download/ieee-access-resubmission/AloScreenReaderApplicationSetupFile.exe) |
| **`SCREEN READER ALO WINDOWS INSTALLATION GUIDE.pdf`** | Step-by-step Windows installation and setup |
| **`ALO User Manual.pdf`** | End-user manual: navigation, speech, and hotkeys |
| **`Alo_Screen_Reader_Full_Guide.docx.pdf`** | Full guide (extended usage / reference) |
| **`Testing Report.pdf`** | Aggregate system benchmarks and user-study summary (no raw participant logs) |
| **`ALO_ Supplementary Materials.pdf`** | Narrative supplementary document aligned with the manuscript (overview, Windows milestones, evaluation notes, figure captions) |
| **`diagrams/`** | Figures used in the paper and detailed implementation diagrams for the supplement |

### Diagrams folder

**Main paper scientific figures (typical names):**

- `alo_scientific_architecture` — architecture and coalescing  
- `alo_plugin_adaptation` — plugin adaptation  
- `alo_interaction_priority` — interaction priority / preemption  
- `alo_uia_resource_safety` — cached navigation and COM ownership  
- `alo_bilingual_routing` — Bengali–English routing  
- `alo_task_study_results` — task study results (*n* = 15)  

**Supplementary implementation / UML views** (plugin lifecycle, startup, UIA focus-change, hotkeys, COM release, cache/navigation, TTS routing, etc.) as described in `ALO_ Supplementary Materials.pdf`.

---

## Windows development milestones (summary)

Only **Windows** deliverables are associated with this paper’s evaluation:

| Milestone | Deliverables (summary) |
|-----------|-------------------------|
| Inception | SRS, design, methodology, workshop report, workplan |
| Milestone 1 | Windows v.1; App Set 1 (browsers, Office, PDF); external TTS |
| Milestone 2 | Windows v.2; App Set 1 v.2; native/external TTS–API integration |
| Milestone 3 | Windows v.2.1; App Set 2 (Gmail, Facebook, WhatsApp, Zoom, YouTube, …) |
| Milestone 4 | Windows v.3; full app support; TTS/STT finalized; paper; UAT; release docs |

Full milestone wording appears in `ALO_ Supplementary Materials.pdf`.

---

## Evaluation summary (aggregate only)

A controlled within-subject study with **15** visually impaired participants compared **ALO**, **NVDA**, and **JAWS** on document navigation, mixed-language text input, and Bengali web browsing.

**Configuration note:** ALO, NVDA, and JAWS were **not** configured with functionally equivalent Bengali–English pipelines. Results describe the **tested configurations**, not every product’s maximum customizable capability.

**Selected findings (full statistics in the main paper / Testing Report):**

- ALO language-routing path: mean **105.0 ms** (SD 18.7 ms). NVDA **134.6 ms** is **engine-switch only**. Different measurement scopes — **no direct percentage advantage** is claimed.  
- Under the evaluated setups, ALO handled unmarked Bengali content automatically; comparators often required manual intervention or unsuitable default synthesis.  
- Preference: **15/15** preferred ALO for Bengali and mixed content; **13/15 (86.7%)** preferred ALO for general navigation and Bengali web browsing (confidence intervals in the main paper).  

See **`Testing Report.pdf`** and the main manuscript for complete reporting.

---

## System requirements

| | Minimum | Recommended |
|--|---------|-------------|
| OS | Windows 10 (64-bit) | Windows 11 (64-bit) |
| RAM | 4 GB | 8 GB+ |
| Disk | ~1 GB | ~1 GB |
| Dependencies | .NET 4.8 runtime, Windows UI Automation, Bengali TTS engine | Same |

Follow **`SCREEN READER ALO WINDOWS INSTALLATION GUIDE.pdf`** for setup.

---

## How to use these materials

1. Download the Windows installer from the release:  
   [AloScreenReaderApplicationSetupFile.exe](https://github.com/apurbatech/alo-paper-supplementary/releases/download/ieee-access-resubmission/AloScreenReaderApplicationSetupFile.exe)  
2. Follow **`SCREEN READER ALO WINDOWS INSTALLATION GUIDE.pdf`** on a supported Windows machine.  
3. Use **`ALO User Manual.pdf`** (and the full guide if needed) for hotkeys and daily operation.  
4. Read **`Testing Report.pdf`** and **`ALO_ Supplementary Materials.pdf`** for evaluation context and diagram captions.  
5. Browse **`diagrams/`** for paper and implementation figures.  

---

## Citation / link

Please cite the main IEEE Access article when available, and link this repository as the supplementary package:

```text
https://github.com/apurbatech/alo-paper-supplementary
```

The installer for this resubmission is tied to release tag **`ieee-access-resubmission`**. Prefer citing that release (or a later tagged release) rather than only the default branch tip.

---

## Corresponding authors

- **Bijan Paul** — bijancse@gmail.com  
- **Md. Mahir Labib** — mdmahirlabib@gmail.com  

**Affiliation:** Apurba Technologies Ltd., Dhaka, Bangladesh (and co-authors as listed in the main paper).

---

## Privacy and licensing

- This repository does **not** include identifiable participant audio or per-person study logs.  
- Materials support academic review and reproducibility of the Windows ALO system described in the paper.  
- Application redistribution may be subject to separate terms; see any `LICENSE` / `NOTICE` file if present, and the installation package notes.

---

## Contact

For questions about this supplementary package, contact the corresponding authors above.
