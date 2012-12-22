# XTermSolarizer


## Description

**XTermSolarizer** is an easily installable bundle providing the dark and the bright version of the [Solarized]((http://ethanschoonover.com/solarized) color theme for *XTerm*. It allows multiple *XTerm* color themes to be run in one *X* session and decouples styling in a non-destructive way using *XTerm's* `-name` feature to extend the default `XTerm` `X` resources class (or any other class that has been defined using *XTerm's* `-class` command line parameter).

## Quick Info

**XTermSolarizer** gives you everything that *Solarized* has to offer...

![More info could be found here http://ethanschoonover.com/solarized .](http://ethanschoonover.com/solarized/img/solarized-vim.png)

... without any hassle™.


It automatically appends the required configuration to the user's `.Xresources` and adds the provided `.Xresources.<themeName>` style sheets to wherever they should go to. To ensure a minimal signature in the user's configuration files `.Xresources` only includes a include file (`.Xresources.styleSheetsList`) which then includes all style sheets. **XTermSolarizer** also generates an alias for each style sheet and appends it to the user's shell configuration file.

###Setup

TODO

### Conventions

#### Resource names

Individual style sheet names should match the *X* resource name prefix used in them.

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

#### File names

All style sheets templates should have a leating dot (`.`) since they are config files.

