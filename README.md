# Lab 1: FSD, but on Kigali roads…

African Leadership University  
Introduction to Python Programming and Databases  
BSE Year 1 — Trimester 2  
Individual Coding Lab

## Overview

This project simulates Full Self Driving (FSD) from **ALU Rwanda** to the **Kigali Convention Centre**.

The road is a Python list. Each item is one 100 m segment and can be:
- a speed limit (`"60"`, `"80"`, etc.)
- `"zebra"` — stop for pedestrians
- `"bus"` — move to the left lane
- `"road"` — plain road, nothing special

A ready-made web page shows the car driving through Kigali at night. Your Python logic decides what the car does.

## Files in this repository

```
lab1_githubUsername/
├── road_simulation.py   # student logic (TODO 1–10)
├── transit_program.py   # ready-made runner (do not edit)
├── engine.py            # ready-made web engine (do not edit)
├── index.html           # visual display (do not edit)
├── analyze_log.sh       # optional shell log analyser
├── README.md            # this file
└── transit_session.log  # created when you run the simulation
```

## How to run

1. Open a terminal in this folder.
2. Run:
   ```bash
   python3 road_simulation.py
   ```
3. Enter your driver name.
4. Use the road editor menu (add / insert / replace / show road).
5. Choose **5. Start driving**, then open the link shown (for example `http://127.0.0.1:8008`).
6. Go back to the terminal and press Enter. The car starts driving.

Events from each run are appended to `transit_session.log`.

## What I implemented

### Part 1 — Check the sign
| Function | What it does |
|---|---|
| `is_valid_sign` | Accepts only `"bus"`, `"zebra"`, or a number from 20 to 100 written as text |
| `get_sign_type` | Returns `"bus"`, `"zebra"`, `"speed"`, or `"road"` |

### Part 2 — Take action
| Function | What it does |
|---|---|
| `get_speed_limit` | Returns the new limit from a speed sign, or keeps the current one |
| `get_target_speed` | Returns `0` while stopped at a zebra, otherwise the limit |
| `adjust_speed` | Moves speed one step toward the target (+5 up, −20 down, no overshoot) |
| `count_signs` | Loops through the road and counts speed signs, zebras, and buses |

### Part 3 — Input and journey summary
| Function | What it does |
|---|---|
| `ask_for_number` | Keeps asking until the user types a whole number in range (`try` / `except`) |
| `insert_sign` | Inserts a sign at a position, with bounds checking |
| `replace_sign` | Replaces the sign at an index, with bounds checking |
| `get_journey_summary` | Counts signs passed, road length in metres, start and end names |

## Optional: Log analyser

After you have run the simulation at least once:

```bash
bash analyze_log.sh
```

Or pass a custom log file:

```bash
bash analyze_log.sh transit_session.log
```

The script:
- uses the file given as the first argument, or `transit_session.log` if none is given
- prints an error and exits with code 1 if the file does not exist
- counts sessions (runs), zebra stops, and lane changes
- shows the driver name and top speed from the latest trip

## Notes

- Do not edit `engine.py`, `transit_program.py`, or `index.html`.
- Only edit `road_simulation.py` (and the optional `analyze_log.sh`).
- Every sign is stored as text, even speed limits.
