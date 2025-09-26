up:
	python manage.py runserver
	
static:
	python manage.py collectstatic --noinput

git:
	git add .
	git commit -m "auto update"
	git push origin main