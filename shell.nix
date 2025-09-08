{ pkgs ? import <nixos> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    docker-compose
    git
    nodejs_22
    openssl
    postgresql_16
    pre-commit
    python313
    tailwindcss
    uv
    yarn
    zsh
  ];

  shellHook = ''
    set -a; source .env; set +a

    # Set up Python environment with uv
    export PYTHONPATH=$PWD:$PYTHONPATH

    # Switch to zsh if not already using it
    if [ "$0" != "${pkgs.zsh}/bin/zsh" ]; then
      exec ${pkgs.zsh}/bin/zsh
    fi
  '';
}

