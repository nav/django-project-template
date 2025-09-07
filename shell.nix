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

    # Django settings
    export DJANGO_SETTINGS_MODULE=portfolio.settings
    export DEBUG=1
    export SECRET_KEY=dev-secret-key-change-in-production

    # Database
    export DATABASE_URL=sqlite:///db.sqlite3

    # Node/NPM environment
    export NODE_PATH=$PWD/node_modules:$NODE_PATH
    export PATH=$PWD/node_modules/.bin:$PATH

    # Activate the uv environment
    source .venv/bin/activate

    # Switch to zsh if not already using it
    if [ "$0" != "${pkgs.zsh}/bin/zsh" ]; then
      exec ${pkgs.zsh}/bin/zsh
    fi
  '';
}

