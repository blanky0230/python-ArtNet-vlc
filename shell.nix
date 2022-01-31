let
  nixpkgs = import <nixpkgs> {};
in
  with nixpkgs;

  stdenv.mkDerivation {
    name = "vlcmedianet";
    buildInputs = [
      python39
      python39Packages.python-vlc
      python39Packages.python-dotenv
      python39Packages.pip
      vlc
      youtube-dl # for downloading test videos
    ];
  }
