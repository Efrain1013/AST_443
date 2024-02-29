#! /bin/bash -u

for file in $(ls -1 ../solved_calibrated_files/*.new)
do
   sex $file -c default.se -CATALOG_NAME $file.cat
done
