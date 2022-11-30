notes to self on archlinux setup
================================

## setup keyboard

loadkeys de-latin1

## check netconnect

```sh
ip link
ping archlinux.org
```

if this fails, run:

```sh
dhcpcd
```
## make efi and root partitions

### Sector to mb conversion


One sector = 256 bytes
One kilo-byte = 1,024 bytes = 4 sectors
One page = 4,096 bytes = 4k = 16 sectors
One mega-byte = 1,024 k-bytes = 256 pages = 4,096 sectors = 1,048,576 bytes
One giga-byte = 1,024 m-bytes = 262,144 pages = 1,048,576 k-bytes = 1,073,741,824 bytes 


#### root 

```
mkfs.ext4 /dev/<root>
```

+ set to /dev/sda2 on acer 09.05.2022

#### efi

```
mkfs.fat -F 32 /dev/<efi_system_partition>
```

+ set to /dev/sda1 on acer 09.05.2022

## mount newly created partitions

```
mount /dev/<root> /mnt
mount --mkdir /dev/<efi_system_partition> /mnt/boot
```

# enter the archroot


## run pacstrap command

```
pacstrap /mnt sudo efibootmgr os-prober networkmanager grub gvfs gvfs-mtp
xdg-user-dirs base linux linux-firmware vi dhcpcd man-db man-pages texinfo
e2fsprogs
```


## setup efi bootloader

check current config 

```
efibootmgr -v
```

remove if necessary 

```

```

setup new image

### get part uuid of root mount point
`PARTUUID=$(lsblk /dev/sda3 -o PARTUUID -d -n)`


```
efibootmgr --create --label "Arch Linux" -l /vmlinuz-linux -u
"root=PARTUUID=$PARTUUID initrd=/initramfs-linux.img quiet loglevel=0"
```


### boot with different kernel parameters

remove a boot entry:

`efibootmgr -Bb 000<N>`

#### cgroups v1 enabled

```
efibootmgr --create --label "Arch Linux cgroups1" -l /vmlinuz-linux -u
"root=PARTUUID=$PARTUUID initrd=/initramfs-linux.img quiet loglevel=0"
```


## useful setup script

look at [wincent's script](https://raw.githubusercontent.com/wincent/wincent/master/contrib/arch-linux/arch-linux-install.sh)
