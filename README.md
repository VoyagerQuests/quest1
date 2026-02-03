# 🧭 Quest 1 — Build the Character API  
## Episode 1: Entering the Realm of Clean Architecture

Welcome to **Quest 1, Episode 1**.  
In this quest, we focus on **building a working foundation**—getting the Character API up and running before refining structure and design in later parts.

Try to implement Quest 1 Episode 1.
Check out the Episode 1 walkthrough video on https://www.youtube.com/@VoyagerQuests
To run this code clone the repository and enter the quest1 folder.
### ⚙️ Create the Project Using `uv`

#### 1️⃣ Verify `uv` is installed

Run:

``` bash
uv --version
```

If you do **not** see a version number, install `uv` by following the
official instructions:\
👉 https://docs.astral.sh/uv/

------------------------------------------------------------------------

#### 2️⃣ Recreate the project environment

From the project root (where `pyproject.toml` and `uv.lock` exist), run:

``` bash
uv sync
```

This will create the virtual environment and install all dependencies
exactly as locked.

------------------------------------------------------------------------

#### 3️⃣ Start the FastAPI development server

``` bash
uv run fastapi dev
```

This runs the application using the synced environment---no manual
activation required.
Once the project is running you can access the docs at:
👉 http://127.0.0.1:8000/docs
👉 http://127.0.0.1:8000/redoc

------------------------------------------------------------------------

#### 4️⃣ Run the CLI

Examples (run from the project root):

``` bash
# Create a character
uv run python cli.py create --name "Aria Stormblade" --Might 70 --Agility 80 --Vitality 60 --Insight 75 --Arcana 40 --Presence 85

# List all characters
uv run python cli.py get

# Update attributes
uv run python cli.py update_attributes --character_id char_XXXXXXXXXXXX --Might 10 --Agility 20 --Vitality 30 --Insight 40 --Arcana 50 --Presence 60

# Get a single character by id
uv run python cli.py get --character_id char_XXXXXXXXXXXX
```

Notes:
- Attribute flags are case-insensitive.
- The CLI uses `characters.json` in the project root for storage.

---

### 📦 Quest Resources

- **GitHub Repository:** https://github.com/VoyagerQuests/quest1
- **Branch:** `part1`

---

## 🧩 Quest Overview

This episode's instructions are detailed in [READQUEST.md](READQUEST.md) in this repository.
