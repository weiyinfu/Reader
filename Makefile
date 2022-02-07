build:
	cd front&&npm run build
frontend:
	rsync -r --progress  front/dist tencent:/home/ubuntu/app/Reader/front/
build-book:
	export PYTHONPATH=.:$PYTHONPATH && python3 reader/build_db.py
upload:frontend
	echo done