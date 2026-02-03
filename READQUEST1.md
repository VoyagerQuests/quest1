## Episode 1
### Branch: episode1

**Quest 1 episode 1: Build the Character API**

**Objective:**  
 Your mission is to create a backend system in **Python** that manages a set of **characters** and their **attributes**. This will be the first building block of your adventure world — the **Character API** — a registry where all heroes, villains, and wanderers are stored.

---

### **⚙️ Requirements**

#### **1\. Create a REST API**

Use **FastAPI** to build a simple backend with these endpoints:

| Method | Endpoint | Description |
| ----- | ----- | ----- |
| `GET` | `/characters` | List all characters with their health and attributes |
| `GET` | `/characters/{id}` | Retrieve a single character by ID |
| `PUT` | `/characters/{id}/attributes/{attribute_name}` | Update a specific attribute’s value |
| `POST` | `/characters` | Add a new character |
| `DELETE` | `/characters/{id}` | Delete a character (optional) |

---

#### 

#### **2\. Character Data Model**

Each character must include the following:

| Field | Type | Description |
| ----- | ----- | ----- |
| `id` | int | Unique identifier |
| `name` | string | Character’s name |
| `health` | int (0–100) | Health level |
| `attributes` | dictionary | Key-value pairs of the six attributes below |

##### **Attributes**

Each attribute has a **score (0–100)** and a **description**.

| Attribute | Description | Examples of Use |
| ----- | ----- | ----- |
| **Might** | Physical power and raw strength | Melee damage, carrying capacity, intimidation |
| **Agility** | Speed, reflexes, coordination | Dodging, accuracy, stealth |
| **Vitality** | Endurance and resistance | Health points, poison resistance |
| **Insight** | Perception and pattern recognition | Detecting traps, lies |
| **Arcana** | Knowledge of mystical or technical arts | Spell power, crafting |
| **Presence** | Force of personality and influence | Persuasion, leadership |

---

#### **3\. Data Storage (File-Based)**

Store all characters in a **JSON file** called `characters.json`.

Whenever characters are added, updated, or deleted:

* Read from the file.  
* Modify the data.  
* Write the updated data back to the file.

Example file content:

`[`  
  `{`  
    `"id": 1,`  
    `"name": "Aria Stormblade",`  
    `"health": 95,`  
    `"attributes": {`  
      `"Might": 70,`  
      `"Agility": 80,`  
      `"Vitality": 60,`  
      `"Insight": 75,`  
      `"Arcana": 40,`  
      `"Presence": 85`  
    `}`  
  `}`  
`]`

---

#### **4\. Bonus Challenges**

* Add **validation** (e.g., health and attributes must stay between 0–100).  
* Add a **search** parameter to `/characters` to filter by name.  
* Use **Pydantic models** for type safety.  
* Return proper **HTTP status codes** (e.g., 404 if a character isn’t found).  
* Add **automatic ID assignment** for new characters.

---

### 

### **🧠 Learning Outcomes**

By completing this quest, you will learn:

* How to design and expose REST APIs in Python  
* How to read and write structured data using files  
* Data modeling and validation  
* CRUD operations  
* JSON file persistence  