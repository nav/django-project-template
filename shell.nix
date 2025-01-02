{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.docker-compose
    pkgs.git
    pkgs.nodejs-18_x
    pkgs.openssl
    pkgs.postgresql_16
    pkgs.pre-commit
    pkgs.python312
    pkgs.tailwindcss
    pkgs.uv
    pkgs.yarn
  ];

  shellHook = ''
    set -a; source .env; set +a
  '';
}
