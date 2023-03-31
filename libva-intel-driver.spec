%global optflags %{optflags} -O3

Summary:	VA-API implementation for Intel chipsets
Name:		libva-intel-driver
Version:	2.4.1
Release:	2
Group:		Video
License:	GPLv2+
Url:		http://cgit.freedesktop.org/vaapi/intel-driver/
Source0:	https://github.com/01org/intel-vaapi-driver/releases/download/%{version}/intel-vaapi-driver-%{version}.tar.bz2
ExclusiveArch:	%{ix86} %{x86_64}
BuildRequires:	pkgconfig(libva) >= 1.1.0
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libdrm_intel)
BuildRequires:  pkgconfig(x11)
Obsoletes:	vaapi-driver-i965 < 1.0.15
%rename		vaapi-driver-intel

%description
libva-driver-intel is the VA-API implementation for Intel chipsets
and Intel HD Graphics for Intel Core processor family.

%files
%{_libdir}/dri/*_drv_video.so

#--------------------------------------------------------------------------

%prep
%autosetup -n intel-vaapi-driver-%{version} -p1

%build
%configure
%make_build

%install
%make_install

rm -f %{buildroot}%{_libdir}/dri/*.la
rm -rf %{buildroot}%{_datadir}/
