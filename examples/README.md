# Examples

Here lies a few example applications using vshieldpy. The examples arent intended to be used as is,
but should serve as a good basis on how an application might look like.

## Discord Bot

A simple Discord bot that shows examples of interaction based commands with choice based arguments and proper exception handling for vshieldpy.

### Commands

Currently there is three commands defined in the example. All responses from the commands are sent as ephemeral messages to hide private information. That being said for commands responding with sensitive information or perform destructive actions, it is recommended to put in place some sort of authentication (2FA, Mail OTP or a fixed password at the very least).

All of the commands feature proper choices via python Enums.

![image](https://github.com/airblast-dev/vshieldpy/assets/111659262/1387a54a-69e4-45d7-85a8-820c42bccd9e)


#### get_server
`/get_server` allows you to get a server and its general information by providing a server ID.
The response contains a view with 4 buttons to control it with actions such as `Start`, `Stop`, `Restart` and `FixNetwork`.
![image](https://github.com/airblast-dev/vshieldpy/assets/111659262/905fa036-eae3-4321-8058-f2ca69225b9a)


#### connect_to_server
`/connect_to_server` fetchs a NoVNC connection URI through the API and returns it.


#### start_server_task
`/start_server_task` executes a selected task on the server. If `Reinstall` is selected selecting an OS is required.
