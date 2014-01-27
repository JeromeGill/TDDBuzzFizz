Vagrant.configure("2") do |config|
  config.vm.box = "centos64"
  config.vm.box_url = "https://github.com/2creatives/vagrant-centos/releases/download/v0.1.0/centos64-x86_64-20131030.box"

 config.vm.network :private_network, ip: "192.168.21.11"
    config.ssh.forward_agent = true

  config.vm.provider :virtualbox do |v|
    v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    v.customize ["modifyvm", :id, "--memory", 1024]
    v.customize ["modifyvm", :id, "--name", "tddbuzzfizz"]
  end

  config.vm.synced_folder "./", "/opt/JSilky/", id: "vagrant-root"
  config.vm.provision "shell", path: "provision/provision.sh"

end
