# Runnable tasks.

include common.mk

all: commands

# CSS=-css chota.css
# CSS=-css neat.css
# CSS=-css picnic.css
# CSS=-css pico.css
# CSS=-css simple.css
# CSS=-css tacit.css
CSS=

## datasets: re-create snailz parameters and datasets
datasets:
	@mkdir -p data/grids
	snailz params --outdir params
	snailz everything --paramsdir params --datadir data

## lint: check code and project
lint:
	@ruff check .
	@python bin/lint.py

## render: convert to HTML
render:
	@python bin/render.py ${CSS}
