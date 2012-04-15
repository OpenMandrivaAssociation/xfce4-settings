%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Configuration settings manager for Xfce
Name:		xfce4-settings
Version:	4.9.5
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/xfce4-settings/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	libxfce4ui-devel >= 4.9.0
BuildRequires:	libxfce4util-devel >= 4.9.0
BuildRequires:	xfconf-devel >= 4.9.0
BuildRequires:	exo-devel >= 0.7.2
BuildRequires:	libnotify-devel
Buildrequires:	pkgconfig(garcon-1)
BuildRequires:	libwnck-devel
BuildRequires:	libxklavier-devel >= 5.0
BuildRequires:	libxxf86misc-devel
Requires:	ldetect-lst
Obsoletes:	xfce-mcs-manager < 4.5
Obsoletes:	xfce-mcs-manager-devel
Obsoletes:	xfce-mcs-plugins < 4.5
Obsoletes:	%{mklibname xfce4mcs 3}
Obsoletes:	%{mklibname xfce4mcs 3 -d}
Obsoletes:	%{mklibname xfce4mcs -d}
Provides:	xfce-mcs-manager
Provides:	xfce-mcs-plugins

%description
Configuration settings manager for Xfce desktop environment.

%prep
%setup -q

%build
%configure2_5x \
	--enable-pluggable-dialogs \
	--enable-xrandr \
	--enable-libnotify \
	--enable-gio-unix \
	--enable-xcursor \
	--enable-libxklavier \
	--enable-pluggable-dialogs \
	--enable-sound-settings \
	--with-pnp-ids-path=%{_datadir}/misc/pnp.ids

%make

%install
%makeinstall_std

# (tpg) this file is in mandriva-xfce-config package
rm -rf %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS TODO
%{_sysconfdir}/xdg/autostart/xfsettingsd.desktop
%{_sysconfdir}/xdg/menus/xfce-settings-manager.menu
%{_libdir}/xfce4/settings/appearance-install-theme
%{_bindir}/xfce4-*settings*
%{_bindir}/xfsettingsd
%{_datadir}/applications/*.desktop
