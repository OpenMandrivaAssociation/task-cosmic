Summary:	Metapackage for COSMIC desktop environment
Name:		task-cosmic
Version:	1.0.0+alpha2
Release:	1
Group:		Graphical desktop/COSMIC
License:	GPLv2+
BuildArch:	noarch

Requires:	%{name}-minimal

Requires: cosmic-ext-tweaks


# Other non branded with COSMIC
Recommends: file-roller
Recommends: firefox
Recommends: clapper


%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the COSMIC.

%package minimal
Summary:	A very minimal COSMIC desktop
Group:		Graphical desktop/COSMIC

Requires: cosmic-settings-daemon
Requires: cosmic-applibrary
# From cosmic-applet
Requires: cosmic-applet-app-list
Requires: cosmic-applet-audio
Requires: cosmic-applet-battery
Requires: cosmic-applet-bluetooth
Requires: cosmic-applet-input-sources
Requires: cosmic-applet-launcher-button
Requires: cosmic-applet-minimize
Requires: cosmic-applet-network
Requires: cosmic-applet-notifications
Requires: cosmic-applet-panel-button
Requires: cosmic-applet-power
Requires: cosmic-applet-status-area
Requires: cosmic-applet-tiling
Requires: cosmic-applet-time
Requires: cosmic-applet-workspaces

Requires: cosmic-bg
Requires: cosmic-comp
Requires: pop-icon-theme
Requires: cosmic-icons
Requires: cosmic-files
Requires: cosmic-edit
Requires: cosmic-launcher
Requires: cosmic-notifications
Requires: cosmic-osd
Requires: cosmic-panel
Requires: cosmic-session
Requires: cosmic-workspaces
Requires: cosmic-randr
Requires: cosmic-settings
Requires: xdg-desktop-portal-cosmic
Requires: cosmic-term
Requires: cosmic-screenshot
Requires: cosmic-store
Requires: pop-launcher
Requires: cosmic-wallpapers

# We should use just greetd+cosmic+greeter but for some reason it boot to command line, instead to GUI. So for now force sane GDM.
Requires: greetd
Requires: cosmic-greeter
Requires: gdm

# TBC
# cosmic-player
# cosmic-reader


%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal GNOME desktop environment.

%files

%files minimal
