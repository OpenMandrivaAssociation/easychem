%define name	easychem
%define version	0.6
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	2D molecular drawing program
Version: 	%{version}
Release: 	%{release}

Source:		http://puzzle.dl.sourceforge.net/sourceforge/easychem/%{name}-%{version}.tar.bz2
URL:		http://easychem.sourceforge.net/
License:	GPL
Group:		Sciences/Chemistry
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	pkgconfig gtk2-devel

%description
EasyChem is a program designed to draw chemical molecules.  The problem in all
existing programs is: they intend to be easy to use at first try, kind of a
quick-and-dirty approach. EasyChem would be a bit difficult to learn, but when
you master it, you can be very fast, and with a huge precision. In fact, it's
just like a specialized vectorial drawing tool.

%prep
%setup -q

%build
%make -f Makefile.linux C_FLAGS="$RPM_OPT_FLAGS"
										
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir
cp %name $RPM_BUILD_ROOT/%_bindir/

#menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=EasyChem
Comment=2D Molecule Editor
Exec=%{_bindir}/%{name} 
Icon=chemistry_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Sciences-Chemistry;Science;Chemistry;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop

