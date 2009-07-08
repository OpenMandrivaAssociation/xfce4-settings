Summary:	Configuration settings manager for Xfce
Name:		xfce4-settings
Version:	4.6.1
Release:	%mkrel 3
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://www.xfce.org
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
Patch0:		xfce4-settings-4.5.92-fix-desktop-entry.patch
Patch1:		xfce4-settings-4.5.99.1-format_not_a_string_literal_and_no_format_arguments.patch
Patch2:		xfce4-settings-4.6.1-avoid-timing-out-on-startup.patch
Patch3:		xfce4-settings-4.6.1-keyboard-settings-typos.patch
Patch4:		xfce4-settings-4.6.1-libxklavier4.0.patch
BuildRequires:	libxfcegui4-devel >= 4.6.0
BuildRequires:	xfconf-devel >= 4.6.0
BuildRequires:	exo-devel >= 0.3.100
BuildRequires:	libnotify-devel
BuildRequires:	libglade2-devel
BuildRequires:	libwnck-devel
BuildRequires:	libxklavier-devel >= 4.0
BuildRequires:	libxxf86misc-devel
Obsoletes:	xfce-mcs-manager < 4.5
Obsoletes:	xfce-mcs-manager-devel
Obsoletes:	xfce-mcs-plugins < 4.5
Obsoletes:	%{mklibname xfce4mcs 3}
Obsoletes:	%{mklibname xfce4mcs 3 -d}
Obsoletes:	%{mklibname xfce4mcs -d}
Provides:	xfce-mcs-manager
Provides:	xfce-mcs-plugins
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Configuration settings manager for Xfce desktop environment.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
#patch4:
autoconf

%build
%configure2_5x \
	--enable-sound-settings \
	--enable-xsettings-daemon \
	--enable-libnotify \
	--enable-xcursor \
	--enable-libxklavier \
	--enable-pluggable-dialogs

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS TODO
%exclude %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml
%{_sysconfdir}/xdg/autostart/xfce4-settings-helper-autostart.desktop
%{_bindir}/xfce4-*settings*
%{_bindir}/xfsettingsd
%{_datadir}/applications/*.desktop
