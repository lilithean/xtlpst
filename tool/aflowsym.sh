#!/bin/sh
if [ -z "$1" ]; then
  echo "usage: $0 <poscar> [output_file]"
  exit 1
fi
if [ -z "$2" ]; then
  output="sym-$1"
else
  output="$2"
fi
itmp=1
while [ -f "tmp_wyccar.$itmp" ]; do
  itmp=$(( $itmp + 1 ))
done
aflow --wyccar=loose < $1 > "tmp_wyccar.$itmp"
aflow --poscar < "tmp_wyccar.$itmp" > "tmp_poscar.$itmp"
aflow --sprim < "tmp_poscar.$itmp" > "tmp_prim.$itmp"
cp "tmp_prim.$itmp" "$output"
rm "tmp_wyccar.$itmp" "tmp_poscar.$itmp" "tmp_prim.$itmp"

