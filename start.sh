#!/usr/bin/env bash

pushd `dirname $0` > /dev/null
BASE_DIR=`pwd -P`
popd > /dev/null

#############
# Functions
#############
function logging {
    echo "[INFO] $*"
}

function build_venv {
    if [ ! -d env375 ]; then
        virtualenv env375
    fi
    . env375/bin/activate

    pip3 install -r requirements.txt
}

function rebuild_db {
	logging "Clean"
	rm -rf "${BASE_DIR}/mysite/db.sqlite3"

	rm -rf "users/migrations/0*.*"
	rm -rf "organization/migrations/0*.*"
	rm -rf "course/migrations/0*.*"	
	rm -rf "operation/migrations/0*.*"			
		

	rm -rf "xadmin/migrations/0*.*"
	
	logging "makemigrations" "makemigrations" "users"
	python "${BASE_DIR}/mysite/manage.py" "makemigrations" "users"

	logging "makemigrations" "makemigrations" "organization"
	python "${BASE_DIR}/mysite/manage.py" "makemigrations" "organization"

	logging "makemigrations" "makemigrations" "course"
	python "${BASE_DIR}/mysite/manage.py" "makemigrations" "course"

	logging "makemigrations" "makemigrations" "operation"
	python "${BASE_DIR}/mysite/manage.py" "makemigrations" "operation"

	logging "makemigrations" "makemigrations" "xadmin"
	python "${BASE_DIR}/mysite/manage.py" "makemigrations" "xadmin"



	logging "migrate"
	python "${BASE_DIR}/mysite/manage.py" "migrate"
	
	logging "initdb.py"
	python "${BASE_DIR}/mysite/initdb.py"
}

function launch_webapp {
    cd ${BASE_DIR}/mysite
    python "manage.py" "runserver"
}

#############
# Main
#############
cd ${BASE_DIR}
OPT_ENV_FORCE=$1

build_venv

if [ "${OPT_ENV_FORCE}x" == "-ix" ];then
    rebuild_db
fi

launch_webapp
