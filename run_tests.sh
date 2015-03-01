#!/usr/bin/env bash

eval venv_root="~/.python"
venv="parse-pfsense-python2.7"


function install_venv()
{
        prompt="Install python virtualenv in $venv_root/$venv [y/n]"
        answer=""

        while [[ ! "$answer" =~ ^[yn]$  ]]
        do
           read -p "$prompt" -n 1 answer 
           echo 
        done

        if [ ! x$answer == "xy" ]; then exit 1;fi

        mkdir -p "$venv_root"
        virtualenv --python=python2.7 "$venv_root/$venv"
}

if [ ! -f $venv_root/$venv/bin/activate ]
then
        install_venv
fi

. "$venv_root/$venv/bin/activate"

which nosetests >/dev/null
if [ ! -z $? ]
then
  pip install nose
fi

nosetests
