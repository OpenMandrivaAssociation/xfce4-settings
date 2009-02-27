Summary:	Configuration settings manager for Xfce
Name:		xfce4-settings
Version:	4.6.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://www.xfce.org
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
Patch0:		xfce4-settings-4.5.92-fix-desktop-entry.patch
Patch1:		xfce4-settings-4.5.99.1-format_not_a_string_literal_and_no_format_arguments.patch
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	xfconf-devel >= %{version}
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
%patch0 -p1
%patch1 -p1

%build
%configure2_5x \
	--enable-sound-settings \
	--enable-xsettings-daemon \
	--enable-libnotify \
	--enable-xcursor \
	--enable-libxklavier

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
