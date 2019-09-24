./monitor.sh $1 1 &
_pid_=$(echo $!)

#python deepmark.py $2 $3 $4 $5
python deepmark.py $2 $3 $4 $5 &> /dev/null

kill -9 $_pid_

echo -e "\n Benchmarking Done! \n"
