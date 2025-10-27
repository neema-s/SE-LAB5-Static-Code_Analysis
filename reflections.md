1. Which issues were the easiest to fix, and which were the hardest? Why?
Easiest to fix:
Missing docstrings : Adding concise docstrings to functions and the module header was straightforward since the purpose of each function was clear.
Snake case naming: Renaming functions like addItem to add_item and removeItem to remove_item was mechanical and quick.
String formatting : Converting print statements to f-strings improved readability and consistency easily.
Using .items() in loops : Simple replacement of for i in stock_data with for item, quantity in stock_data.items() fixed both efficiency and clarity issues.

 Hardest to fix:
Global statement : Required a structural rethink of how data was shared across functions. The solution was to avoid modifying global state directly and instead work with return values or parameters.
Broad exception catching : Needed care to ensure that only relevant exceptions (like KeyError or ValueError) were caught without missing real errors.
File handling without encoding or context manager: Needed rewriting with with open(..., encoding='utf-8') to ensure safe file closure and encoding handling.

2. Did the static analysis tools report any false positives? If so, describe one example.
There were no major false positives, but one borderline case, where a global statement was flagged for using a global variable stock_data. While global variables are generally discouraged, it’s an intentional design choice, not an error. Thus, it’s a contextual false positive.

3. How would you integrate static analysis tools into your actual software development workflow?
Local development stage: Run pylint or flake8 before each commit using pre-commit hooks to automatically scan and block code with major issues. Use IDE integration (e.g., VS Code, PyCharm) for real-time linting feedback while coding.
Continuous Integration (CI): Integrate static analysis tools like pylint, flake8, or bandit into a CI pipeline (GitHub Actions, GitLab CI, Jenkins). Set threshold levels — for example, pylint score >= 9.0 must pass before merging pull requests. Combine with code coverage tools to ensure tested and linted code before deployment.

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

Code Quality:
Function naming now follows PEP 8, improving maintainability and consistency.
Removal of dangerous defaults (e.g., mutable list [] as default argument) prevents subtle runtime bugs.

• Readability:
Docstrings make the purpose, arguments, and return values of each function immediately clear.
F-strings and for item, quantity in stock_data.items() make the logic easy to follow.

• Robustness:
Specific exception handling avoids swallowing critical errors silently.
Type checks prevent invalid data from corrupting the inventory state.

