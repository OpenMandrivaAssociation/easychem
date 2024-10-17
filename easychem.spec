%define _enable_debug_packages	%{nil}
%define debug_package		%{nil}

Name:		easychem
Summary:	2D molecular drawing program
Version:	0.6
Release:	8

Source0:	http://puzzle.dl.sourceforge.net/sourceforge/easychem/%{name}-%{version}.tar.bz2
Patch0:		easychem-0.6-rosa-linkage.patch
URL:		https://easychem.sourceforge.net/
License:	GPLv2+
Group:		Sciences/Chemistry
BuildRequires:	gtk2-devel

%description
EasyChem is a program designed to draw chemical molecules.  The problem in all
existing programs is: they intend to be easy to use at first try, kind of a
quick-and-dirty approach. EasyChem would be a bit difficult to learn, but when
you master it, you can be very fast, and with a huge precision. In fact, it's
just like a specialized vectorial drawing tool.

%prep
%setup -q
%patch0 -p1

%build
%make -f Makefile.linux C_FLAGS="%{?optflags} %{?ldflags}"

%install
install -D -m755 %{name} %{buildroot}/%{_bindir}/%{name}

#menu

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=EasyChem
Comment=2D Molecule Editor
Exec=%{name}
Icon=chemistry_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Sciences-Chemistry;Science;Chemistry;
EOF

%files
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6-6mdv2011.0
+ Revision: 617949
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.6-5mdv2010.0
+ Revision: 428440
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.6-4mdv2009.0
+ Revision: 244603
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.6-2mdv2008.1
+ Revision: 140723
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import easychem


* Tue Sep 05 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.6-2mdv2007.0
- XDG

* Tue Jul 5 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.6-1mdk
- 0.6
- %%mkrel
- rpmbuildupdate friendly

* Sun May 2 2004 Austin Acton <austin@mandrake.org> 0.5-1mdk
- 0.5

* Wed Jan 28 2004 Austin Acton <austin@mandrake.org> 0.3-1mdk
- initial package
