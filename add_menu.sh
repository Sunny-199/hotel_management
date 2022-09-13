#!/bin/bash
python manage.py migrate
#fixtures=$(ls seed/003_roles.json)
#while IFS= read -r fixture; do
#    echo -n "Seeding "
#    echo $fixture
python manage.py loaddata seed/003_roles.json
done <<< "$fixtures"
