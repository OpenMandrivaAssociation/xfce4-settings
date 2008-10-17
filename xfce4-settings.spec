Summary:	Configuration settings manager for Xfce
Name:		xfce4-settings
Version:	4.5.91
Release:	%mkrel 2
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://www.xfce.org
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	libxfcegui4-devel >= 4.5.91
BuildRequires:	xfconf-devel
BuildRequires:	exo-devel >= 0.3.91
BuildRequires:	libnotify-devel
BuildRequires:	libglade2-devel
BuildRequires:	libwnck-devel
BuildRequires:	libxklavier-devel
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
Configuration settings manager for Xfce.

%prep
%setup -q

%build
%configure2_5x \
	--enable-sound-settings \
	--enable-xsettings-daemon

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
%{_sysconfdir}/xdg/autostart/xfce4-settings-helper-autostart.desktop
%{_bindir}/xfce4-*settings*
%{_bindir}/xfsettingsd
%{_datadir}/applications/*.desktop
