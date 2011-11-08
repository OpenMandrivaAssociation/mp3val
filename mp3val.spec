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
