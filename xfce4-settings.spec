%define url_ver %(echo %{version} | cut -d. -f1,2)
%define _disable_rebuild_configure 1

Summary:	Configuration settings manager for Xfce
Name:		xfce4-settings
Version:	4.14.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/xfce4-settings/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:  gtk-doc
BuildRequires:  gtk-doc-mkpdf
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(exo-2)
BuildRequires:	pkgconfig(colord)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:	pkgconfig(garcon-1)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(inputproto)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:  pkgconfig(libxfce4kbd-private-3)
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(libxfconf-0)
BuildRequires:	pkgconfig(libxklavier)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xorg-libinput)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  xfce4-dev-tools
Requires:	ldetect-lst

Recommends:	xfce4-screensaver
Recommends:	xfce4-whiskermenu-plugin

%description
Configuration settings manager for Xfce desktop environment.

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS TODO
%{_sysconfdir}/xdg/autostart/xfsettingsd.desktop
%{_sysconfdir}/xdg/menus/xfce-settings-manager.menu
%{_libdir}/xfce4/settings/appearance-install-theme
%{_bindir}/xfce4-*settings*
%{_bindir}/xfce4-find-cursor
%{_bindir}/xfsettingsd
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/devices/*.png
%{_iconsdir}/hicolor/*/apps/xfce4-color-settings.*

#---------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%configure \
	--enable-pluggable-dialogs \
	--enable-xrandr \
	--enable-libnotify \
	--enable-gio-unix \
	--enable-xcursor \
	--enable-libxklavier \
	--enable-pluggable-dialogs \
	--enable-sound-settings \
	--with-pnp-ids-path=%{_datadir}/misc/pnp.ids \
	%{nil}
%make_build

%install
%make_install

# (tpg) this file is in mandriva-xfce-config package
rm -rf %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml

# locales
%find_lang %{name} %{name}.lang
