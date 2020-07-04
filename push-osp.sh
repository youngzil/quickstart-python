for i in `git log -p -$1  --name-status|grep java|grep M|awk '{print $2}'`; 
	do 
		echo $i; 
		j=`find ../../osp/osp/ -name ${i##*/}`; 
		echo $j;  
		k=${i%/*}; 
		k=../../osp/osp/$k; 
		echo $k;  
		cp $i $k; 
	done
cd ../../osp/osp
git pull origin master
git add *
git commit -m "chenjc"
git push origin master