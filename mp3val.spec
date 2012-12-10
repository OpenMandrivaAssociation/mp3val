%define name mp3val
%define version 0.1.8
%define release %mkrel 2

Summary: Tool to validate and fix MPEG audio files
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://downloads.sourceforge.net/project/%name/%name/%{name}%%20%{version}/%{name}-%{version}-src.tar.gz
Patch: mp3val-0.1.7-src-fix-open.patch
License: GPLv2+
Group: Sound
Url: http://mp3val.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
MP3val is a small, high-speed tool for MPEG audio files validation and
(optionally) fixing problems. It was primarily designed for
verification of MPEG 1 Layer III (MP3) files, but supports also other
MPEG versions and layers.

%prep
%setup -q -n %name-%version-src
%patch -p1
chmod 644 changelog.txt manual.html

%build
%make -f Makefile.linux CXXFLAGS="%optflags"

%install
rm -rf $RPM_BUILD_ROOT
install -m 755 -D %name %buildroot%_bindir/%name

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc changelog.txt manual.html
%_bindir/%name


%changelog
* Tue Nov 08 2011 Götz Waschk <waschk@mandriva.org> 0.1.8-2mdv2012.0
+ Revision: 729033
- rebuild

* Fri Nov 06 2009 Götz Waschk <waschk@mandriva.org> 0.1.8-1mdv2011.0
+ Revision: 460832
- new version
- update source URL

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.1.7-4mdv2010.0
+ Revision: 430101
- rebuild

* Fri Sep 19 2008 Götz Waschk <waschk@mandriva.org> 0.1.7-3mdv2009.0
+ Revision: 285838
- fix build
- update license

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.7-2mdv2008.0
+ Revision: 89951
- rebuild

* Sun Jun 17 2007 Götz Waschk <waschk@mandriva.org> 0.1.7-1mdv2008.0
+ Revision: 40566
- new version

* Tue Apr 17 2007 Götz Waschk <waschk@mandriva.org> 0.1.6-1mdv2007.1
+ Revision: 13554
- Import mp3val



* Tue Apr 10 2007 Götz Waschk <waschk@mandriva.org> 0.1.6-1mdv2007.1
- initial package
