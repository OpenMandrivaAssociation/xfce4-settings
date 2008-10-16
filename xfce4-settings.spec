Summary:	Configuration settings manager for Xfce
Name:		xfce4-settings
Version:	4.5.91
Release:	%mkrel 1
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
