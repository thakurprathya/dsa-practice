# DSA Practice Hub
A comprehensive, systematic approach to mastering Data Structures and Algorithms through deliberate practice and progress tracking.

## 🛠️ Features

### Random Problem Picker
The `picker.py` script randomly selects unsolved problems for blind practice:
- Filters out already solved problems
- Provides problem details without revealing the topic
- Tracks progress automatically

### Progress Tracking
- **CSV/Excel Integration**: Problems stored in `sheet.csv` and `sheet.xlsx`
- **Solved Status**: Mark problems as completed

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/thakurprathya/dsa-practice
   cd dsa-practice
   ```

2. **Set up Python virtual environment** (recommended):
   ```bash
   python -m venv .
   source bin/activate  # On Windows: Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 📝 Usage

### Random Problem Selection

Get a random unsolved problem for practice:

```bash
python picker.py sheet.csv
```

or

```bash
python picker.py sheet.xlsx
```

### Marking Problems as Solved

After solving a problem:

1. Open `sheet.csv` or `sheet.xlsx`
2. Find the problem row
3. Mark the "Solved" column with:
   - ✅ for completed
   - Date when solved
   - Any notes about your solution approach
   - commit for tracking across devices

### Adding New Problems

To add new problems to your practice set:

1. Edit `sheet.csv` or `sheet.xlsx`
2. Add new rows