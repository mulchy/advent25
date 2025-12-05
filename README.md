```bash
uvx ruff check
uvx ruff format --check

uvx ty check
uvx mypy .
npx pyright

uv run pytest

for i in {01..12}
do
    echo "Day ${i}"
    uv run python -m advent.day${i} < inputs/day${i}.txt
    echo
done
```