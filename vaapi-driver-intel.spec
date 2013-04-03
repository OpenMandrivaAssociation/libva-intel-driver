%define oname	intel-driver

Summary:	Is the VA-API implementation for Intel G45 chipsets
Name:		vaapi-driver-intel
Version:	1.0.20
Release:	1
Group:		Video
License:	GPLv2+
URL:		http://cgit.freedesktop.org/vaapi/intel-driver/
Source0:	http://cgit.freedesktop.org/vaapi/intel-driver/snapshot/%{oname}-%{version}.zip
BuildRequires:	libva-devel => 1.0.15
Provides:	%{oname} = %{version}-%{release}
Obsoletes:	vaapi-driver-i965

%description
libva-driver-intel is the VA-API implementation for Intel G45 chipsets
and Intel HD Graphics for Intel Core processor family.


%prep
%setup -q -n %oname-%version

%build
autoreconf -v --install
%configure2_5x
%make

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/dri/*.la

%files
%doc AUTHORS NEWS
%{_libdir}/dri/*_drv_video.so


%changelog
* Wed Jun 13 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.18-1
+ Revision: 805359
- version update 1.0.18

* Thu Apr 19 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.17-1
+ Revision: 791972
- version update 1.0.17

* Sat Nov 05 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.0.15-2
+ Revision: 719700
- description fix removed all vdpau comments
- bs libva-devel fix again
- testing libva again
- release bump for testing libva-devel 1.0.15
- BuildReq fix for libva
- spec fixes for mandriva package policy
- imported package vaapi-driver-intel

