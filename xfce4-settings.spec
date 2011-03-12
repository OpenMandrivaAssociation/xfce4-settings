%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Configuration settings manager for Xfce
Name:		xfce4-settings
Version:	4.8.1
Release:	%mkrel 2
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/xfce4-settings/%{url_ver}/%{name}-%{version}.tar.bz2
Patch1:		xfce4-settings-4.5.99.1-format_not_a_string_literal_and_no_format_arguments.patch
BuildRequires:	libxfce4ui-devel >= 4.6.0
BuildRequires:	libxfcegui4-devel >= 4.7.0
BuildRequires:	xfconf-devel >= 4.7.0
BuildRequires:	exo-devel >= 0.5.4
BuildRequires:	libnotify-devel
BuildRequires:	libglade2-devel
BuildRequires:	libwnck-devel
BuildRequires:	libxklavier-devel >= 5.0
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
#%patch1 -p1

%build
%configure2_5x \
	--enable-sound-settings \
	--enable-xsettings-daemon \
	--enable-libnotify \
	--enable-xrandr \
	--enable-xcursor \
	--enable-libxklavier \
	--enable-pluggable-dialogs \
	--with-pnp-ids-path=%{_datadir}/misc/pnp.ids

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

# (tpg) this file is in mandriva-xfce-config package
rm -rf %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml

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
