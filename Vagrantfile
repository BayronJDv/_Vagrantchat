RAM = "512"
CPUS = "1"
BOX_BASE = "ubuntu/focal64"
VMS = "vms"
VMC = "vmc"

Vagrant.configure("2") do |config|	
  config.vm.box = BOX_BASE

#configuracion de la primer vm "Servidor"

  config.vm.define "vms" do |vms|
    vms.vm.hostname = VMS
    vms.vm.provider :virtualbox do |vb|
        vb.customize [ 'modifyvm', :id, '--memory', RAM ]
        vb.customize [ 'modifyvm', :id, '--cpus', CPUS ]
        vb.customize [ 'modifyvm', :id, '--name', VMS ]

    end
    vms.vm.network "private_network", ip: "192.168.56.50"
    
	vms.vm.provision "shell", path: "script-server.sh"
	
    end 

#configuracion de la segunda vm "Cliente"

  config.vm.define "vmc" do |vmc|
    vmc.vm.hostname = VMC
    vmc.vm.provider :virtualbox do |vb|
        vb.customize [ 'modifyvm', :id, '--memory', RAM ]
        vb.customize [ 'modifyvm', :id, '--cpus', CPUS ]
        vb.customize [ 'modifyvm', :id, '--name', VMC ]

    end
    vmc.vm.network "private_network", ip: "192.168.56.100"
    
    vmc.vm.provision "shell", path: "script-client.sh"
    
    end

end
