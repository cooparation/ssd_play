cur_dir=$(cd $( dirname ${BASH_SOURCE[0]} ) && pwd )

redo=1
data_root_dir="/apps/liusj"
#dataset_name="FoodDetDatasets"
dataset_name="testLabelImgs"
mapfile="./data/labelmap_voc.prototxt"
anno_type="detection"

db="lmdb"
lmdb_path=$data_root_dir/$dataset_name/$db
lmdb_softlink_path=data/$dataset_name
min_dim=0
max_dim=0
width=0
height=0

extra_cmd="--encode-type=jpg --encoded"
if [ $redo ]
then
  extra_cmd="$extra_cmd --redo"
fi
image_root_dir='/'
for subset in test trainval
do
  python create_annoset.py --anno-type='detection' --label-map-file=$mapfile --min-dim=$min_dim --max-dim=$max_dim --resize-width=$width --resize-height=$height --check-label $extra_cmd $image_root_dir ./data/$subset.txt $lmdb_path/$dataset_name"_"$subset"_"$db $lmdb_softlink_path
done
