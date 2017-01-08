all:
	./initial.py
	docker build -t v4l-utils .

run:
	docker run -it --rm v4l-utils /bin/bash

clean:
	rm -fr initials

dist-clean: clean
	docker rmi v4l-utils
