# School Manager
_(Needs Python 3.10 or newer.)_
1. Install: `pip install -r requirements.txt` (pytest needed; `anthropic` only for AI comments).
2. Run the app from this folder: `python main.py` — data is saved to `school.json`, logs to `school.log`.
3. Run tests: `pytest -v` (all tests run offline; the AI model is mocked).
4. Optional AI comments: copy `.env.example` to `.env` and add your API key; without it, rule-based comments are used.
5. Code layout: `school/` package (models, grading, storage, ai_comment) + `main.py` (menu) + `tests/`.
