# creo el comando phony serve
.PHONY: serve

serve:
	@echo "Starting Docsify server..."
	docsify serve .