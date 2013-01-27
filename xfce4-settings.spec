%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Configuration settings manager for Xfce
Name:		xfce4-settings
Version:	4.10.0
Release:	3
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/xfce4-settings/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	libxfce4ui-devel >= 4.10.0
BuildRequires:	libxfce4util-devel >= 4.10.0
BuildRequires:	xfconf-devel >= 4.10.0
BuildRequires:	exo-devel >= 0.8.0
BuildRequires:	libnotify-devel
BuildRequires:	pkgconfig(garcon-1)
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
Provides:	xfce-mcs-manager = %{version}
Provides:	xfce-mcs-plugins = %{version}

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
#rm -rf %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS TODO
%{_sysconfdir}/xdg/autostart/xfsettingsd.desktop
%{_sysconfdir}/xdg/menus/xfce-settings-manager.menu
%config(noreplace) %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/*.xml
%{_libdir}/xfce4/settings/appearance-install-theme
%{_bindir}/xfce4-*settings*
%{_bindir}/xfsettingsd
%{_datadir}/applications/*.desktop


%changelog
* Sat May 05 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.10.0-1
+ Revision: 796423
- adjust buildrequires version
- update to new version 4.10.0

* Sun Apr 15 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.5-1
+ Revision: 791047
- update to new version 4.9.5

* Wed Apr 04 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.4-1
+ Revision: 789238
- update to new version 4.9.4
- update buildrequires
- update file list
- drop old stuff from spec file

* Fri Sep 23 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.3-1
+ Revision: 701027
- update to new version 4.8.3

* Sun May 22 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.2-1
+ Revision: 677294
- update to new version 4.8.2

* Tue Apr 19 2011 Funda Wang <fwang@mandriva.org> 4.8.1-3
+ Revision: 656004
- rebuild for new libnotify 0.7

* Sat Mar 12 2011 Funda Wang <fwang@mandriva.org> 4.8.1-2
+ Revision: 643889
- rebuild to obsolete old packages

* Wed Feb 02 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.1-1
+ Revision: 634988
- update to new version 4.8.1

* Sat Jan 22 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.0-1
+ Revision: 632337
- update to new version 4.8.0

* Thu Jan 06 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.7-1mdv2011.0
+ Revision: 629101
- update to new version 4.7.7

* Wed Dec 08 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.6-1mdv2011.0
+ Revision: 616398
- update to new version 4.7.6

* Sat Dec 04 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.5-1mdv2011.0
+ Revision: 609504
- add versioned buildrequires on libxfcegui4-devel

* Sun Nov 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.4-1mdv2011.0
+ Revision: 594779
- update to new version 4.7.4

* Sat Nov 06 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.3-1mdv2011.0
+ Revision: 593820
- update to new version 4.7.3

* Sat Sep 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.2-1mdv2011.0
+ Revision: 579351
- update to new version 4.7.2
- update configure options
- update buildrequires

* Fri Jul 16 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.5-1mdv2011.0
+ Revision: 553885
- update to new version 4.6.5
- drop patch 0, fixed by upstream

* Mon Jan 11 2010 Götz Waschk <waschk@mandriva.org> 4.6.4-2mdv2010.1
+ Revision: 489692
- patch for new libxklavier

* Sat Jan 02 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.4-1mdv2010.1
+ Revision: 485061
- update to new version 4.6.4
- drop patch 2, fixed upstream

* Thu Nov 12 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.3-3mdv2010.1
+ Revision: 465100
- Patch2: fix detecting newer libXi versions

* Wed Nov 11 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.3-2mdv2010.1
+ Revision: 464912
- rebuild for new X11 librariers

* Tue Oct 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.3-1mdv2010.0
+ Revision: 455242
- update to new version 4.6.3
- drop pacthes 0, 2, 3 and 4 as they were fixed by upstream
- adapt to new URL schemas for Xfce sources

* Wed Jul 08 2009 Götz Waschk <waschk@mandriva.org> 4.6.1-3mdv2010.0
+ Revision: 393441
- build with new libxklavier (bug #52028)

* Wed Jun 17 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-2mdv2010.0
+ Revision: 386851
- Patch2: avoind timing out of xfce4-session on startup
- Patch3: fix two typos in keyboard settings dialog

* Tue Apr 21 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-1mdv2010.0
+ Revision: 368578
- update to new version 4.6.1

* Sun Apr 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-5mdv2009.1
+ Revision: 364247
- Patch3: do not set keyboard layout by default
- Patch4: use folder name for selecting the icon and theme style

* Tue Mar 17 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-4mdv2009.1
+ Revision: 356959
- Patch2: select the correct refresh rate in the display dialog

* Sat Mar 14 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-3mdv2009.1
+ Revision: 355023
- Patch2: changing screen resolution works again
- enable embedded dialogs in xfce4-settings
- extend description

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-2mdv2009.1
+ Revision: 349230
- rebuild whole xfce

* Fri Feb 27 2009 Jérôme Soyer <saispo@mandriva.org> 4.6.0-1mdv2009.1
+ Revision: 345708
- New upstream release

* Tue Jan 27 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.99.1-1mdv2009.1
+ Revision: 333982
- update to new version 4.5.99.1
- Patch1: fix build with -Werror=format-security
- use versionate buildrequires on xfconf-devel

* Wed Jan 14 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.93-1mdv2009.1
+ Revision: 329518
- update to new version 4.5.93

* Wed Jan 07 2009 Götz Waschk <waschk@mandriva.org> 4.5.92-2mdv2009.1
+ Revision: 326459
- fix desktop entry

* Sat Nov 15 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.92-1mdv2009.1
+ Revision: 303562
- exclude xsettings.xml, as it should go to mandriva-xfce-config
- add full path for the Source0
- update to new version 4.5.92 (Xfce 4.6 Beta 2 Hopper)

* Fri Oct 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.91-3mdv2009.1
+ Revision: 294738
- obsolete xfce-mcs library, manager and plugins

* Thu Oct 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.91-1mdv2009.1
+ Revision: 294458
- Xfce4.6 beta1 is landing on cooker
- add source and spec files
- Created package structure for xfce4-settings.

