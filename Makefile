setup:
	pip3 install pip setuptools pipenv --upgrade
	pipenv install

dev: setup
	pipenv shell

lint:
	flake8 ./ \
	    --exclude=.git,slides,previous-course-code-samples \
	    --max-complexity 12 \
	    --ignore=E501
