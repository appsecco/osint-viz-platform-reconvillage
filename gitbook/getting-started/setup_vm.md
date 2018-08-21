# Getting Started



## Steps to get started
1. Copy the ova file to a local drive
2. Install Virtual Box (skip if already installed)
3. Import the Virtual Machine Appliance
4. Ensure all the settings are working

### Virtualbox Host-Only Adapter

![host-only-adapter](imgs/host_only_adapter.png)

![host-only](imgs/host_only.png)

### Virtualbox NatNetwork  Adapter

![nat-network](imgs/nat_network.png)

### Setting up the virtual machine



#### Import the Appliance 

![import](imgs/import_ova.png)



#### Settings for Appliance Import

![import-settings](imgs/import_settings.png)



#### If you face an error while importing
![network-settings](imgs/network_settings.png)



#### Virtual Machine Imported


![imported](imgs/imported.png)



- Start the `osint-viz` VM

![start](imgs/start_vm.png)



#### Login into the VM and open terminal

- Username: **student**
- Password: **osintviz@dc26**



#### Are you able to ping a machine on the Internet from the VM?

```
ping appsecco.com
```

#### Are you able to access the services on VM from the host?

- In your host machine, navigate to **VM-IP-ADDRESS**