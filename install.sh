# Detect the current shell
current_shell=$(basename "$SHELL")

# Determine the appropriate RC file
case $current_shell in
bash)
  rc_file="${HOME}/.bashrc"
  ;;
zsh)
  rc_file="${HOME}/.zshrc"
  ;;
ksh)
  rc_file="${HOME}/.kshrc"
  ;;
tcsh)
  rc_file="${HOME}/.tcshrc"
  ;;
csh)
  rc_file="${HOME}/.cshrc"
  ;;
fish)
  rc_file="${HOME}/.config/fish/config.fish"
  ;;
*)
  echo "Unrecognized or unsupported shell: $current_shell"
  rc_file=""
  ;;
esac

# Append the function to the identified RC file
if [ -n "$rc_file" ]; then
  echo "Appending the function to the RC file: $rc_file"
  cat >>"$rc_file" <<'EOF'

 osh() {
    last_command=$(fc -ln -1)
    last_command=$(echo "$last_command" | sed 's/^[[:space:]]*//')
    last_output=$(eval "$last_command")
    retVal=$?
    if [ $retVal -ne 0 ]; then
        echo "TBD"
    else
        echo "Your last command ran successfully. Please summon me only when something goes wrong."
    fi
}
EOF
  echo "Functionality installer successfully. Please run `source $rc_file`"

else
  echo "Could not append the function to the RC file."
fi
