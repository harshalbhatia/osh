# 💩 OSH (Oh SH!t)


# Usage

```bash
# Install, then go about your everyday business
pip3 install git+https://github.com/harshalbhatia/osh

# When there is an error, call `osh`
$ rm temp
rm: temp: is a directory
$ osh
The `rm` command is used to remove files or directories. In this case, the error message indicates that `temp` is a directory and cannot be removed using the `rm` command alone. To remove a directory, you need to use the `-r` (recursive) flag with the `rm` command. 
The correct command to remove the directory `temp` and its contents is:
rm -r temp
This will recursively remove all files and subdirectories within `temp` and then remove the `temp` directory itself. Please be careful when using the `rm` command with the `-r` flag as it can permanently delete files and directories.
```

# Motivation
A lot of us are already Unix enthusiasts (and some even pros). And we write out everyday commands at the speed of thought. However, we're mere mortals (not LLMs) and even the best of us forget a flag or two sometimes.

For exactly this usecase, we made `osh` which once installed and run, takes in the previously run command and it's corresponding erorr and gives you a helping hand.

# How it works?
Todo
