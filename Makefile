# creo el comando phony serve
.PHONY: serve projects

serve:
	@echo "Starting Docsify server..."
	docsify serve .

projects:
	@echo "Building content/projects.md from remote public reports..."
	python3 ufabric-org/projects-sync/scripts/build_projects_page.py \
		--sources ufabric-org/projects-sync/sources.md \
		--output content/projects.md
