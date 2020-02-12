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
    # if [ ! -d env ]; then
    #     virtualenv env
    # fi
    # . env/bin/activate

    pip install -r requirements.txt
}

function rebuild_db {
	logging "Clean"
	rm -rf "${BASE_DIR}/mysite/db.sqlite3"
	
	rm -rf "${BASE_DIR}/mysite/app/migrations/0001_initial.py"
	python "${BASE_DIR}/mysite/manage.py" "makemigrations" 'app'

	logging "migrate"
	python "${BASE_DIR}/mysite/manage.py" "migrate"
	
	logging "initdb.py"
	python "${BASE_DIR}/mysite/init-user-group-per.py"
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
