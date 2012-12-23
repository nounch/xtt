# XTermSolarizer


## Description

**XTermSolarizer** is an easily installable bundle providing the dark and the bright version of the [Solarized]((http://ethanschoonover.com/solarized) color theme for *XTerm*. It allows multiple *XTerm* color themes to be run in one *X* session and decouples styling in a non-destructive way using *XTerm's* `-name` feature to extend the default `XTerm` `X` resources class (or any other class that has been defined using *XTerm's* `-class` command line parameter).

Prerequesit: *XTerm* with `color256` option compiled into it. It may also be useful to export the `TERM` enviroment variable (system-depend).

## Details

**XTermSolarizer** gives you everything that *Solarized* has to offer...

![More info could be found here http://ethanschoonover.com/solarized .](http://ethanschoonover.com/solarized/img/solarized-vim.png)

... without any hassle™.


It automagically appends the required configuration lines to the user's `.Xresources` and adds the provided `.Xresources.<themeName>` style sheets to wherever they should go to (default `~/.styleSheets/xtermStyleSheets/`). To ensure a minimal signature in the user's configuration files `.Xresources` only includes one include file (`.Xresources.styleSheetsList`) which then includes all style sheets. **XTermSolarizer** also generates an alias for each style sheet and appends it to the user's shell configuration file.

###Setup

TODO

### Conventions

#### Resource names

Individual style sheet names should match the *X* resource name prefix used in them. The `X` resource name itself should be lowercase to differenciate them from `X` classes.

Example - `.Xresources.solarizedDarkXTerm.template` uses the prefix name solarizedDarkXTerm:

```
! ...
solarizedDarkXTerm*background:              S_base03
solarizedDarkXTerm*foreground:              S_base0
solarizedDarkXTerm*fading:                  40
solarizedDarkXTerm*fadeColor:               S_base03
solarizedDarkXTerm*cursorColor:             S_base1
! ...
```

It is recommended to use the `.Xresources.` prefix to clarify that themes are essentially just `.Xresources` includes and to use the `Suffix` prefix to avoid confusion with future resources setup.

#### File names

All style sheets templates should have a leading `.` since they are valid *X* resource files (and could pententially be merged individually using `xrdb -merge .<themeName>`).

## OS Support & Dependencies

- Python 2.7.2+
- Linux

