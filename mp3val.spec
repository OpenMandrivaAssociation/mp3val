%define name mp3val
%define version 0.1.7
%define release %mkrel 4

Summary: Tool to validate and fix MPEG audio files
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}-src.tar.bz2
License: GPL
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
