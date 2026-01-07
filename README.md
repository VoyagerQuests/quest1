# 🧭 Quest I — Build the Character API  
## Part 1: Getting Things Working

Welcome to **Quest 1, Part 1**.  
In this quest, we focus on **building a working foundation**—getting the Character API up and running before refining structure and design in later parts.

---

### 📦 Quest Resources

- **GitHub Repository:** https://github.com/VoyagerQuests/quest1
- **Branch:** `part1`

---

## 🧩 Quest Overview

### 🎯 Objective

Your mission is to create a backend system in **Python** that manages a set of **characters** and their **attributes**.

This system—the **Character API**—will serve as the **registry of your adventure world**, storing heroes, villains, and wanderers alike.

---

## ⚙️ Requirements

### 1️⃣ Create a REST API

Use **FastAPI** to build a backend with the following endpoints:

| Method | Endpoint | Description |
|------|---------|-------------|
| `GET` | `/characters` | List all characters with health and attributes |
| `GET` | `/characters/{id}` | Retrieve a single character by ID |
| `POST` | `/characters` | Add a new character |
| `PUT` | `/characters/{id}/attributes/{attribute_name}` | Update a specific attribute |
| `DELETE` | `/characters/{id}` | Delete a character *(optional)* |

---

### 2️⃣ Character Data Model

Each character must include:

| Field | Type | Description |
|------|------|-------------|
| `id` | `int` | Unique identifier |
| `name` | `string` | Character name |
| `health` | `int` (0–100) | Health level |
| `attributes` | `dict` | Attribute key–value pairs |

#### 🧬 Attributes

Each attribute has a **score (0–100)** and a descriptive purpose.

| Attribute | Description | Example Uses |
|---------|-------------|--------------|
| **Might** | Physical strength | Melee damage, intimidation |
| **Agility** | Speed and coordination | Dodging, stealth |
| **Vitality** | Endurance and resilience | Health, poison resistance |
| **Insight** | Perception and awareness | Detecting traps or lies |
| **Arcana** | Mystical or technical knowledge | Spellcasting, crafting |
| **Presence** | Influence and charisma | Persuasion, leadership |

---

### 3️⃣ Data Storage (File-Based)

Store all characters in a JSON file named:

```text
characters.json
