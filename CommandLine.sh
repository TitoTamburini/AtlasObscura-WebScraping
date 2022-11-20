!#/bin/bash

# START

wget https://ersecchiodetito.s3.amazonaws.com/merged.tsv

echo "How many places can be found in each country?"
echo ''
echo "Italy :" $(cut -f 8 merged.tsv | grep -c 'Italy\s*$')
echo "Spain :" $(cut -f 8 merged.tsv | grep -c 'Spain\s*$')
echo "France :" $(cut -f 8 merged.tsv | grep -c 'France\s*$')
echo "England :" $(cut -f 8 merged.tsv | grep -c 'England')
echo "United States :" $(cut -f 8 merged.tsv | grep -c 'United States\s*$')
echo ''
echo ''
echo "How many people, on average, have visited the places in each country?"
echo ''
echo "Italy :" $(cut -f 3,8 merged.tsv | grep 'Italy\s*$' | awk '{ total += $0 } END { print total/NR }')
echo "Spain :" $(cut -f 3,8 merged.tsv | grep 'Spain\s*$' | awk '{ total += $0 } END { print total/NR }')
echo "France :" $(cut -f 3,8 merged.tsv | grep 'France\s*$' | awk '{ total += $0 } END { print total/NR }')
echo "England :" $(cut -f 3,8 merged.tsv | grep 'England' | awk '{ total += $0 } END { print total/NR }')
echo "United States :" $(cut -f 3,8 merged.tsv | grep 'United States\s*$' | awk '{ total += $0 } END { print total/NR }')
echo '' 
echo ''
echo "How many people in total want to visit the places in each country?"
echo '' 
echo "Italy :" $(cut -f 4,8 merged.tsv | grep 'Italy\s*$' | awk '{ total += $0 } END {print total}')
echo "Spain :" $(cut -f 4,8 merged.tsv | grep 'Spain\s*$' | awk '{ total += $0 } END {print total}')
echo "France :" $(cut -f 4,8 merged.tsv | grep 'France\s*$' | awk '{ total += $0 } END {print total}')
echo "England :" $(cut -f 4,8 merged.tsv | grep 'England' | awk '{ total += $0 } END {print total}')
echo "United States :" $(cut -f 4,8 merged.tsv | grep 'United States\s*$' | awk '{ total += $0 } END {print total}')

# END
