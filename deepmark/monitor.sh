filename=$(echo $1)
frequency=$(echo $2)

while :
do

# time
timestamp=$(python3 -c 'import time; print(time.clock_gettime(1))')

# clock speed (cpu mhz, cpu max mhz, cpu min mhz)
mhz=$(lscpu | grep MHz | tr -s  ' ' | rev | cut -d ' ' -f1 | rev | tr '.,' ' ' | cut -d ' ' -f1 | tr '\n' ',' | tr -d ' ' | sed 's/,$//')

# cpu power draw
cpu_power=$(sudo turbostat --out /tmp/turbo.temp --quiet --cpu 0-3 --show CorWatt --add msr0x199,u32,raw sleep .1; cat /tmp/turbo.temp | head -3 | tail -1 | rev | cut -f1 | rev;)

# cpu temp (cpu temp)
cpu_temp=$(cat /sys/class/thermal/thermal_zone0/temp | tr -d ' ' | sed 's/,$//')

# cpu stats from io stats (%user   %nice %system %iowait  %steal   %idle)
cpu_stats=$(iostat | head -4 | tail -1 | tr ',' '.' | tr -s ' '| tr ' ' ',')

# memory stats (total, used, free, cached)
memory_stats=$(free -w | head -2 | tail -1 | tr -s ' ' | cut -d ' ' -f2-4,7 | tr ' ' ',')

# gpu 0 stats (see below query string)
gpu0_stats=$(nvidia-smi --query-gpu=pstate,temperature.gpu,utilization.gpu,utilization.memory,fan.speed,power.draw,power.limit,clocks.current.graphics,clocks.current.memory --format=csv,noheader,nounits | head -1 | tr -d ' ')

# gpu 1 stats (see below query string)
gpu1_stats=$(nvidia-smi --query-gpu=pstate,temperature.gpu,utilization.gpu,utilization.memory,fan.speed,power.draw,power.limit,clocks.current.graphics,clocks.current.memory --format=csv,noheader,nounits | tail -1 | tr -d ' ')

file=/tmp/"$filename".log
if [ ! -f $file ]
then
	echo time,cpu_power,cpu_mhz,cpu_max_mhz,cpu_min_mhz,cpu_temp,cpu_user,cpu_nice,cpu_system,cpu_iowait,cpu_steal,cpu_idle,ram_total,ram_used,ram_free,ram_cached,gpu_pstate,gpu_temp,gpu_util,gpu_mem_util,gpu_fan,gpu_power,gpu_powerlimit,gpu_clock,gpu_mem_clock,gpu_pstate,gpu_temp,gpu_util,gpu_mem_util,gpu_fan,gpu_power,gpu_powerlimit,gpu_clock,gpu_mem_clock > /tmp/"$filename".log
fi

echo $timestamp,$cpu_power,$mhz,$cpu_temp$cpu_stats,$memory_stats,$gpu0_stats,$gpu1_stats >> /tmp/"$filename".log

sleep $frequency

done
