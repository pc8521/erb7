SHELL := /bin/zsh
.SHELLFLAGS := -c
up:
	source ~/.zshrc && workon erb7
	python manage.py runserver && \
	
static:
	python manage.py collectstatic --noinput

git:
	git add .
	git commit -m "auto update"
	git push origin main