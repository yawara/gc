require "rake/clean"

task :default => [:download,:install]

task :download => ["bin", "bin/btsync.tar.gz"]
file "bin" do mkdir "bin" end
file "bin/btsync.tar.gz" do
    sh "wget http://download-new.utorrent.com/endpoint/btsync/os/linux-x64/track/stable -O bin/btsync.tar.gz"
    sh "tar xzvfC bin/btsync.tar.gz bin"
end
CLEAN.include("bin")

task :install => [ :checkuid, :set_varlib, :set_conf, :set_init, :set_bin ]

task :checkuid do
    if Process.uid != 0 
        puts "no root privilege"
        exit(1) end
end

task :set_varlib => "/var/lib/btsync"
file "/var/lib/btsync" do mkdir "/var/lib/btsync" end

task :set_conf => "btsync.conf" do
    cp "btsync.conf" "/etc/btsync.conf"
end
CLEAN.include("/etc/btsync.conf")

task :set_init => "init.sh"
file "/etc/init.d/btsync" do
    cp "init.sh" "/etc/inid.d/btsync"
    sh "chkconfig --add btsync"
end
CLEAN.include("/etc/init.d/btsync")

task :set_bin => "bin/btsync"
file "bin/btsync" do
    cp "bin/btsync" "/usr/local/bin/btsync"
end
CLEAN.include("/usr/local/bin/btsync")

def check prog
    print "checking for #{prog}... "
    if system("test -x $(which #{prog})") then puts "yes" else puts "no" end
end
        
task :configure do
    check "wget"
    check "tar"
end