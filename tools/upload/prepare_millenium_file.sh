#/bin/bash

set -e
set -u
input_file=$1;
# ORGINAL_FILE_DIR=${input_file%/*}
tmp_dir="/tmp/mbank"; # store temp files in this directory
mkdir -p ${tmp_dir}

[ -f ${input_file} ] ||  { echo "${input_file} does not exist" ; exit 1; }

#1  usuń do nazw kolumn
sed -i '/Data operacji/,$!d' ${input_file}
#2 usuń białe przestrzenie
s2_file_space_fixed="${tmp_dir}/s2_space_fixed.csv"
cat ${input_file} | tr -s " " > ${s2_file_space_fixed};
#3 remove currency and 2 semicolons at the end of line 
sed -i "s/.PLN;;.$//g" ${s2_file_space_fixed}
#4 fix encoding
s4_file_enoding_fixed="${tmp_dir}/s4_enoding_fixed.csv"
iconv -f Windows-1250 -t UTF-8 < ${s2_file_space_fixed} > ${s4_file_enoding_fixed};
#5 remove redundant column "rachunek" , move file to orginal localization
# removed_col_file="final_$(basename ${input_file})";

#zmień nagłówki
sed -i "s/#Data operacji/Date/g" ${s4_file_enoding_fixed};
sed -i "s/#Kategoria/Memo/g" ${s4_file_enoding_fixed};
sed -i "s/#Kwota/Amount/g" ${s4_file_enoding_fixed};
#zmien , w kwoce na .
sed -i "s/,/./g" ${s4_file_enoding_fixed};
#zmien ; na , jako rozdzielnik
sed -i "s/;/,/g" ${s4_file_enoding_fixed};
#remove werid new line characters like ^M
sed -i "s/\r//g" ${s4_file_enoding_fixed};

removed_col_file="converted_mbank_$(date +%Y_%m_%d_%H-%M).csv"
final_file=${PWD}/${removed_col_file};
# final_file=/tmp/mbank/${removed_col_file};

# echo $final_file
cut -d "," --complement -f2,3 ${s4_file_enoding_fixed} > ${final_file};
rm ${PWD}/${input_file};
echo ${final_file};
# echo "/tmp/final_bak.csv";