{ pkgs }: {
  env = {
    "VIRTUAL_ENV" = "$REPL_HOME/.pythonlibs";
  };
  deps = [
    pkgs.glibcLocales
  ];
}