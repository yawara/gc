#!/bin/sh
#
# btsync          Start/Stop the BitTorrent Sync daemon.
#
# chkconfig: 2345 90 60
# description: BitTorrent Sync lets you sync 
#              and share an unlimited number of files
#              and folders across all of your trusted devices.

RETVAL=0
prog="btsync"
exec=/usr/bin/btsync
lockfile=/var/lock/subsys/btsync
config=/etc/btsync.conf

# Source function library.
. /etc/rc.d/init.d/functions

[ $UID -eq 0 ]

start() {
    if [ $UID -ne 0 ] ; then
        echo "User has insufficient privilege."
        exit 4
    fi
    [ -x $exec ] || exit 5
    echo -n $"Starting $prog: "
    daemon $prog --config $config
    retval=$?
    echo
    [ $retval -eq 0 ] && touch $lockfile
}

stop() {
    if [ $UID -ne 0 ] ; then
        echo "User has insufficient privilege."
        exit 4
    fi
    echo -n $"Stopping $prog: "
	#if [ -n "`pidfileofproc $exec`" ]; then
		killproc $exec
		RETVAL=3
	#else
	#	failure $"Stopping $prog"
	#fi
    retval=$?
    echo
    [ $retval -eq 0 ] && rm -f $lockfile
}

restart() {
    rh_status_q && stop
    start
}

rh_status() {
    # run checks to determine if the service is running or use generic status
    status -p /var/lib/btsync/sync.pid $prog
}

rh_status_q() {
    rh_status >/dev/null 2>&1
}


case "$1" in
    start)
        rh_status_q && exit 0
        $1
        ;;
    stop)
        rh_status_q || exit 0
        $1
        ;;
    restart)
        $1
        ;;
    status)
        rh_status
        ;;
    *)
        echo $"Usage: $0 {start|stop|status|restart}"
        exit 2
esac
exit $?

