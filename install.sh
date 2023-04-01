# Detect the current shell
current_shell=$(basename "$SHELL")

echo "osh: Detecting current shell"
case $current_shell in
bash)
  rc_file=""
  ;;
zsh)
  rc_file=".zshrc"
  ;;
ksh)
  rc_file=".kshrc"
  ;;
tcsh)
  rc_file=".tcshrc"
  ;;
csh)
  rc_file=".cshrc"
  ;;
fish)
  rc_file=".config/fish/config.fish"
  ;;
*)
  echo "Unrecognized or unsupported shell: $current_shell"
  rc_file=""
  ;;
esac
echo "osh: current shell is $current_shell"
# Append the function to the identified RC file
if [ -n "$rc_file" ]; then
  if [ -n "$(LC_ALL=C type -t osh)" ] && [ "$(LC_ALL=C type -t osh)" = function ]; then
    echo "Looks like osh is already installed. Skipping the installation.
          Please run 'source ~/$rc_file' to make sure it is loaded "
  else
    echo "Installing osh into : ~/$rc_file"
    cat >>"${HOME}/$rc_file" <<'EOF'
osh() {
    last_command=$(fc -ln -1)
    last_command=$(echo "$last_command" | sed 's/^[[:space:]]*//')
    last_output=$(eval "$last_command")
    retVal=$?
    if [ $retVal -ne 0 ]; then
        osh_py "input" "$last_command" "output" "$last_output" "return_code" "$retVal"
    else
        echo "Your last command ran successfully. Please summon me only when something goes wrong."
    fi
}
EOF

  fi

  echo "Osh installed successfully. Please run 'source ~/$rc_file'"

else
  echo "Failed to install osh. rc file not found for the current shell."
fi
