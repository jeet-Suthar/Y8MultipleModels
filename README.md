# Y8MultipleModels

### Train YOLO model from different datasets with different class IDs.

As you have might have already realized that if you want to train an YOLO model on different pre-made datasets, you need to change class IDs of each an every class from previous dataset to your new set of class ID. So it directly means that you have to go in each .txt file and change it by yourself.

It is quite doable if your dataset is of small size, but what if you have huge dataset?<br>
It will be nightmare if you have to go each and every file and change it by yourself and not to mention mind boggling files management.

What if you only want some portion of some datasets and some of other dataset? I know all of this is really a pain in A##.<br>
I too faced this, it got me scratching my head untill that Indian _jugadu_ genes inside me woke up and gusse what I created **solution** to this problem.

It's not some kind of ground-breaking technological advancement, just overly complicated file handling stuff and nothing else.

See all the problem lies in that .txt files only, we just need to change that particular class ID from desired .txt file and all will be good to go. 
