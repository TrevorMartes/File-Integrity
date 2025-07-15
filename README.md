
# FIM (File Integrity Monitor)

FIM is a lightweight Python-based File Integrity Monitoring tool that helps track changes in file contents by storing file hashes and checking for modifications. Whether you're verifying file authenticity or tracking unauthorized changes, FIM is a simple and effective tool to add to your security toolkit.

---

## 🔍 Features

- Create a baseline hash for any file
- Check the integrity of files by comparing them against the stored baseline
- Store file hashes and metadata in a local SQLite database
- Interactive terminal-based script
- Upcoming CLI support via `run.py` using command-line arguments

---

## 🚀 Getting Started

### Option 1: Use the Interactive Script

```bash
python FIM.py
````

You’ll be prompted to:

* Enter a file ie. FIM.py
* Choose whether to add it to the baseline or check its integrity
* View the result of the scan/check

---

### Option 2: Use the CLI Tool (In Progress)

```bash
# First scan (file added to DB)
python run.py scan path/to/file.txt
# Output: Baseline created or updated for (filepath).

# Second scan (same file, unchanged)
python run.py scan path/to/file.txt
# Output: Baseline for (filepath) already exists. File is unchanged.

# Third scan (file modified)
python run.py scan path/to/file.txt
# Output: File already exists with different hash. Use --force to update baseline.

# Update it
python run.py scan path/to/file.txt --force
# Output: Baseline created or updated for (filepath).

# Check Integrity (same hash)
python run.py check path/to/file.txt
# Output: No changes have been made to the file (filepath).

# Check Integrity (different hash)
python run.py check path/to/file.txt
# Output: WARNING: The file {filepath} has been changed *Integrity may be compromised!
```

*(This feature is currently under development but will be included in the repo.)*

---

## 📦 Dependencies

For the CLI (coming soon):

* `typer` (Install with `pip install typer[all]`)

---

## 🔧 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/TrevorMartes/File-Integrity.git
   cd FIM
   ```

2. Ensure you have Python 3.x installed:

   ```bash
   python --version
   ```

3. Set file permissions (if needed):

   ```bash
   chmod +x FIM.py
   ```

4. Run the script:

   ```bash
   python FIM.py
   ```

> 📌 *Note: No additional configuration is required at this time.*

---

## 📁 Roadmap

* [x] Interactive script for baseline and integrity check
* [x] CLI support via `run.py` and `typer`
* [ ] Directory scanning
* [ ] File monitoring over time
* [ ] Alert system (email/log)

---

## 📜 License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](./LICENSE) file for details.

---

## 👤 Author

Developed by **\TrevorMartes**

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📫 Contact

Feel free to reach out via GitHub issues or open a discussion in the repository.

