# MoKe-Shadow
###### MoKe _(Mouse-Keyboard)_ Shadow. An automated script for recording keyboard and mouse events, and then calling the script to replay/repeat the activities.

## Usage

Before any initial use delete **temp/log1.txt** and **logs/log.txt**. Unless you'll be using already saved logs)

For listening(/recording):
`python listener.py`

For replaying: `python controller.py`

### NB: there's no hotkey to exit the listener. It exits on **right mouse click**

###### Change the arguments for sleep() method in [listener.py](#) and [controller.py](#) to set sleep time before script starts.
