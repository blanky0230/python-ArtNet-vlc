let
  nixpkgs = import <nixpkgs> {};

  stupidArtnet = nixpkgs.python39Packages.buildPythonPackage rec {
    pname = "stupidArtnet";
    version = "1.1.0";

    src = nixpkgs.python39Packages.fetchPypi {
      inherit version pname;
      sha256 = "16frx706wrhxq3j66rajfzawg5lqv9yfrwhcmbiq1z5jn4iqgm28";
    };

    doCheck = false;
  };

  pyinstaller-hooks-contrib = nixpkgs.python39Packages.buildPythonPackage rec {
    pname = "pyinstaller-hooks-contrib";
    version = "2022.2";

    src = nixpkgs.python39Packages.fetchPypi {
      inherit version pname;
      sha256 = "07hfqxqaqzgg8qxhc12b2416vb0bk0fsbbn6n3vzy5ih0pz187db";
    };

    doCheck = false;
  };

  altgraph = nixpkgs.python39Packages.buildPythonPackage rec {
    pname = "altgraph";
    version = "0.17.2";

    src = nixpkgs.python39Packages.fetchPypi {
      inherit version pname;
      sha256 = "0n4ihdwzp42gfnqzwlbwq43wdjz4yqwn8scfp2rrfzdlc69jdwpb";
    };

    doCheck = false;
  };

  pyInstaller = nixpkgs.python39Packages.buildPythonPackage rec {
    pname = "pyinstaller";
    version = "4.9";

    src = nixpkgs.python39Packages.fetchPypi {
      inherit version pname;
      sha256 = "1y94zq53dw1hflnv1kd7svsrhkm5zy86yjzrkhgw86w7b2k818bm";
    };
    buildInputs = [nixpkgs.zlib altgraph pyinstaller-hooks-contrib];

    doCheck = false;
  };

in
  with nixpkgs;

  stdenv.mkDerivation {
    name = "vlcmedianet";
    buildInputs = [
      python39
      python39Packages.python-vlc
      python39Packages.python-dotenv
      python39Packages.pip
      python39Packages.tkinter
      pyInstaller
      altgraph
      pyinstaller-hooks-contrib
      stupidArtnet
      vlc
      youtube-dl # for downloading test videos
    ];
  }
