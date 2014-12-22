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
        exit(1) 
    end
end

task :set_varlib => "/var/lib/btsync"
file "/var/lib/btsync" do mkdir "/var/lib/btsync" end

task :set_conf => "/etc/btsync.conf"
file "/etc/btsync.conf" => "btsync.conf" do
    cp "btsync.conf", "/etc/btsync.conf"
end
CLEAN.include("/etc/btsync.conf")

task :set_init => "/etc/init.d/btsync"
file "/etc/init.d/btsync" => "init.sh" do
    cp "init.sh", "/etc/init.d/btsync"
    sh "chkconfig --add btsync"
end
CLEAN.include("/etc/init.d/btsync")

task :set_bin => "/usr/local/bin/btsync"
file "/usr/local/bin/btsync" => "bin/btsync" do
    cp "bin/btsync", "/usr/local/bin/btsync"
end
CLEAN.include("/usr/local/bin/btsync")