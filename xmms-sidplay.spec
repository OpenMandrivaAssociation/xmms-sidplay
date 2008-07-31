%define name xmms-sidplay
%define version 0.40
%define release %mkrel 15

Name:          %name
Version:       %version
Release:       %release
Summary:       SidPlay Output plugin for XMMS
Group:         Sound
URL:           http://www.lysator.liu.se/~hallon/sidplay.html
License:       GPL
BuildRequires: libxmms-devel
BuildRequires: sidplay-devel
Source:        %name-%version.tar.bz2
Patch:	       xmms-sidplay-0.40-linking.patch
BuildRoot:     %_tmppath/%name-buildroot
BuildRequires: automake1.4
Requires:      xmms

%description
This is an input plugin for xmms based on libsidplay and is used to play 
Commodore 64 SID music. You can drag the slide bar to switch the subsongs.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q
%patch
rm -f configure
automake-1.4
autoconf

%build
%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT
make install libdir=$RPM_BUILD_ROOT%{_libdir}/xmms/Input
rm -f %buildroot%{_libdir}/xmms/Input/*a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/xmms/Input/libsidplay.so

