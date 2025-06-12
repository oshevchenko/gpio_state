# gpio_state
Check the state of a gpio pin.

```
$ ./copy_to_board.sh 192.168.2.27
gpio_state.tar.gz 100% 3282     1.0MB/s   00:00
untar_install.sh  100%  170    72.7KB/s   00:00
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Files copied to board!
Now run the following commands on board as root:
cd /tmp && ./untar_install.sh gpio_state
python3 -m gpiostate 1
```

Similar to:
```
gpioget gpiochip3 1
```
but inverted.
