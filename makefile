install:
	uv sync


package:
	hatchling build


brain-games:
	uv run brain-games


build:
	uv build


package-install:
	uv tool install dist/*.whl


run:
	brain-games
